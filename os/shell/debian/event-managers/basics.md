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

### rsyslogd
For logging.  
Can put conf files in its folder, then `systemctl restart rsyslog`.  

## sysVinit

## upstart

