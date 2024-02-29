# LINUX SHELL  
## README.md  
*	[README.md](./README.md)  

## (verified on Debian)


## FILE SYSTEM   
### cd
`cd` :  
*	`-L` : follow symbolic link  

`cd -` : to previous directory  
`cd` : = `cd /home/USER/`  

### find
`find DIR` : list (recursively) elements in dir  
*	```-maxdepth LEVELS``` : 	  
*	```-mindepth LEVELS``` :   

`find DIR -name FILENAME` : find files (recursively) in dir matching basename with file_name  
`find DIR -path PATTERN` : find files with path matching pattern  

---  
`ln FILE` : create (hard) link to file (in current directory, with same name)  
*	`note: `file must be precise path, not relative  ``
*	``-s`` : symbolic link  
*	``ln [FILE] [LINK]`` : links link to file  
*	``-f`` : (force) used to overwrite existing link to point another file  
*	``// symbolic link: false file, reference  ``
*	``// hard link:  ``

`ls [PATH=.]` : list of files  
*	`-1` : vertical  
*	`-d` : list dirs, not contents
	*	e.g.: `ls -d ${PWD}/*` : list abs paths in `.`
*	`-i` : show inodes  
*	`-l` : long  
*	`-o` : -l without groups  
*	output format: `crwxrwxrwx+` : (access rights, special modes)  
	*	c=type flag; rwx= for User, Groups, Others; +=special character(s)  
	*	`special bits` : SUID, GUID, sticky bit (no effect on executables)  
	*	`suid` : (s at user x) when executing, take owner's rights  
	*	`sgid` : (s at group x) take owner’s group  
	*	`sticky bit` : (t at other x) only owner can delete files in folder (if folder has write right for others)  

`mkdir DIR` :  
*	``-p`` : ignore errors; also make parent dirs if needed  

`mv SRC DST` :  
`pushd` : cd, allows to go back  
`pwd` : current path  
`rm` : remove  
*	`-r` : recursive  
*	`-f` : force (also rm --force)   
*	`rm A{B1,B2}` : match `AB1`, `AB2`


`(oss)` : if file being used: removed name, then file after execution ended  
`(oss)` : file completely deleted after each copy of its name deleted  
`rmdir ` :  
  
## FILES   
`basename FILE` : print without path  
`basename FILE SUFFIX` : print without path and trailing SUFFIX  
*	e.g.: remove extension

`cp SRC DST` : copy  
`cp SRCS.. DST` : copy all files in dir  
`dd if=FROM_PATH of=TO_PATH` : Copy a file, converting and formatting according to the operands  
`diff FILE1 FILE2` : difference  
*	`q` : files summary
*	`u` : unified - nicer, like git diff (with context, +,-)

`file FILE` : info about file  
`gdb` : (disassemble)  
`ldd` : print shared object dependencies  
`nm FILE` : symbol table  
*	note: U=not found  

`objdump` : info on object file  
*	`-D` : (disassembler)  
*	`-h` : section-headers; elf setions  

`readelf` : info on ELF file  
`readlink FILE` : output linked file  
`touch FILE` : create file  
  
## FILES - ENCODED   
`base64` : base64 encode/decode and print  
*	``-d`` : decode  
`bzip2` :   
*	``-d`` : decompress  

`gzip` :   
*	``-d`` : decompress  

`l` : list of files  
`od FILE` : (octal dump) to octal (from char)  
`od -cx FILE` : (hexadecimal) to hexadecimal  
`tar` : tar files  
*	`-c` : compress  
*	`-f` : use file ARCHIVE (?)  
*	`-t` : list archive content  
*	`-v` : verbose  
*	`-x` : extract  
*	`-z` : gzip  
*	e.g.: ``tar czvf TAR DIR`` : compress DIR to TAR  
*	e.g.: ``tar tvzf TAR`` : list contents  
*	e.g.: ``tar xzvf TAR`` : extracts tar gz file  
*	e.g.: ``tar xzvf TAR -C DESTINATION`` : to destination folder  
*	e.g.: ``tar xzvf TAR --directory DESTINATION`` : /  

`tree` : file system tree (for current directory)  
`xxd [infile]` : make hexdump  
*	``-r`` : reverse (from hexdump to file)  
  
## FILE SYSTEM (SYSTEM CALL)   

