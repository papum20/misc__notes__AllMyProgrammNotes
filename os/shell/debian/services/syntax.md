# SYNTAX

## cron

### crontab

`[USER]	MIN	HOUR	D.MONTH	MONTH	D.WEEK	COMMAND` : format
*	`USER` : only in sys crontab, specifies for whom to exec
*	`D.WEEK` : from `0` to `7`, where both are sunday
*	`COMMAND` executed any day of month/week, at time

`*` : any  
`N` : number  
`N-M/S` : from `N` to `M` with step `S`  
`N,M` : list  

## rsyslog

`/etc/rsyslog.conf` :  
`/etc/rsyslog.d/*.conf` :  
`/etc/rsyslog.d/*.off` : disabled  

entries format :
*	`FACILITY` : argument
	*	in `*, auth, authpriv, cron, daemon, ftp, kern, lpr, mail, news, syslog, user, uucp, local0..local7`
*	`PRIORITY` : 
	*	in descending order, `emerg, alert, crit, err, warning, notice, info, debug, *`
*	```conf
	# set messages from FACILITY, of priority PRIORITY or higher, to be logged to DESTINATION path
	FACILITY.PRIORITY	DESTINATION
	# only exact PRIORITY level
	FACILITY=PRIORITY	DESTINATION
	# multiple
	FACILITY1.PRIORITY1;FACILITY2.PRIORITY2	DESTINATION
	```
