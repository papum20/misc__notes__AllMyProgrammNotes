# BASICS

## INSTALL

Sometimes (like in some docker containers) `apt` won't find stuff like `ss`: install `net-tools` :  
```bash
apt install net-tools
```

## linux

By default, linux doesn't forward packets between interfaces
*	for security...
*	so need to neable from `/etc/sysctl.conf` (see [files](files.md))

## tools

### ip

obs: `ip` directives only valid until restart  

### SSH

`ssh` : command to connect "with a secure shell" (from your machine)  
`sshd` : ssh demon - concerns received ssh connections (on your machine)  