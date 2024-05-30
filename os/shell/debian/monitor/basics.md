# BASICS

## snmp

`snmpcmd` : man page  

On the **agent**, `snmpd` runs as a standard user, so remember it when executing privileged commands (see[notes.md](notes.md)).  

### install

note: require append `contrib non-free` to `/etc/apt/sources.list` lines  

**manager** : who collects data
*	```bash
	sudo apt install snmp
	sudo apt install snmp-mib-downloader
	sudo sed -i `s/^#mibs :/#mibs :/g` /etc/snmp/snmp.conf	# as comments say, uncomment mibs to load them
	```

**agent** : who provides data
*	```bash
	sudo apt install snmpd	# daemon
	```

