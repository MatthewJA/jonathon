"""Watches git repositories for breakages."""
import ast
import subprocess
import shutil
import random
import os, re
from pathlib import Path
from contextlib import contextmanager

import exrex

REPO_SSH = 'git@github.com:ncss/projects-2019-2d.git'
BRANCH = 'dev'
CLONE_DIR = Path('.cloned')
RUN_FILE = 'cli_rhyme.py'

@contextmanager
def cwd(path):
    oldpwd=os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)

def setup_repo(repo_ssh=REPO_SSH, branch=BRANCH, clone_dir=CLONE_DIR):
    if not os.path.exists(clone_dir):
        # Clone the repo.
        subprocess.run(['git', 'clone', repo_ssh, clone_dir])
    # Pull.
    with cwd(clone_dir):
        subprocess.run(['git', 'checkout', branch])
        subprocess.run(['git', 'pull', 'origin', branch])

def fuzz_repo(clone_dir=CLONE_DIR, run_file=RUN_FILE):
    # Iterate over all Python files to find regexes.
    regexes = []
    for file in clone_dir.iterdir():
        if file.suffix == '.py':
            with open(file) as f:
                parsetree = ast.parse(f.read())
                for node in ast.walk(parsetree):
                    if isinstance(node, ast.Str):
                        regexes.append(node.s)
    big_regex = '|'.join(re.sub(r'\?P<\w+>', r'', f'(?:{r})') for r in regexes)
    big_regex = exrex.simplify(big_regex)
    with cwd(clone_dir):
        input_string = '\n'.join(exrex.getone(big_regex) for _ in range(10000)).encode('ascii')
        result = subprocess.run(['python3', run_file], input=input_string, stdout=subprocess.PIPE)
        print(result.stdout.decode('ascii'))


states = {
    'NO QUERY': [(r'tell me \d{1,2} (synonym|rhyme)s? (?:for|with) [a-z]{2,5}', 'NO QUERY'),
                 (r'tell me (synonym|rhyme)s? (?:for|with) [a-z]{2,5}', 'WORD')],
    'WORD': [(r'\d{2,5}', 'NO QUERY')],
}

def simulate_statemodel(run_path):
    state = 'NO QUERY'
    queries = []
    for i in range(10):
        query_regex, state = random.choice(states[state])
        query = exrex.getone(query_regex)
        queries.append(query)
    input_string = '\n'.join(queries).encode('ascii')
    print(input_string)
    result = subprocess.run(['python3', run_path], input=input_string, stdout=subprocess.PIPE)
    print(result.stdout.decode('ascii'))


if __name__ == '__main__':
    setup_repo()
    simulate_statemodel(CLONE_DIR / RUN_FILE)
