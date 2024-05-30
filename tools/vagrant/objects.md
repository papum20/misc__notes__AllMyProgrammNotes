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

`vm.disk` : manage disks for vm 
*	e.g.: config for virtualbox
*	e.g.: `config.vm.disk :disk, name: "backup", size: "1GB"` : additional (vm/virtualbox?) disks  

`config.vm.define "NAME"` : define machine with name `NAME`, and refer to it in the following block (ruby syntax)    
`config.vm.network "TYPE", ip: "192.168.33.10"` : config network, with static ip  
*	`TYPE=private_network` : private network, only host can access
*	`TYPE=public_network` : public network, accessible from outside
*	`auto_config=false` : disable auto config (dflt=`true`)
	*	don't use if specify static ip

`config.vm.network "forwarded_port", guest: 80, host: 8080` : ?  
`config.vm.synced_folder LOCAL_PATH REMOTE_PATH` : specify additional sync folder path  

#### machine

`machine.vm.hostname="HOSTNAME"` : set hostname for machine  
`machine.vm.network "private_network", virtualbox__intnet: "LAN1", auto_config: false` : add `machine` to network named `private_network` with `virtualbox__intnet` name `LAN1`    
*	e.g.: to connect more vms to same network, use same `LAN1`

`machine.vm.synced_folder ".", "/vagrant", disabled: true` : dont sync folder
*	obs: faster up


#### provider
Config vm provider, and hw specs.  

```bash
config.vm.provider "virtualbox" do |vb| 
	# provider configs here
end
```

`vb.memory = BYTES_N` :  
`vb.cpus = CPUS_N` :  
`vb.linked_clone = true|false` : (dflt=`false`) if false, box is copied at creation, otherwise only a link, and image only saves differences with original os image  
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