# OBJECTS

## Vagrantfile objects

```bash
# -*- mode: ruby -*-
# vi: set ft=ruby :
# (ruby-like syntax)
Vagrant.configure("2") do |config|
	# configs here
end
```

### config
`config.*` :  

`vm.box="BOX"` : box name
*	e.g.: `debian/bookworm64` : 

`vm.disk` : ??  
*	e.g.: `config.vm.disk :disk, name: "backup", size: "1GB"` : ?? 

`config.vm.network "private_network", ip: "192.168.33.10"` : ?  
`config.vm.network "public_network"` : ?  
`config.vm.network "forwarded_port", guest: 80, host: 8080` : ?  
`config.vm.synced_folder LOCAL_PATH REMOTE_PATH` : specify additional sync folder path  


#### provider
Config vm provider, and hw specs.  

```bash
config.vm.provider "virtualbox" do |vb| 
	# provider configs here
end
```

`vb.memory = BYTES_N` :  
`vb.cpus = CPUS_N` :  
`vb.linked_clone = true|false` : (dflt=`false`) if false, box is copied at creation, otherwise only a link  
*	obs: copy full os img

#### provision
Executed (only once) at first vagrant up (unless `vagrant up --provision` or `vagrant provision`).  

```bash
config.vm.provision "shell", inline: <<-SHELL
	# shell commands here
SHELL  
```

ansible :
*	```bash
	Vagrant.configure("2") do|config|
	#
	# Run Ansible from the Vagrant Host
	#
	   	config.vm.provision "ansible" do |ansible|
			ansible.playbook = "playbook.yml"
		end
	end
	```