`chmod [augo] [+-=] [rwxs] file` :   
*	`[all, user, group, others] [add, remove, set right]  `
*	e.g.: `chmod +x FILE` : add execute for all  
*	e.g.: `chmod g+s FILE` : add setgid  

`chmod o-r FILE` : o=others, -=remove rr=read -> remove read from others  
`getfacl FILE` : get acl permissions
`setfacl FILE` : set acl permissions
*	`-m ACL_SPEC` : modify with new permissions
	*	`ACL_SPEC={u|g|o}{GROUP|USER}:[rwx]` : set rwx permissions for users/groups/others
	*	e.g.: `setfacl -m g:docker:rwx file` : add rwx for group docker to file
*	`-R` : recursive

`umask OCTALS` : set default permission for newly created files  
*	``(with parameters in decimals/base 8 working as in chmod)  ``
*	e.g.: ``umask 0777`` : all permissions  
  
## I/O STREAMS   

`cat [file_name]` : (catenate) redirects stream i/o  
`cat FILE` : prints file  
`cat FILE1 FILE2 ...` : prints files one after each other  
`cat > FILE` : “cout”  
`cat  FILE` : “cin”  
`cat  FILE1  FILE2` :  
`cut [(-c|-f)LIST] [-dDELIM] [INPUT]` : cut sections  
*	`-cLIST` : select only these characters  
*	`-dDELIM` : set delim char  
*	`-fLIST` : select only these fields (separated by DELIM, like split())  
*	`-s` : exclude lines not containing char  
*	`LIST=N|N-|N-M|-M` : ranges of chars/fields  

`echo` :   
*	``-n`` : no trailing new line  

`edit [file_name]` : text editor  
`head INPUT` : print first 10 lines  
*	``head -N INPUT`` : print first n lines  

`grep PATTERN [FILE]` : search pattern in file  
*	`-A|B NUM` : include NUM lines after/before  
*	`-E` : enable extended regex
	*	e.g: enable `|`
*	`-n` : also print in which line was found
*	`-r` : recursive - used for searching directory instead of single file
*	`-v PATTERN` : “inverse”, i.e. excludes pattern  

`sed '/START/[,/END/]CMD' [FILE]` : "stream editor for filtering and transforming text"  
*	filter file text from regex `START` (to `END`) and apply command `CMD`  
*	`/REGEX/` : REGEX between slashes
*	`-E` : extended (modern) regex
*	default: old regex
*	`-n` : don't print all
*	commands:
	*	`p` : print (like grep)  
	*	`s/REGEX/REPLACEMENT/` : replace `REGEX`
		*	e.g.: `sed 's#.*/##; s#[.][^.]*$##'` : remove extension and path
	*	`$#` : matched part in REGEX, to refer in REPALCEMENT

`sort TEXT` : (default) sort lines  
*	``sort -r`` : reverse order  

`strings` : print the sequences of printable characters in files  
`tail INPUT` : print last 10 lines  
`tail -N INPUT` : print last n lines  
`-f` : follow; append elements as file grows  
`es.: head -n1 INPUT | tail -n2` : print from n1-n2+1 to n1  
`tee` : “redirect from input to output”  
`tr SET1 [SET2]` : replace SET1 occurrences in input with SET2  
*	``tr -d SET1`` : delete SET1 occurrences  
*	``CHAR1-CHAR2`` : all chars from CHAR1 to CHAR2  
*	``[:alpha:]`` : all letters (A-Za-z)  
*	e.g.: ``tr [:alpha:] N-ZA-Mn-za-m`` : shift letters by 13 positions  

`uniq` : (default) merge repeated lines  
*	``-d`` : only print duplicate lines  
*	``-u`` : only print unique lines  

`vi [file_name]` : (edit)  
`wc INPUT` : count things (bytes, words…)  
*	``wc -l INPUT`` : count lines in input  
  
## MEMORY   

`df` : drives mounted/disk usage  
*	``df -h`` : (human-readable)  

`sudo fdisk` : show/edit disk partitions  
*	`-l` : list

`sudo fdisk DISK` : edit disk partition, with fdisk gui  

`sudo mkfs DISK` : mk fs  
`sudo mkfs.ext4` :  
  
## PROCESSES   

`disown [JOBSPEC|PID]` : unlink process from terminal
*	default: `JOBSPEC` : current job

