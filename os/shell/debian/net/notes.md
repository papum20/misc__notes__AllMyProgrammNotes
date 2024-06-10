# NOTES

## Configs

enable ip forwarding :
*	```bash
	# in /etc/sysctl.conf, uncomment
	# net.ipv4.ip_forward=1

	# apply
	sysctl -p
	```

## Errors

sometimes to change something on a given interface `ETH`, with either `networking.service` or `ifup`, first delete the previous config :
*	```bash
	ifup address flush dev ETH
	```
*	or :
	```bash
	ifdown ETH && ifup ETH
	```
