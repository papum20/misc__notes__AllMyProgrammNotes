# OBJECTS

## yml file

### start of file

`---` : start of file  
`hosts:` : hosts where to run  
*	`all`

`become: bool` : become root to exec all tasks  
`become_user: string` : become user  
*	requires `become: true`
*	if user non-privileged, install `apt install acl`
	*	ref: https://stackoverflow.com/a/56379678/20607105

`tasks:` : list of tasks  

### other

```ansible
production                # inventory file for production servers
staging                   # inventory file for staging environment

group_vars/
   group1                 # here we assign variables to particular groups
   group2                 # ""
host_vars/
   hostname1              # if systems need specific variables, put them here
   hostname2              # ""

library/                  # if any custom modules, put them here (optional)
module_utils/             # if any custom module_utils to support modules, put them here (optional)
filter_plugins/           # if any custom filter plugins, put them here (optional)

site.yml                  # master playbook
webservers.yml            # playbook for webserver tier
dbservers.yml             # playbook for dbserver tier

roles/
    common/               # this hierarchy represents a "role"
        tasks/            #
            main.yml      #  <-- tasks file can include smaller files if warranted
        handlers/         #
            main.yml      #  <-- handlers file
        templates/        #  <-- files for use with the template resource
            ntp.conf.j2   #  <------- templates end in .j2
        files/            #
            bar.txt       #  <-- files for use with the copy resource
            foo.sh        #  <-- script files for use with the script resource
        vars/             #
            main.yml      #  <-- variables associated with this role
        defaults/         #
            main.yml      #  <-- default lower priority variables for this role
        meta/             #
            main.yml      #  <-- role dependencies
        library/          # roles can also include custom modules
        module_utils/     # roles can also include custom module_utils
        lookup_plugins/   # or other types of plugins, like lookup in this case

    webtier/              # same kind of structure as "common" was above, done for the webtier role
    monitoring/           # ""
    fooapp/               # ""
```

## task

`name: str` : task name  
`become: bool` : become root to exec task  
`MODULE:` : use a module  

## modules

### ansible.builtin

*	```yml
	ansible.builtin.apt:
	 # `[PKG1, PKG2]` : list of packages
	  name: APT_PKG_NAME 
	  state: present
	 #  `apt update` before
	  update_cache: yes 
	```
*	```yml
	ansible.builtin.copy: 
	 # source path (on local)
	  src: 
	 # destination path (on managed node)
	  dest: 
	  group: 
	 # octals
	  mode: 
	  owner: 
	```
*	```yml
	# like cron, add a job
	ansible.builtin.cron:
	  name : 
	  minute: "*/2"
	  weekday: "1-5"
	  month: "1-7,9-12"
	  # whose crontab to add to (default: current)
	  user : 
	  job: "/usr/bin/copy.sh >/dev/null" 
	```
*	```yml
	ansible.builtin.file:
		path: /etc/foo.conf
		# touch: create if not present, otherwise update other params
		state: touch
		owner: root
	    group: root
		# also: `u=rw,g=r,o=r`
    	mode: '1777'
	```
*	```yml
	# check/change line(s)
	ansible.builtin.lineinfile:
	 # bool, if file not exists, crate
	  create: 
	 # line to add after `regexp`
	  line: 
	  path: 
	 # to match, e.g. for `present`/`absent`
	  regexp: 
	 # wether to add (if not present, otherwise just check) or remove
	 # present|absent
	  state: present
	 #  exec command to validate, passing the file as parameter usable as `%s`
	  validate: /usr/sbin/visudo -cf %s
	 # line to replace `regexp` (only matched part)
	  replace: 
	```
*	```yml
	ansible.builtin.service: 
	  name: 
	  state: 
	```
*	```yml
	ansible.builtin.systemd:  
	  enabled: 
	  name: rsyslog.service
	 # started|restarted|...
	  state: 
	```
*	```yml
	ansible.builtin.user:` : create user
	  name: USERNAME 
	  comment:  
	 #  user expiry, in epoch (float)
	  expires: 
	 # hashed password (will be put in shadow as hash)
	 # so generate in one of many ways... `openssl passwd "PASSWORD"`
	  password: 
	```

### ansible.posix

`ansible.posix.authorized_key:` : add authorized key (ssh)
*	`user: str` : 
*	`state: present` : 
*	`key: str` : 
	*	e.g.: `key: "{{ lookup('file', '~/.ssh/id_rsa_ansible.pub') }}"` : from file

`ansible.posix.sysctl` :
*	e.g.:
	```yml
	-	ansible.posix.sysctl:
			name: net.ipv4.ip_forward
			value: '1'
			sysctl_set: true
			state: present
			reload: true
	```

### community.general

`community.general.interfaces_file:` : manage interfaces file
*   `inface: str` : interface name
*   netmask :
    *   ```
        option: 'netmask'
        value: '255.255.255.0'
        ```
*   `backup: yes` : 
*   `state: present|absent` :