`ltrace FILE` : intercept and record dynamic library calls;  
*	``(relies on ptrace syscall)  ``
*	``-e FILTER`` : filter library calls  
*	``FILTER`` : e.g.: +F1-F2+@PATH1-@PATH.so* :  
+ filters in, - filter out, @ indicates library pattern, without is symbol pattern (function), wildcard allowed  

`nohup COMMAND` : make command no hang up when closing terminal  
*	e.g.: `nohup COMMAND &` :  

`ps` : processes  
*	`-a` : all associated with a terminal
*	`-A|-e` : all
*	`-u` : show owner user

`strace PROCESS` : list of system call made;  
*	``(relies on ptrace syscall)  ``
*	``-f`` : follow forks  
  
## SIGNAL   

`kill` : sends (kill) signal  
`kill -N PID` : send signal number n  
`kill` : = kill -9  
`kill -9 PROC` : (force) interrupt  
`kill -15 PROC` : (ask interrupt)  
  
## USERS   

`addgroup [[-g GID]|[USER]] GROUP` : add `USER` to `GROUP` or create `GROUP`
*	`-g GID` : assign gid to group

`adduser user` : create new user (interactive)  
`adduser user group` : add user to group  
`chgrp [GROUP] file` : change file’s group  
`chown [USER[:GROUP]] file` : change file’s owner/group  
*	`-R` : recursive

`chroot` : change root  
*	e.g.: ``chroot /mnt/PARTITION/ /bin/bash`` : start a chrooted bash  

`groupadd GROUP` : create group
*	`-g GID` : assing gid

`id USER` : user and groups id
`passwd [user]` : change user’s password (own if no arg); (executed as root)  
`su [USER]` : switch user  
`sudo COMMAND` : exec as super-user  
*	`-i` : launch interactive shell as sudo
*	`-l` : list commands executable as current user running sudo

`sudo useradd user` : create new user (not interactive)  
`usermod` : modify user  
*	`-a` : add to groups (to use with `-G`)
*	`-G GROUPS...` : specify list of groups
*	e.g.: `usermod -aG GROUP USER` : add `USER` to `GROUP`

`who` : list connected hosts/users  
  
## MISC  

`alias` : display alias  
*	``alias [...]`` : define alias  

`clear` : clears terminal and starts from first row  
`history` : history of commands given  
`man [SECTION] COMMAND` : manual  
*	`-k KEYWORD` :  
*	e.g.: `man man` : manual for manual  
*	e.g.: `man ascii` :   
*	e.g.: `man 2 SYSTEM_CALL` :   
	*	e.g.: `man 2 write` : write()  

`md5sum [FILE]` : md5 hash of `FILE`
*	e.g.: `echo -n STRING | md5sum` : hash of string (remove `\n` with `-n`)  

`reset` : reset terminal  
`timedatectl` : time for pc/os/hw…  
`xargs` : build and execute command lines from standard input  
*	``-L max-lines`` :   
*	``-l[max-lines]`` : like -L  
*	``-n max-args`` : use at most max-args arguments per command line  
+	`-I REPLACE-STR` : replace occurrences of `REPLACE-STR` in command with argument received (implies `-L 1`)

`yes` : prints y forever  
  
## DISK:  
`truncate …` : “create an empty file with specified size”  
  
## INFO:
`df` : info on storage  
*	``df -h`` : human readable (for instance, converts bytes to biggest possible measure)  
*	``df -BM`` : in MB  

`du [PATH=.]` : disk usage  
*	``-a, --all`` : (recursive) all files  
*	``-B, --block-size`` : size
*	e.g.: `-BM mega`  
*	``-b`` : SIZE = 1byte  
*	``-h`` : human-readable  
*	``-s`` : summarize  

`inxi -Fxxxrz` : info, including gpu driver, … (under graphics)  
`lsblk` : show (storage) blocks  
*	``lsblk -a`` : all blocks  

`lscpu` : cpu info (from /proc/cpuinfo)  
`lsmod` : loaded modules (from /proc/modules/)  
`lspci -kd` ::300 : gpu info (including driver if available)  
`lsusb` : devices  
`top` : processes / resources used  
  
## apt  
`apt autoremove` : remove unnecessary packages  
`apt search APPLICATION_NAME` :  
`apt show ` :   
*	``-a`` : all entries  

`apt update` : check updatable packages  
`apt upgrade` : update updatable packages  

## dpkg

## apt
`update-grub` : update grub  
*	e.g.: boot options  
