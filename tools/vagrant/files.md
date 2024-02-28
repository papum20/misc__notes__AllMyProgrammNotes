# FILES

## FILES
`/vagrant` : shared folder with main sys  
*	corresponds to folder where env installed (`Vagrantfile`)  

## Vagrantfile
Config file for a vm.  

### config
`config.*` :  

`vm.box` : box name
*	e.g.: `debian/bookworm64` : 

`vm.provider` : ??  
*	e.g.:
		```bash
		config.vm.provider "virtualbox" do |vb|
			vb.linked_clone = true
		end
		```
		: ??

`vm.disk` : ??  
*	e.g.: `config.vm.disk :disk, name: "backup", size: "1GB"` : ?? 


## BOXES
`hashicorp/bionic64` :   
`ubuntu/trusty32` :  