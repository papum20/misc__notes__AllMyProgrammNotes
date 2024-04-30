# COMMANDS

## vagrant
`vagrant COMMAND` :  

`box add BOX` : add a box  
`box list` :  
`box remove BOX` :  

`destroy` : remove resources created  

`global-status` : list envs  
`halt` : stop execution  
`init` : init Vagrant env;  
*	create `Vagrant` config file  

`init BOX` : init using BOX vm img  
`provision` : exec provision  
*	even if up

`status` :   
`ssh [VM_NAME]` : connect to started vagrant  
*	`VM_NAME` : name of vm to connect to
	*	required if more vms defined in `Vagrantfile`

`ssh-config` : generate ssh config to connect  
`up` : start vm (with `Vagrant` file)  
*	`--provision` : exec provision (even if not first `up`)