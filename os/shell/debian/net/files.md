# FILES	

## dns

### dhcp

`/var/lib/dhcp/*.leases` : ips leased (as server) or got in lease (from server)  

### dnsmasq

`/etc/dnsmasq.conf` : 
*	configure dns server :
	```conf
	# listen as dns server on eth1
	interface=eth1
	# range of ips to assign to clients, with lease time
	dhcp-range=10.1.1.10,10.1.1.20,12h
	# disable default behaviour, by which client would use this server as default gateway
	# e.g. useful with VirtualBox, where we want the default gateway to be VirtualBox (e.g. 10.0.2.2) and not this dns server (10.1.1.254)
	dhcp-option=3                            
	#dhcp-option=3,10.1.1.254	# instead, set the default gateway
											
	dhcp-option=option:ntp-server,10.1.1.254
	dhcp-option=option:dns-server,10.1.1.254
	# give static route: tell client to reach 10.2.2.0/24 via 10.1.1.254
	dhcp-option=121,10.2.2.0/24,10.1.1.254
	```
*	configure with 2 interfaces (connecting to 2 different networks, each with its own dhcp range and routes) :
	```conf
	dhcp-range=interface:eth1,10.1.1.1,10.1.1.253,12h
	dhcp-range=interface:eth2,10.2.2.1,10.2.2.253,12h
	dhcp-option=3
	# option 6: dns servers addresses to tell to clients
	dhcp-option=6,10.1.1.254,10.2.2.254
	# option 121, then list of routes (net via gateway, net via gateway, ...)
	dhcp-option=121,10.1.1.0/24,10.2.2.254,10.2.2.0/24,10.1.1.254
	```
*	specific to host :
	```conf
	dhcp-range=...	# also neededs
	dhcp-host=00:11:22:33:44:55,10.1.1.1	# assign ip to host with mac
	dhcp-host=00:11:22:33:44:66,ignore	# dont assign anyting to this mac
	dhcp-hostfile=FILE	# a file containing entries (lines) with same format as dhcp-host
	```

### hosts

`/etc/hosts` :
*	associate ips with hostnames; when this host or any other using this as dsn server tries to resolve a hostname, it will looked here too :
	```conf
	1.2.3.4 hostname
	5.6.7.8 host2
	```
	

## kernel

### /etc/nsswitch.conf

entry :
*   a database can return a status
    *   if `success`, stop searching
    *   else, apply the specified `action`, or continue with next db if not specified
*   format : ```
    <entry> ::= <database> ":" [<source> [<criteria> ]]*
    <criteria> ::= "[" <criterion> + "]"
    <criterion> ::= <status> "= " <action>
    <status> ::= "success" | "notfound " | "unavail" | "tryagain"
    <action> ::= "return" | "continue"
    ```
*   e.g.: `hosts: ldap [NOTFOUND=return] dns files`

databases :
*   `files`
    *   source in `/etc/hosts`
        *   entry format : `<IP> <FQDN> [<ALIAS> ...]`
        *   e.g.: `8.8.8.8 dns.google.com gdns`
*   `dns` : 
    *   configured from `/etc/resolv.conf`
        *   configured not manually (will be overwritten)
        *   entry format : `<nameserver|...> <IP>`

### /etc/sysctl.conf

`net.ipv4.ip_forward=1` : enable ip forwarding  

obs: corresponds to file `/proc/sys/net/ipv4/ip_forward`  
*	each directive in the file corresponds to a file in `/proc/sys/`

obs: reload with `sysctl -p`  
*	`echo "1" > /proc/sys/net/ipv4/ip_forward` : do manually

## ifup

### /etc/network/intefaces

```conf
# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug eth0		# define interface eth0 to be brought up by hotplug
iface eth0 inet dhcp	# use dhcp for eth0

auto eth1						# define interface eth1 to be brought up at boot
iface eth1 inet static			# define interface eth1 as static, i.e. not dhcp but with static ip
    address 10.1.1.1			# set ip address for eth1 interface
    netmask 255.255.255.0		# set netmask for eth1 interface
    up /usr/sbin/ip route add 10.2.2.0/24 via 10.1.1.254	# add route to net 10.2.2.0/24 passing through another host 10.1.1.254 (which is accessible somehow from this host)
```

obs: reload with `systemctl restart networking.service`  

`etc/network/interfaces.d/` : also sourced any files in here
*   filenames must only contain `[A-Za-z0-9_-]`
*   sourced with `source` or `source-directory` directives

## ssh

where keys are searched :
*	when trying to connect to host with ssh, it reads config files  
	*	`/etc/ssh/ssh_config`   
		*	`ssh_config` looks for keys in default names, written in it (`id_rsa`, ...) 
	*	`~/.ssh/config`  
		*	`IdentityFile ~/.ssh/your_key_name` : add custom keys names

### ssh_config

`/etc/ssh/ssh_config` :  
`~/.ssh/config` :  

### sshd_config

`/etc/ssh/sshd_config` :  


