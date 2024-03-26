# COMMANDS


## at

`at [-V] [-q QUEUE] [-f FILE] [-mldbv] TIME` : plan a command at `TIME`  
*	if no file, use stdin
*	e.g.: `echo A | at 08:00`

`atq [-V] [-q QUEUE] [-v]` : list jobs waiting in queue  
`atrm [-V] JOB [JOB...]` : remove planned from queue  
*	you can see job id from `atq`

`batch [-V] [-q queue] [-f file] [-mv] [TIME]` : ?  

## cron

`crontab [-el] [-u USERNAME] [NEW_TAB]` :   
*	`NEW_TAB` : replace current table with new
*	`-e` : edit
*	`-l` : list (show table)


## systemd

`systemctl {start|stop|status|restart|reload} SERVICE` :  
*	`-H [HOSTNAME]` : first connect with ssh

**service** :
*	**reload** : if such services defines and specifed a way to reload, `systemd reload SERVICE` uses that
	*	e.g.: `SERVICE` reloads on `SIGUSR1`

**target** : a goal, for which the specified processes must be executed (with success)
*	replaced **runlevel**s

## sysVinit

**runlevel** : (basic concept)  

## udev
Automatically create special file on new dev connection.  
Now part of `systemd`.  

## upstart
