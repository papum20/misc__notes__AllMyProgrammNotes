# LINUX FILES  
  
  
  
FOLDERS:  
/dev/null : false path to write: writes nowhere  
/dev/urandom : when read file, gives random number  
/etc/default/grub : grub config  
		fix disappeared other os dual boot entry: uncomment GRUB_DISABLE_OS_PROBER=false  
/etc/groups : groups info  
/etc/hostname :   
/etc/os-release : contains linux version/distro  
/etc/passwd : users passwords / login info  
/etc/ssh/<config_files> :   
/mnt : empty file, where to mount a device  
/proc/ : virtual folder for processes / also contains system info  
	/proc/	<proc_id> : process info (viewed as files)  
	/proc/ <proc_id>/status : info  
		$$ : shell (corrente)  
	/proc/	cpuinfo :   
		meminfo :   
/usr/include/x86_64-linux-gnu/asm/unistd_64.h : syscalls numbers  
~/.bashrc : executed at startup for user  
~/.profile : executed at login for user  
  
ENVIRONMENT VARIABLES :  
LD_LIBRARY_PRELOAD : change linked library  
	(only for current process)  
	e.g. LD_…_PRELOAD=./lib.so ./file.c  
