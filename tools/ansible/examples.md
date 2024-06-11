# EXAMPLES

## builtin

replace final part of each line :
*	```yml
	- name: Replace final part of each line
	  ansible.builtin.lineinfile:
	   - regexp: 'main$'
	   - replace: 'main contrib non-free-firmware$'
	   ...
	```

## ldap

add if not present :
*	```bash
	ldapsearch -x -b "ou=People,dc=labammsis" -s base > /dev/null || 
		ldapadd -x -H ldap:/// -D "cn=admin,dc=labammsis" -w "gennaio.marzo" -f /tmp/people.ldif
	```

## net

setup interface, copying local file `interfaces` :
*	```yml
	- name: Set eth3 netmask
	  community.general.interfaces_file:
	    iface: eth3
	    option: 'netmask'
	    value: '255.255.255.0'
	    backup: yes
	    state: present
	  when: ansible_facts['os_family'] in ['Debian']
	  notify: Restart Networking
	
	handlers:
	  - name: Restart Networking
	    ansible.builtin.service:
	       name: networking
	       state: restarted
	```  

Alternative with copy :
*	```yml
	- name: Copy a new network configuration "interfaces" file into place, after passing validation with ifup 
	ansible.builtin.copy:
		src: eth3
		dest: /etc/network/interfaces.d/eth3
		validate: /usr/sbin/ifup --no-act -i %s eth3
	notify: Restart Networking
	handlers:
	- name: Restart Networking
		ansible.builtin.service:
		name: networking
		state: restarted
	```

add privileged command :
*	```yml
	- name: Add privileged actions for snmp agent scripts
	ansible.builtin.copy:
		src: Debian-snmp
		dest: '/etc/sudoers.d/'
		owner: 'root'
		group: 'root'
		mode: '0440'
		validate: '/usr/sbin/visudo -csf %s'
	```


