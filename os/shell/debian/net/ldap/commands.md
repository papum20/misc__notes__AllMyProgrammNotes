# COMMANDS

`ldap* [OPTIONS] [FILTER]` : 
*	`-b BASE` : tree base for search
*	`-D DN` : **bind dn** - perform actions as this entity
	*	e.g.: `-D "cn=admin,dc=labammsis"` : 
*	`-H URI` : ldap server uri
*	`-L` : shorter output
	*	e.g.: remove comments
*	`-LL` :
*	`-LLL` :
*	`-x` : simple auth (disable advanced feature)
*	`-w password` : admin password, for db ?
*	`FILTER=(PREDICATE)`:
	*	`PREDICATE=(var=val)` : 
		*	e.g.: `cn=dave` 
	*	`PREDICATE=&(P1)(P2)` : and
	*	`PREDICATE=!(P1)` : not
	*	`PREDICATE=(var=*)` : any value
		*	e.g.: `!(var=*)` : not set

`ldapadd` : add entries  
*	`-f FILE.ldif` : from file
*	e.g.: `ldapadd -x -D "cn=admin,dc=labammsis" -w "gennaio.marzo" -H ldap:/// -f people.ldif`

`ldapmodify` : modify entry
*	e.g.: `ldapmodify -x -D cn=admin,dc=labammsis -w gennaio.marzo -f chsh.ldif`

`ldapsearch` : search ldap db
*	`-s SCOPE=sub` : scope of search
	*	`base` : only base
	*	`one` : only one level
	*	`sub` : all levels
*	e.g.: `ldapsearch -x -D "cn=admin,dc=labammsis" -w "gennaio.marzo" -H ldap://10.0.2.15/ -b "dc=labammsis" -s sub` : 

`ldappasswd [OPTIONS] USER` :  
*	`USER` : **dn** of user
*	`-s password` : set password
	*	if omitted, generated automatically
*	obs: need permissions, so admin can always, while a user can only change his own
