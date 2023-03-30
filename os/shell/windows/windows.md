# WINDOWS CMD  
  
net start/stop bits :  
  
net start wuauserv : start windows update  
net stop wuauserv: stop windows update  
  
  
  
ren file new_name : rename  
  
  
diskpart : disks partitions / format  
list disk  
format  
select disk <number>  
  
ping <ip> : send package and receive ack  
arp -a : arp table  
  
ENVIRONMENT VARIABLES :  
%name%  
echo %name%	: print env.var.’s value  
ipconfig : get system ip  
pwd : in which directory am I  
rename <old-file> <new-file> :  
set 			: show environment variables  
set varname=value	: create/set  
set varname=value;%name% : append/add variable  
setx varname “value”	: set permanently (“ ” if value contains spaces)  
shutdown <type> : shutdown (type: /s=shutdown, /r=restart)  
Stop-Process -Name <process> :  
