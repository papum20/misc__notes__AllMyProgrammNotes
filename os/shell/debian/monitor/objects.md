# OBJECTS

## snmp

MIB objects :
*	`UCD-SNMP` : `1.3.6.1.4.1.2021`
	*	`disk [partition] [minfree|minfree%]` : `9` 
	*	`load [max-1] [max-5] [max-15]` : `10` 
	*	`proc [proc_name] [maxnum] [minnum]` : `2`
*	`NET-EXTEND` : extension
	*	`NET-SNMP-EXTEND-MIN` : table
		*	a row for each value of directive `extend CMD` or `extend-sh CMD` in `snmpd.conf`
			*	can add as many as you want
			*	command can include arguments
			*	e.g.: `extend-sh sshd /usr/bin/sudo /usr/bin/ss -lntp | egrep '0\.0\.0\.0:22.*sshd` : name is `sshd` and command `sudo ss ...`
				*	note: use absolute paths
		*	columns :
			*	`nsExtendOutputFull` : a string; full command output ?
		*	e.g.: `snmpget ... NET-SNMP-EXTEND-MIB::nsExtendOutputFull.\"sshd\"` : 
			*	note: escape quotes, as they will be resolved by agent's snmpd shell