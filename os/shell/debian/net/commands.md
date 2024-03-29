# COMMANDS
// networks commands  
  
## IP - SYNTAX   
`::` : (IPv6) short for more than one zero  
*	e.g.: `:: = 0.0.0.0.0.0` :  
*	e.g.: `::1 = 0.0.0.0.0.1` :  
  
## NETWORK  
`ip` :   
`ip addr add [ipaddress/netmask] dev [devicename]` :  
*	assign address to interface devicename  
*	`ip a` : same

`ip addr del [ipaddress/netmask] dev [devicename]` :  
*	remove address assigned to interface devicename  

`ip route` : list routes  
*	`ip r` : same
*	`add` :  
*	`change` :  
*	`del` :  
*	`replace` :  

`ip route add [remotenet_ipaddress/netmask] via [nexthop_ipaddress]` :   
*	`add static route to remote network, updating routing table of a node`  
*	e.g. `add 192.168.0.0/16` : wildcard : anything matching mask  

`iptables [-t TABLE] {-A|-C|-D|-V} CHAIN RULE_SPECIFICATION` : ip tables manager  
*	`-t TABLE` : specify table  
	*	default tables: `nat`, `filter`, `docker`, others
*	`-A` : append rule(s) to end of chain  
*	`-D` : delete  
*	`-F, --flush [CHAIN]` : delete all rules in chain, or all chains if not speficifed  
*	`-R CHAIN RULENUM RULE` : replace rulenum with rule (numbered from 1)
*	`CHAIN`:
	*	`PREROUTING` : altering pkt as soon as comes in  
	*	`POSTROUTING` : altering packets as about to go out  
*	`RULE` :   
	*	`-d, --destination ADDR[/mask][,...]`  
	*	`-i, --in-interface NAME` : interface via which pkt was received (INPUT/PREROUTING)  
	*	`-j EXTENSION` : action to perform if matched rule  
		*	if not specified j or g, nothing is done
	*	`-o, --out-interface NAME` : interface via which pkt will be sent  
	(OUTPUT/POSTROUTING)  
	*	`-p PROT` : protocol to match 
		*	e.g.: `-p tcp` : 
	*	`-s, --source ADDRESS[/MASK][,...]`  
	*	`DNAT [--to-destination ADDR]` : (only for nat) change dest addr  
		*	e.g.: `iptables -t nat -A PREROUTING -p [protocol] -d [source_ip] --dport [source_port] -j DNAT --to-destination [destination_ip]:[destination_port]` : port forwarding (change destination NAT)
	*	`MASQUERADE` : (only for `nat`) forwarding, i.e. replace with own ip  
		*	e.g.: `iptables -t nat -A POSTROUTING -o [devicename] --source [sourcenet_ipadress/netmask] -j MASQUERADE` : masquerade (change source NAT)  
	*	`SNAT [--to-source ADDR]` : (nat) change src addr  

`netstat` : (deprecated, use ss, or other commands suggested in man)   
*	show active/inactive connections  
*	`-a` : all types  
*	`-i` : list network intefaces
	*	names:
		*	`eth*` : real net interface
		*	`ens*` : same as eth
		*	`veth*` : created by docker
		*	`br-*` : bridge
*	`-n, --numeric` : don’t resolve names, keep numbers  
*	`-p` : show pid, process  

`nmap` : network exploration, port scanning  
*	`nmap HOST` : scan host’s ports  
*	`-n` : no DNS resolution (could be very slow otherwise)/  
*	`-sT` : (default?) TCP connect scan;  
nmap asks underlying os to establish connection with target machine:port by issuing the connect system call  
*	`-sV` : (?) find out versions  
	*	note: `very slow, probably faster with -T4 (?)`  
