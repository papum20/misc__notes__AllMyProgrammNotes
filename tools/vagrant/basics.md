# BASICS

## Requirements
Needs vm provider (virtual box).  

## Vagrantfile

Uses ruby syntax.  

## Concepts

### Boxes
Pre-made VMs: vagrant uses these to fastly create a VM  

### Network
Vagrant by default performs port forwarding on `127.0.0.1:2222`.  
*	you can see it in vagrant up
*	or change 
*	with more vagrant machines, assigns automatically different, not to make conflicts
	*	e.g.: `2200`, `2201`...
