# SYNTAX

## ssh

### misc

indentation : doesn't matter
`# comment` :  

### options

```
Host HOST_NAME
	COMMANDS
Match PATTERN
	COMMANDS
```

#### scopes
`Host HOST_NAME` : match host  
`Match PATTERN` :  
*	`Match User USERNAME` :  
*	`Match Port PORT` :  

#### commands

##### ssh_config
`ProxyCommand COMMAND` : when ssh command matches, executes shell command (similar to ssh tunnel)  
`StrictHostKeyChecking=yes|no` : if `no`, automatically adds host to `known_hosts`   

#### sshd_config
`ForceCommand COMMAND` : when encountered (i.e. when its block is matched) executes the shell command on ssh connection  