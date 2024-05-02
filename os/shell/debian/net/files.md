# FILES	

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

```
# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug eth0		# define interface eth0 to be brought up by hotplug
iface eth0 inet dhcp

auto eth1						# define interface eth1 to be brought up at boot
iface eth1 inet static			# define interface eth1 as static, i.e. not dhcp
    address 10.1.1.1			# set ip address for eth1 interface
    netmask 255.255.255.0		# set netmask for eth1 interface
    up /usr/sbin/ip route add 10.2.2.0/24 via 10.1.1.254	# add route to
```

obs: reload with `systemctl restart networking.service`  

`etc/network/interfaces.d/` : also sourced any files in here
*   filenames must only contain `[A-Za-z0-9_-]`
*   sourced with `source` or `source-directory` directives

## ssh

### ssh_config

`/etc/ssh/ssh_config` :  
`~/.ssh/config` :  

## sshd_config

`/etc/ssh/sshd_config` :  


## WHERE KEYS ARE FOUND  
// when trying to connect to host with ssh, it reads config files  

/etc/ssh/ssh_config   
~.ssh/config  
*	ssh_config looks for keys in default names, written in it (id_rsa, …).  
*	in ~/.ssh/config, you can add personalized names, different from defaults, with the line  
*	IdentityFile ~/.ssh/your_key_name  

