# NOTES

## Configs

enable ip forwarding :
*	```bash
	# in /etc/sysctl.conf, uncomment
	# net.ipv4.ip_forward=1

	# apply
	sysctl -p
	```

enable authentication with ldap :
*	add ldap to `/etc/nsswitch.conf` :
	```conf
	passwd: files systemd ldap
	group: files systemd ldap
	shadow: files ldap
	# optionally: gshadow: files ldap
	```
	*	restart service
*	install `libnss-ldapd` and `libpam-ldapd` (services `nslcd` and `nscd`)
	*	`nslcd` also stores ip of ldap server, you can configure it at install (with `dpkg`) or in `/etc/nslcd.conf` (and then restart service)

## Errors

sometimes to change something on a given interface `ETH`, with either `networking.service` or `ifup`, first delete the previous config :
*	```bash
	ifup address flush dev ETH
	```
*	or :
	```bash
	ifdown ETH && ifup ETH
	```
