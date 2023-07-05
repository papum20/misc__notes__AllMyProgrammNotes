# COMMANDS

// status: untracked/modified -> tracked/to be committed -> “saved”  
`add FILENAME` : add filename to git repo in same folder  
(untracked/modified -> to be committed)  
`add .` : add all  
`branch BRANCH-NAME` : new branch (named …), but current doesn’t change  
`branch` : list of branches (with star next to current one)  
*	`-r` : list remote branches  
*	`-a` : list all branches  
*	`-v` : -verbose  

`branch -d BRANCH` : delete branch  
`branch -D BRANCH` : (stronger, when asked)  
`checkout COMMIT-HASH/BRANCH` : go back to previous commitment  
`checkout -b BRANCH-NAME` : new branch and move to it  
`checkout --track origin/BRANCH` : creates branch `BRANCH` that tracks remote `BRANCH`  
`clean` :  remove untracked files from the working tree  
*	`-d` : remove directories  
*	`-f` : force  
*	`-n` : don’t actually remove anything, just show what would be done  
*	`-X` : Remove only files ignored by git  

`commit -m “string”` : applies changes to be committed and saves them with string (some information)  
*	`(to be committed -> nothing to be committed)`  

`commit -m “string” -m “description”` : commits with another optional string  
`commit -am “string”` : adds and commits (only for modified, not untracked)  
`commit --amend` : edit last commit  
*	`--allow-empty` : empty commit  

`diff COMMIT` : differences from last change  
`diff COMMIT1 COMMIT2` : diff from COMMIT1 to COMMIT2  
*	`--stat` : (colors as GitHub)  

`fetch` :  
*	`--all` :  

`init` : create an empty repository (.git folder)  
`log` : log of changes (commitments) (“in current branch”)  
`log BRANCH` :  
`log REMOTE-REPO/REMOTE_BRANCH` :   
*	`--all` :   
*	`--graph` : show timeline  
*	`--oneline` :   

`log -p -- path-to-file` : show log of file  
*	`--follow` : also show history for when it had another name  

`merge BRANCH` : merges BRANCH current branch  
`rebase NEWBASE` : replaces current banch’s history with the one ending in newbase  
// merge keeps histories visible; rebase hides old history  
// rebase useful when worked alone on a branch, if there were some errors in other files in that branch, you can rebase it on a stable branch, so the environment is working, the history clean and your additional file are added  
`reset` : undos all modified/added files  
`reset FILE` : undo file  
`reset HEAD~N` : undo n commitments  
// HEAD = pointer to last commitment  
`reset COMMIT-HASH` : undo to hash  
`reset --hard COMMIT-HASH` : undo to hash and remove changes  
`rm FILE` : remove file both locally and from repo  
`rm --cached FILE` : only remove from repo  
`rm -r DIRECTORY` : remove directory  
`show ARG` : “search arg in log”  
`show COMMIT:PATH` : show PATH at COMMIT  
`status` : repository info  
*	`--ignored` : status, showing ignored files  

`switch BRANCH` : switch to branch  
  
## GitHub (/ remote repo)  
// row colors: green = updated, red = deleted, white = unchanged  
`clone LINK` : creates repository cloned from a remote one  
`(fork - GitHub` : create a copy of a branch  
	`*	used to modify others’ repos)`  
`pull origin BRANCH` : merge origin/current branch into BRANCH  
`pull -u origin BRANCH` : (as push)  
`pull --allow-unrelated-histories` : (solve to “fatal: refusing to merge unrelated histories)  
// pr=pull request  
`push origin BRANCH` : saves current local branch in branch in repository origin  
`push REPO LOCAL_BRANCH:REMOTE_BRANCH` : saves local branch in remote branch  
		`*	in repo`  
`push -u origin BRANCH` : makes origin BRANCH default  
				`*	-u = short for --set-upstream`  
`push` : –  
`push --delete REPO BRANCH` : delete remote branch  
`push --force REPO REMOTE-BRANCH` : ignores errors and pushes anyway  
`remote` : list of “linked remote repos” (as links)  
`remote -v` : -verbose  
`remote add origin LINK` : add local repo (=origin) to remote at link   
*	and “leave a local link to it”  
`git remote remove REPO` : remove repo (es. origin)  
  
## config  
// email and username are to identify who made a change to file  
`--global` : (parameter) : global for this host  
`config --global --list` : list of config options (file .config)  
`config --global user.name USERNAME` : set username  
`config --global user.email EMAIL` : set email  
  
## ssh  
//ssh generation: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent  
`pbcopy < <file.pub>` : copy public key text  
`ssh-keygen -t rsa -b 4096 -C “email”` : locally generate a key, with   
*	encryption type -t, encr. strength -b, email  
// generates 2 keys: private: to show that it’s your repo when you use one  
// online; public (.pub): to put on GitHub so it compares with the private  
`ssh-keygen -t ed25519 -C “email”` : (admstaff)  
`ssh [-v] [-vvv] [-T] git@github.com` : test connection [v=verbose, vvv=very verbose, T=?]  
  
## GIT-GITHUB linking   
*	`generate ssh key`  
*	`save it in github->settings (public key)`  
*	`copy github repository link (SSH link !)`  
*	`use it for git remote add`  
*	`add key to ssh-agent:`  
*	`eval “$(ssh-agent -s)”		//start ssh-agent`  
*	`ssh-add PATH_TO_KEY	//add private key`  
*	`(ssh-add -l)			//check: saved keys`  
*	`ERROR (public key): see terminal/linux`  
  

## README.md  
*	[README.md](./README.md)  



