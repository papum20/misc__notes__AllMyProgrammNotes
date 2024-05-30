# FILES


## cron

`/var/spool/cron/crontab/USER` : **USER**'s **crontable**  
`/etc/crontab` : sys tasks  
*	usually calls all `cron.{hourly|daily|weekly|monthly}`

`/etc/cron.{hourly|daily|weekly|monthly}` : sys tasks, divided by common planning periods  

## systemd

`/etc/rsyslog.d/*` : `rsyslog` files  

service file :
*	e.g.: `/lib/systemd/system/networking.service :
	```
	[Unit]
	Description=Raise network interfaces	# description
	Documentation=man:interfaces(5)	# man page
	DefaultDependencies=no
	Requires=	# dependencies (service doesn't start w/out)
	Wants=network.target ifupdown-pre.service	# dependencies (but can start w/out)
	After=local-fs.target network-pre.target apparmor.service systemd-sysctl.service systemd-modules-load.service ifupdown-pre.service
	Before=network.target shutdown.target network-online.target
	Conflicts=shutdown.target

	[Install]
	WantedBy=multi-user.target	# add this as dependency to others
	WantedBy=network-online.target

	[Service]
	Type=oneshot
	EnvironmentFile=-/etc/default/networking
	ExecStart=/sbin/ifup -a --read-environment	# command run at systemctl start SERVICE
	ExecStart=-/bin/sh -c 'if [ -f /run/network/restart-hotplug ]; then /sbin/ifup -a --read-environment --allow=hotplug; fi'
	ExecStop=/sbin/ifdown -a --read-environment --exclude=lo	# command run at systemctl stop SERVICE
	ExecStopPost=/usr/bin/touch /run/network/restart-hotplug
	RemainAfterExit=true
	TimeoutStartSec=5min
	```

## sysVinit

## upstart