* `-sU` : UDP scans; can be combined with TCP  
* `-P*` : select ping types  
*	`-Pn` : apply functions to all hosts, even when not up (until time limit)  
*	`-p* PORT-RANGES` : port ranges to scan  
*	-p-` : (default) 1:65535  
*	-p A-B,C-D,...` : ranges  
*	-p ,B` : default start=1 (if not specified)  
*	-p A,` : default end=65535 (if not specified)  
*	note: `0 is only scanned if specified`  
*	-p U:[RANGE],T:[RANGE]...` :  
*	specify ranges for each protocol (TCP, U=UDP, S=SCTP, P=IP)  

`ss` : show active/inactive connections  
*	`-a` : all types  
*	`-n, --numeric` : don’t resolve names, keep numbers  
*	`-p` : show pid, process  
*	`-t` : only tcp  
*	`-u` : only udp  
*	e.g. `ss -t -a` : all tcp  
  
## openssl COMMAND   
connection:  
`s_client -connect HOSTNAME:PORT` : connect and print ssl certificate  
`COMMAND(S) | s_client -connect HOSTNAME:PORT` :  
*	stdin is sent to server, response comes to stdout  
`-ign_eof` : (?) when says “HEARTBEATING“ or “Read R BLOCK”  
encryption:  
`enc -aes-256-cbc -in FILE.EXT -out FILE.bin` : encrypt  
`enc -aes-256-cbc -d -in FILE.bin -pass PASSWORD` : decrypt  
misc:  
`list-cypher-commands` : secret key algorithms  
`list-standard-commands` : -  
`version -a` : version  
  
`ping IP` : sends package and calculates rtt (round trip time) until stopped (ctrl+C);  
*	`then returns average rtt`  
*	`ping -c N` : number n of packages  

`scp FROM TO` : ssh copy  
*	e.g.: `nome.cognome@studio.unibo.it:~/directory/file` : remote file  
*	`from, to, for remote, in format: login_name@host:path`  
  
`telnet IP PORT` : establish connection with telnet protocol  
commands:  
GET http://IP/file HTTP/1.0 //get file  
Host: PORT //end connection  
return codes:  
`404` : file not found  
`200` : ok  
  
`traceroute IP` : sends package increasing ttl (time to live) each time,  
*	`to calculate routers path`  

`traceroute -m MAX_TTL` :   
`wget URL` : download url here  
*	`--cut-dirs=NUM` : parent directories levels to skip  
*	`-l NUM` : level of subdirectories (0=infinite)  
*	`-np` : no parent directories  
*	`-nH` : no hostname/host-directories (prefixed by hostname)  
*	`-r` : recursive	  
*	`-O NEW-NAME` : save as  
*	`-P DIR` : save in dir	  
*	`--reject html,tmp` : reject “index.html” files  

`who` : 	  
  
`ssh [PARAMS] HOST [COMMAND]` :   
*	`COMMAND` : if specfìified, exec command directly
*	`-i KEY` : (identity file) use private key  
*	`-J` : proxy jump  
*	`-l NAME` : login name  
	*	e.g.: ssh -l daniele.dugo@studio.unibo.it dalibor.cs.unibo.it  
*	`-X …` : enable X11, i.e. allow graphic applications  
  
`ssh-agent` :   
`eval “$(ssh-agent -s)”` : start ssh-agent  
  
`ssh-add PATH_TO_KEY` : add ssh key to ssh agent (when ssh-agent started, key private)  
`ssh-add -l` : list saved keys  
  
## WEB
`curl HOST` : transfer data (send request) from/to server  
*	`-X METHOD=GET` : select method  
*	`-d DATA` : data to transfer (i.e. body)  
*	`-i` : include headers in response
	*	note: with `OPTIONS` method, allowed methods are returned in `Allow` header
*	`-H HEADER` : header to send  
  
## WHERE KEYS ARE FOUND  
// when trying to connect to host with ssh, it reads config files  

/etc/ssh/ssh_config   
~.ssh/config  
*	ssh_config looks for keys in default names, written in it (id_rsa, …).  
*	in ~/.ssh/config, you can add personalized names, different from defaults, with the line  
*	IdentityFile ~/.ssh/your_key_name  

## README.md  
*	[README.md](./README.md)  

