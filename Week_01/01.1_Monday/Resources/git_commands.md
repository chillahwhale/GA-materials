## Helpful git commands

- `git --help`: Prints out all `git` commands
- `git status`: Prints current commit/ edits status (e.g. changed files)
- `git log --oneline`: print git commit log, limit one line.

**Create a git repository from scratch**
- `git init`: initialize empty repository
- Jump to _Switch remote url_

**Create a git repository from remote url**
- Create a fork on GitHub
- `git clone <link to repo>`: clone the repository
- Jump to _Made changes to your local repo?_

**Switch remote url**
- Why? Perhaps you forked/cloned on GHE but want to push to your personal github
- `git remote -v`
- `git remote set-url origin <url_to_new_github_repo>`
- Jump to _Made changes to your local repo?_

**Made changes to your local repo?**
- `git add .`: stage all recent changes for commit
	- or `git add <path_to_some_file_name> <path_to_another_file_name>` 
- `git commit -m "some message about the commit`: commit the changes
- `git push origin master`: push local changes to remote repo (GitHub)

**Add upstream branch for repo updates**
- `git remote add upstream <link_to_upstream_fork>`: add updated remote repo
- `git pull upstream master`: download updates.
or
- `git fetch upstream master`: fetch changes without merging.

**Branching**
- List branches
	- `git branch -a` 
- Create a new branch
	- `git branch <branchname>`
- Checkout the branch
	- `git checkout <branchname>`
	- shows branches and active branch
- make changes to branch.
	- `git add .` / `git commit -m "changes"` to the new branch
- switch back to master branch to show master is unchanged 
	- `git checkout master`
-  merge code back into master branch
	- `git checkout master`
	- `git merge branchname`
- delete branch with merged features
	- `git branch -d branchname` 
- delete branch without merged features
	- `git branch -D branchname`
- if merging a branch that doesn't have all of master's features
	- "merge made by the 'recursive' strategy.
- if conflict?
	- _Stand by for updates_


