# NOTES

## snmp


other (possible?) initial configuration steps **agent** : 
*	```bash
	sudo apt install snmpd	# daemon
	# configure socket (why?)
	sudo sed -i 's/agentAddress  udp:127.0.0.1:161/agentAddress  udp:161/' /etc/snmp/snmpd.conf

	# access control
	## ??
	sudo sed -i '$a view all included -1' /etc/snmp/snmpd.conf
	## create a ro and a rw community
	sudo sed -i 's/rocommunity public  default    -V all/rwcommunity supercom  default    -V all/' /etc/snmp/snmpd.conf
	## check there aren't any other rows for rocommunity or rwcommunity (?)

	# restart service
	sudo systemctl restart snmpd
	```

to execute privileged commands on the agent, should give the snmpd user correct permissions :
*	```bash
	sudo visudo
	# add the following line
	## Debian-snmp ALL=NOPASSWD:/usr/bin/ss -lntp
	### assuming that the used is Debian-snmp
	### notes on the sudoers file:
	#### NOPASSWD allows no password required
	#### can specify a single command to execute as root, so don't give full privileges; can also specify args
	```

