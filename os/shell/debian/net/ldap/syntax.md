# SYNTAX

## lidf

### by examples

`ou` `people.ldif` :
*	```
	dn: ou=People,dc=labammsis
	objectClass: organizationalunit
	ou: People
	description: system users
	```

user :
*	```
	dn: uid=dave,ou=People,dc=labammsis
	objectClass: top
	objectClass: posixAccount
	objectClass: shadowAccount
	objectClass: inetOrgPerson
	givenName: Davide
	cn: Davide
	sn: Berardi
	mail: davide.berardi@unibo.it
	uid: dave						# unique identifier
	uidNumber: 10000				# linux uid
	gidNumber: 10000				# main group gid
	homeDirectory: /home/dave
	loginShell: /bin/bash
	gecos:Davide "Dave" Berardi
	userPassword: {crypt}x			# {crypt}x says to not define here in plain text, but specify later
	```

group :
*	```
	dn: cn=dave,ou=Groups,dc=labammsis
	objectClass: top
	objectClass: posixGroup
	cn: dave
	gidNumber: 10000
	```

### set
*	`changetype` : type of modify
	*	`delete` :
	*	`modify` : 
*	e.g.: add :
	*	just no `changetype` line
*	e.g.: `chsh.ldif` : change shell of `dave`
	*	```ldif
		dn: uid=dave,ou=People,dc=labammsis
		changetype: modify
		replace: loginShell
		loginShell: /bin/sh
		```
*	e.g.: delete entry :
	*	```ldif
		dn: uid=dave,ou=People,dc=labammsis
		changetype: delete
		```
*	e.g.: delete attribute :
	*	```ldif
		dn: uid=dave,ou=People,dc=labammsis
		changetype: modify
		delete: loginShell
		```


### misc

` ` : a space can separate multiple entries in a single file  
