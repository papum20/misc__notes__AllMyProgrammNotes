# EXAMPLES

## net

setup interface, copying local file `interfaces` :
*	```
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
*	```
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

