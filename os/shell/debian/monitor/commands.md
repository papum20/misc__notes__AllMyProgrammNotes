# COMMANDS

## snmp

`snmp*` :   
*	`-c COMMUNITY` : set community
	*	e.g.: those defined in `rocommunity`
*	`-O<OPTION>` : output options
	*	`n` : numeric (don't resolve names)
*	`-v VERSION` : snmp version
	*	e.g.: `-v 2`

`snmpget AGENT OID` : get value of `OID` on `AGENT` (ip) addr
*	e.g.: `snmpget -v 1 -c public 10.2.2.1 .1.3.6.1.1.2.1.1.6.0`

`snmpset AGENT OID TYPE VALUE` : set value of `OID` on `AGENT` (ip) addr to `VALUE` of `TYPE`
*	`TYPE` :
	*	`s` : string
*	obs: needs `-c` with a community with write permission
*	e.g.: `snmpset -v 1 -c public 10.2.2.1 .1.3.6.1.1.2.1.1.6.0 s "new value"`

`snmpwalk [OPTIONS] AGENT [OID]` : walk full sub-tree, from root `OID`  
*	obs: useful when don't know where to search
*	e.g.: `OID=1.` : root  

## logging

`logger -p local1.info <<< "INPUT"` : log `INPUT` to `local1.info` (`rsyslog` facility)   
*	`-n SERVER` : write to
*	`-p FACILITY.PRIORITY` : priority
