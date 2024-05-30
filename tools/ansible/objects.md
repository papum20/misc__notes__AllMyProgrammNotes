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

`ansible.builtin.apt` :
*	`name: APT_PKG_NAME` : 
*	`state: present` : 
*	`update_cache: yes` : `apt update` before 

`ansible.builtin.copy:` : 
*	`src: str` : source path (on local)
*	`dest: str` : destination path (on managed node)
*	`group: str` : 
*	`mode: str` : octals
*	`owner: str` : 

`ansible.builtin.cron:` : like cron, add a job
*	`minute: "*/2"` :  
*	`weekday: "1-5"` :  
*	`month: "1-7,9-12"` :  
*	`job: "/usr/bin/copy.sh >/dev/null"` :  

`ansible.builtin.lineinfile:` : check/change line(s)
*	`line: str` : line to add after `regexp`
*	`path: str` : 
*	`regexp: ` : to match
	*	e.g.: for `present`/`absent`
*	`state: present|absent` : wether to add (if not present, otherwise just check) or remove
*	`validate: COMMAND` : exec command to validate, passing the file as parameter usable as `%s`
	*	e.g.: `validate: /usr/sbin/visudo -cf %s`

`ansible.builtin.service:` : 
*	`path: str` : 
*	`regexp: ` : to match
*	`replace` : line to replace `regexp` (only matched part)
	*	e.g.: replace final part of each line
		```yaml
		regexp: 'main$'
		replace: 'main contrib non-free-firmware$'
		```

`ansible.builtin.service:` : 
*   `name` : 
*   `state` : 

`ansible.builtin.systemd:` :  
*	`enabled: bool` : 
*	`name: rsyslog.service` :
*	`state: started|restarted|...` :  

`ansible.builtin.user:` : create user
*	`name: str` : user name 
*	`comment: str` :  
*	`expires: float` : user expiry, in epoch
*	`password: str` : hashed password (will be put in shadow as hash)
	*	so generate in one of many ways... `openssl passwd "PASSWORD"`

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
