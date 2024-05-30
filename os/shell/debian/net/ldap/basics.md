# BASICS


Ldap uses a hierarchical tree :
*	`dn` : **domanin name** - unique identifier for each entry, composed of the identifiers of all nodes to reach it from root
	*	e.g.: `dn: cn=John Doe,dc=example,dc=com`
*	`dc` : **domain component** - component of domain
	*	e.g.: `dc=google,dc=com` for `google.com`
*	`ou` : **organizational unit** - group of entries
*	`cn` : **common name** - name of single entity
