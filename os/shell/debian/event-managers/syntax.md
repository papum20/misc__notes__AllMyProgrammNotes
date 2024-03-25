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
