# Jonathon: The Helpful Git Assistant

Jonathon is going to be the best virtual assistant ever. He's going to check git repositories for me. Or you.

## User story

1. Introduction
    - I want to check up on my students' work in git repositories
    - There's lots of complexity I have to remember for using git, from the commands to all the different people I want to check up on
    - Jonathon helps do this
2. Setting up
    - I tell Jonathon who or what I want to check up on
    - Jonathon tells me all the repos I'm dealing with
3. Why check-ups?
    - I want to know when updates have happened
    - I want to know whether things broke
    - I want to update my local/remote versions
4. Jonathon's job
    - Jonathon will let me know when updates have happened (without asking)
    - I can ask Jonathon to tell me recent updates for specific repos
    - Jonathon can update my local and remote versions, automatically if I want
    - Jonathon can run my test suites
5. Now I'm super productive! Instead of wasting all my days finding out what's going on myself, Jonathon can do it all for me.

## Query diagram

- "I'm Jumping Jonathon and I'll jump-start your job!"
- "How can I help?"
    + recent updates
        * list all recent updates
    + check {repo}
        * list updates for that repo
    + does {repo} work?
        * run tests for that repo
    + update {repo}
        * git pull
    + do I have local changes?

This is a pretty simple bot without lots of deep levels, so I'll leave it there...

