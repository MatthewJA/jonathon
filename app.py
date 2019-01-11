"""Watches git repositories for breakages."""

import subprocess
import shutil
from pathlib import Path

REPO_SSH = 'git@github.com:ncss/projects-2019-2d.git'
BRANCH = 'dev'
CLONE_DIR = Path('.cloned')

def setup_repo(repo_ssh=REPO_SSH, branch=BRANCH, clone_dir=CLONE_DIR):
    shutil.rmtree(clone_dir)
    # Clone the repo.
    subprocess.run(['git', 'clone', repo_ssh, clone_dir])
    # Pull.
    with clone_dir:
        subprocess.run(['git', 'checkout', branch])

# def try_repo():
    
if __name__ == '__main__':
    setup_repo()