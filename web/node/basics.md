# BASICS

## INSTALL

Upgrade:
1.	`n VERSION` : installed via npm
	*	`VERSION=latest|lts|N` : choose version
	```bash
	npm install --global n && \
    	n $VERSION
	```
2.	`nvm` : download the script
	*	note: the following commands are suggested by nvm, to see the new version without needing to reopen terminal
	```bash
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash && \
		export NVM_DIR="$HOME/.nvm" && \
		[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" && \
		[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" && \
		nvm install node
	```
