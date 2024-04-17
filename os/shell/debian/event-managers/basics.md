# BASICS

Programs to manage processes :  
*	execution planners (periodic or not)
*	daemons (event managing)
*	sys init procedures


## cron
Execution planner.  
Checks which to exe every minute.  

**crontab** : each user has one  
*	`/var/spool/cron`
/etc/crontab

## systemd
Big single program to replace many others.  

**service** :
*	**reload** : if such services defined and specifed a way to reload, `systemd reload SERVICE` uses that
	*	e.g.: `SERVICE` reloads on `SIGUSR1`

**target** : a goal, for which the specified processes must be executed (with success)
*	replaced **runlevel**s


### rsyslogd
For logging.  
Can put conf files in its folder, then `systemctl restart rsyslog`.  

## sysVinit

## upstart

