# COMMANDS

`conda COMMAND` :  

## Envs
`activate ENV` :   
`clean -[ptcl]` : remove unused pkgs and caches
*	`-c` : tempfiles
*	`-l` : logfiles
*	`-p` : packages
*	`-t` : tarballs
*	`--dry-run` : only output

`create -n ENV` : specify name  
`create -n ENV Python=x.x` : specify python version  
*	`--file FILE` : create from requirements  

`deactivate` : deactivate current active  
`env list` : list of envs  
`env remove -n ENV` : remove env named env  
`env update -f FILE` : (YAML file .yml)  
`info` : info on conda  
`install PKG` : install for current env  
*	`--file FILE` : install from requirements
*	e.g.: `conda install --file requirements.txt` :  

`list` : list of installed packages  
*	`-e, --export` : list as exportable requirements
	*	e.g.: `conda list -e > requirements.txt` :  

`remove PKG` :  
*	`-d, --dry-run` : only display, don't remove
	*	e.g.: to see if `PKG` is needed by any

`update conda` : update conda  

## Config
`config --append PROP VAL` : add `VAL` to `PROP` list
*	e.g.: `config --append channels conda-forge` :  

`config --set PROP VAL` :  
`config --show PROP` : `PROP` value  
*	e.g.: `config --show channels` : show channels used  

## README.md  
*	[README.md](./README.md)  

