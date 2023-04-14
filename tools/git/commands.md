// status: untracked/modified -> tracked/to be committed -> “saved”  
git add <filename> : add filename to git repo in same folder  
(untracked/modified -> to be committed)  
git add . : add all  
git branch : list of branches (with star next to current one)  
git branch -r : list remote branches  
git branch -a : list all branches  
git branch -v : -verbose  
git branch <branch-name> : new branch (named …),  
but current doesn’t change  
git branch -d <branch> : delete branch  
git branch -D <branch> : (stronger, when asked)  
git checkout <commit-hash>/<branch> : go back to previous commitment  
git checkout -b <branch-name> : new branch and move to it  
git checkout --track origin/branch : creates branch named branch that tracks  
		remote branch  
git commit -m “string” : applies changes to be committed and saves them with				 string (some information)  
				(to be committed -> nothing to be committed)  
git commit -m “string” -m “description” : commits with another optional string  
git commit -am “string” : adds and commits (only for modified, not untracked)  
git commit --amend : edit last commit  
git commit --allow-empty : empty commit  
git diff <branch> : differences from last change  
(colors as GitHub)  
git fetch <> :  
git fetch --all :  
git init : create an empty repository (.git folder)  
git log : log of changes (commitments) (“in current branch”)  
git log <branch> :  
git log <remote-repo/remote_branch> :   
	--all :   
--graph :   
	--oneline :   
git log -p -- path-to-file : show log of file  
	--follow : also show history for when it had another name  
git log –graph : show timeline  
git merge <branch> : merges branch with master (branch)  
git rebase <newbase> : replaces current banch’s history with the one ending in newbase  
// merge keeps histories visible; rebase hides old history  
// rebase useful when worked alone on a branch, if there were some errors   
in other files in that branch, you can rebase it on a stable branch,  
so the environment is working, the history clean and your additional file are added  
git reset : undos all modified/added files  
git reset <file> : undo file  
git reset HEAD~<n> : undo n commitments  
HEAD = pointer to last commitment  
git reset <commit-hash> : undo to hash  
git reset --hard <commit-hash> : undo to hash and remove changes  
git rm <file> : remove file both locally and from repo  
git rm --cached <file> : only remove from repo  
git rm -r <directory> : remove directory  
git show <arg> : “search arg in log”  
git status : repository info  
git status --ignored : status, showing ignored files  
git switch <branch> : switch to branch  
  
GitHub (/ remote repo)  
// row colors: green = updated, red = deleted, white = unchanged  
git clone <link> : creates repository cloned from a remote one  
(fork - GitHub : create a copy of a branch  
		used to modify others’ repos)  
git pull origin <branch> : merge origin/current branch into <branch>  
git pull -u origin <branch> : (as push)  
git pull --allow-unrelated-histories : (solve to “fatal: refusing to merge unrelated histories)  
// pr=pull request  
git push origin <branch> : saves current local branch in branch in repository origin  
git push <repo> <local_branch>:<remote_branch> : saves local branch in remote branch  
			in repo  
git push -u origin <branch> : makes origin <branch> default  
					-u = short for --set-upstream  
git push : –  
git push --delete <repo> <branch> : delete remote branch  
git push --force <repo> <remote-branch> : ignores errors and pushes anyway  
git remote : list of “linked remote repos” (as links)  
git remote -v : -verbose  
git remote add origin <link> : add local repo (=origin) to remote at link   
and “leave a local link to it”  
git remote remove <repo> : remove repo (es. origin)  
  
git config  
// email and username are to identify who made a change to file  
--global : (parameter) : global for this host  
git config --global --list : list of config options (file .config)  
git config --global user.name <username> : set username  
git config --global user.email <email> : set email  
  
ssh  
//ssh generation: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent  
pbcopy < <file.pub> : copy public key text  
ssh-keygen -t rsa -b 4096 -C “email” : locally generate a key, with   
encryption type -t, encr. strength -b, email  
// generates 2 keys: private: to show that it’s your repo when you use one  
// online; public (.pub): to put on GitHub so it compares with the private  
ssh-keygen -t ed25519 -C “email” : (admstaff)  
ssh [-v] [-vvv] [-T] git@github.com : test connection [v=verbose, vvv=very verbose, T=?]  
  
GIT-GITHUB linking :  
generate ssh key  
save it in github->settings (public key)  
copy github repository link (SSH link !)  
use it for git remote add  
add key to ssh-agent:  
eval “$(ssh-agent -s)”		//start ssh-agent  
ssh-add <path_to_key>	//add private key  
(ssh-add -l)			//check: saved keys  
ERROR (public key): see terminal/linux  
  
.md (markdown) file  
// es. README.md (showed in GitHub main page)  
for plain text (txt)  
#title : make a (bold) title/chapter/header  
## README.md  
*	[README.md](./README.md)  

##subheader  
newline : double space  
separator line : “\t-” (“    -”)  


