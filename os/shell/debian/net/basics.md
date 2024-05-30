# BASICS

## INSTALL

Sometimes (like in some docker containers) `apt` won't find stuff like `ss`: install `net-tools` :  
```bash
apt install net-tools
```

## concepts

### socket

Only 2 ends will see it, as pair local-remote
*	inverted pair between local and remote
*	intermediate routers won't
*	e.g.: with `ss`

## linux

By default, linux doesn't forward packets between interfaces
*	for security...
*	so need to neable from `/etc/sysctl.conf` (see [files](files.md))

### name-service
Association ip-hostname, handled by default by linux, with `C` dflt library, with **Name Service Switch** (NSS)  
*	associates an entry with one ore more databases where to lookup some information

### dns

**nss** : does it in `C` with **resolver**  

`dnsmasq` : 
*	`sudo apt install dnsmasq`
*	`/etc/dnsmasq.conf` : config file


## tools

### ip

obs: `ip` directives only valid until restart  

### SSH

`ssh` : command to connect "with a secure shell" (from your machine)  
`sshd` : ssh demon - concerns received ssh connections (on your machine)  