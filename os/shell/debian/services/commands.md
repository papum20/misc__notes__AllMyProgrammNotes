# COMMANDS


## at

`at [-V] [-q QUEUE] [-f FILE] [-mldbv] TIME` : plan a command at `TIME`  
*	if no file, use stdin
*	e.g.: `echo A | at 08:00`
*	e.g.: `at now +2 minutes`


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
*	`status`
	*	output: 
		```
		~$ sudo systemctl status networking.service
		networking.service - Raise network interfaces
		Loaded: loaded (/lib/systemd/system/networking.service; enabled; preset: enabled)
		# path to service file, enabled at boot, enabled by default (as specified by service file)
    	Active: active (exited) since Tue 2024-04-16 15:02:31 CEST; 31min ago
       	Docs: man:interfaces(5)
   		Main PID: 856 (code=exited, status=0/SUCCESS)
        CPU: 39ms
		```

## sysVinit

**runlevel** : (basic concept)  

## udev
Automatically create special file on new dev connection.  
Now part of `systemd`.  

## upstart
