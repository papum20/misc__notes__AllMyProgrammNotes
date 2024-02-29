# LINUX FILES  
  
## FOLDERS  

### /dev
`/dev/null` : false path to write: writes nowhere  
`/dev/urandom` : when read file, gives random number  

### /etc
`/etc/default/grub` : grub config  
*	fix disappeared other os dual boot entry: uncomment GRUB_DISABLE_OS_PROBER=false` 

`/etc/fstab` : statuc fs info/boot  
*	`FS	MOUNT_POINT TYPE OPTS DUMP PASS` : format of an entry in the file
	*	e.g.: `/dev/sda1 /some_dir ext4 defaults 0 0` :  

`/etc/groups` : groups info  
`/etc/hostname` :   
`/etc/os-release` : contains linux version/distro  
`/etc/passwd` : users passwords / login info  
`/etc/ssh/CONFIG_FILES` :   
`/etc/sudoers` : sudo config file  
*	**Runas_Spec** : specify commands a user can execute as sudo
	*	e.g.: `alan    boulder = (root, bin : operator, system) /bin/ls` : user `alan` can run on host `boulder` only the command `/bin/ls`, as user `root` or `bin` (e.g. `sudo -u root /bin/ls`), and OPTIONALLY with group `operator` or `system` (e.g. `sudo -g operator /bin/ls`)
	*	e.g.: `alan    ALL = (root, bin : operator, system) ALL` : 

### /mnt
`/mnt` : empty file, where to mount a device  

### /proc
`/proc/` : virtual folder for processes / also contains system info  
`/proc/PROC_ID` : process info (viewed as files)  
`/proc/PROC_ID/status` : info  
*	`$$` : shell (corrente)  

`/proc/cpuinfo` :   
`/proc/meminfo` :   

### /usr
`/usr/include/x86_64-linux-gnu/asm/unistd_64.h` : syscalls numbers  
`/usr/share/dict/words` : list of english words  

### $HOME
`~/.bashrc` : executed at startup for user  
`~/.profile` : executed at login for user  
`~/.ssh/config` : config for ssh; see `man ssh_config`  
*	e.g.: `IdentityFile ~/.ssh/PRIVATE_RSA` : (line in config) use rsa key
  
## ENVIRONMENT VARIABLES   
`LD_LIBRARY_PRELOAD` : change linked library  
*	`(only for current process)`  
*	e.g. `LD_…_PRELOAD=./lib.so ./file.c`  

## README.md  
*	[README.md](./README.md)  

