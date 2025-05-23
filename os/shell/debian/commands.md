# LINUX SHELL  
## README.md  
*	[README.md](./README.md)  

## (verified on Debian)


## FILE SYSTEM   

`find DIR` : list (recursively) elements in dir  
*	`-name FILENAME` : match basename with file_name  
*	`-path PATTERN` : match linux path pattern  
*	`-maxdepth LEVELS` : 	  
*	`-mindepth LEVELS` :   
*	`-exec COMMAND \;` : exec command for each file found
	*	`\;` : needed to end command
	*	`{}` : can be used and will be replaced with file name
*	numbers preceded by `-` : less than

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
*	output: `crwxrwxrwx+` : (access rights, special modes)  
	*	c=type flag; rwx= for User, Groups, Others; +=special character(s)  
	*	`special bits` : SUID, GUID, sticky bit (no effect on executables)  
	*	`suid` : (s at user x) when executing, take owner's rights  
	*	`sgid` : (s at group x) take owner’s group  
	*	`sticky bit` : (t at other x) only owner can delete files in folder (if folder has write right for others)  
	*	special bit uppercase, means `s` and no `x` (else `s+x`)
		*	e.g.: `rwS`

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
*	`cp SRCS.. DST` : copy all files in dir  
*	`cd -` : to previous directory  
*	`cd` : = `cd /home/USER/`  
*	`-L` : follow symbolic link  

`dd if=FROM_PATH of=TO_PATH` : Copy a file, byte by byte, from input file to out file, converting and formatting according to the operands  
*	`bs`  : block size - bytes to copy at a time
	*	e.g.: `bs=4k`
*	`count` : number of blocks to copy
*	use: copy large files; also keep track of where you are (e.g. if need to stop)

`diff FILE1 FILE2` : difference  
*	`q` : files summary
*	`u` : unified - nicer, like git diff (with context, +,-)

`file FILE` : info about file  
`gdb` : (disassemble)  
`ldd` : print shared object dependencies  
`mktemp` : create temporary file  
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
*	if no other complex options before these, can omit `-`
*	`-c` : compress  
*	`-f` : use file ARCHIVE (?)  
*	`--files-from FILE` : read list of files from `FILE`
*	`-t` : test - list archive content  
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

`cat [FILE...]` : (catenate) redirects stream input to output   
*	`FILE` : if specified, used as input (i.e. printed)  
*	`FILE1 FILE2 ...` : if specifed more, prints files one after each other  

`cut [(-c|-f)LIST] [-dDELIM] [INPUT]` : cut sections  
*	`-cLIST` : select only these characters  
*	`-dDELIM` : set delim char  
*	`-fLIST` : select only these fields (separated by DELIM, like split())  
*	`-s` : exclude lines not containing char  
*	`LIST=N|N-|N-M|-M` : ranges of chars/fields  

`echo` :   
*	`-n` : no trailing new line  

`edit [file_name]` : text editor  
`head INPUT` : print first 10 lines  
*	`-n N`, `-<N>` : print first `<N>` lines  
*	`-n -<N>` : all but the last `<N>`

`less` : view file  
*	commands : internal commands
	*	`<N>` : go `<N>` lines ahead
	*	`h` : help

`grep PATTERN [FILE]` : search pattern in file  
*	`-A|B NUM` : include NUM lines after/before  
*	`-E` : enable extended regex
	*	e.g: enable `|`
*	`-F` : match fixed string
*	`-I` : exclude binary matches
*	`-n` : also print in which line was found
*	`-o` : only print matched
*	`-r` : recursive - used for searching directory instead of single file
*	`-v PATTERN` : “inverse”, i.e. excludes pattern  
*	`-x` : match only whole lines  

`read VAR1 ...` : read from input, assign each element to a `VAR`, separated by `IFS`  
*	`-a ARRAY` : assign tokens to elements of `ARRAY`
*	`-p PROMPT` : print `PROMPT` before reading
*	`-u FD` : read from `FD`

`rev [FILE]` : reverse input lines  
*	note: doesn't support multi-byte chars and gives problems

`sed '/START/[,/END/]CMD' [FILE]` : "stream editor for filtering and transforming text"  
*	filter file text from regex `START` (to `END`) and apply command `CMD`  
*	`/REGEX/` : REGEX between slashes
*	`-E` : extended (modern) regex
*	default: old regex
*	`-i` : in place - edit file
*	`-n` : don't print all
*	commands:
	*	`p` : print (like grep)  
	*	`s/REGEX/REPLACEMENT/` : replace `REGEX`
		*	`s/REGEX/REPLACEMENT/g` : global - apply to all occurrences in line
		*	e.g.: `sed 's#.*/##; s#[.][^.]*$##'` : remove extension and path
	*	`$#` : matched part in REGEX, to refer in REPALCEMENT
*	e.g.: `sed -i '$a TEXT' FILE` : add line at end of file
*	e.g.: `sed -i 'Ni TEXT' FILE` : add line at line `N` (start from `1`)
*	e.g.: `sed -i '/PATTERN/a TEXT' FILE` : add line after each line matching `PATTERN`
*	note: `-Ei` and not `-iE`

`sort [FILE]` : sort input  
*	`-c` : check if sorted
*	`-k KEY` : ordering key
	*	if used multiple times, uses in order from left
*	`-m` : merge sorted files
*	`-r` : reverse order  
*	`-R` : random permutation of lines
*	`-tSEP` : set chars to separate fields (default spaces)
*	`-u` : `sort|uniq`
*	interpreptation and filters :
	*	`-b` : ignore leading spaces
	*	`-d` : only use alphanum and spaces
	*	`-f` : ignore case
	*	`-h` : 
	*	`-n` : interpret digits as number values

`strings` : print the sequences of printable characters in files  
`tail INPUT` : print last 10 lines  
*	`-N` : print last n lines  
*	`-f` : follow; append elements as file grows  
*	e.g.: `head -n1 INPUT | tail -n2` : print from n1-n2+1 to n1  

`tac` : redirects stream input to output, but starting from last input line
*	obs: reverse of cat

`tee` : “redirect from input to output”  
`tr SET1 [SET2]` : replace SET1 occurrences in input with SET2  
*	`-c` : take complement of first set
	*	e.g.: `tr -cd '[:print:]'` : remove non-printable characters
*	``tr -d SET1`` : delete SET1 occurrences  
*	``CHAR1-CHAR2`` : all chars from CHAR1 to CHAR2  
*	``[:alpha:]`` : all letters (A-Za-z)  
*	e.g.: ``tr [:alpha:] N-ZA-Mn-za-m`` : shift letters by 13 positions  

`uniq` : (default) merge adjacent repeated lines  
*	obs: `sort|uniq` : to remove all duplicates
*	`-c` : number of lines merged
*	`-d` : only print duplicate lines  
*	`-u` : only print unique lines  

`vi [file_name]` : (edit)  
`wc INPUT` : count things (bytes, words…)  
*	`-l` : count lines in input  
  
## MEMORY   

`df` : drives mounted/disk usage  
*	``df -h`` : (human-readable)  

`sudo e2fsck DEV` : fs check
`sudo fdisk` : show/edit disk partitions  
*	`-l` : list

`sudo fdisk DISK` : edit disk partition, with fdisk gui  

`sudo mkfs DISK` : mk fs  
`sudo mkfs.ext4` :  
`sudo mount -a` : mount all, according to fstab  
`sudo resize2fs DEV [SIZE]` : resize
*	e.g.: if expanding and there's empty space, can omit size and will fill

`testdisk` : find lost partitions, with cli  
  
## PROCESSES   

`bg [JOB_SPEC]` : bring job id to bg   

`disown [JOBSPEC|PID]` : unlink process from terminal (remove from hob table)  
*	default: `JOBSPEC` : current job

`fg [JOB_SPEC]` : job id to fg  

`ltrace FILE` : intercept and record dynamic library calls;  
*	``(relies on ptrace syscall)  ``
*	``-e FILTER`` : filter library calls  
*	``FILTER`` : e.g.: +F1-F2+@PATH1-@PATH.so* :  
+ filters in, - filter out, @ indicates library pattern, without is symbol pattern (function), wildcard allowed  

`nice COMMAND` : run command with _niceness_>0 (scheduling priority)   
*	default: 10
*	<10 : only used by root

`nohup COMMAND` : make command no hang up when closing terminal  
*	e.g.: `nohup COMMAND &` :  

`ps` : processes  
*	`-a` : all users
*	`-A|-e` : all
*	`-C` : command name
	*	obs: better than using `grep`
*	`-h` : no header
*	`-o COLUMN1,COLUMN2...` : select format columns
	*	e.g.: `-o pid,user,cmd` 
*	`-u` : show owner user
*	`-x` : include processes without associated terminal

`strace PROCESS` : list of system call made;  
*	``(relies on ptrace syscall)  ``
*	``-f`` : follow forks  

`wait [PID]` : wait for `PID` to terminate
*	`PID` : if not specified, waits for all children

## SYSTEM

#### configure

`sysctl` : 
*	`-p [FILE]` : load file, default is `/etc/sysctl.conf`

#### debug

`dmesg` : kernel messages  
`systemctl
`journalctl` : system logs?  
*	run as `sudo` to see all, like kernel stuff
*	`-b` : boot logs (same you see at boot)
  
### signals   

`kill [-N] {PID|%JOBSPEC}` : send signal number `N` 
*	`-l`,`-L` : list signal names
*	default: `N=9`
*	signals :
	*	`15` : ask interrupt
	*	`9` : force interrupt

`trap [-lp] [[CODE] SIGNAL ...]` : register **signal handler** to os, so on `SIGNAL` from the calling process, `CODE` is executed  
*	`-l` : list signals
*	signals :
	*	`DEBUG` : thrown by shell before executing each command
	*	`RETURN` : thrown by shell after a function call return, or the import of a source file
	*	`ERR` : launched by shell on error
	*	`EXIT` : launched by shell on exit (for any reason, except kill)
*	e.g.: if executed from terminal, it's for terminal's process signals
*	e.g.: if in a script, it's for that script
  
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
  
## Variables

`declare NAME[=VAL]` : declare a var or set properties on it  
*	`-i` : type int
*	`--` : no type

`let` : eval arithmetic expression  
*	e.g.: `let N++`

`shopt [-pqsu] [-o] [OPTNAME...]` : set shell options
*	`-s` : set
*	`-u` : unset
*	e.g.: `shopt -s extglob` : enable extended pattern matching
  
## MISC  

`alias` : display alias  
*	``alias [...]`` : define alias  

`bc` : calculator, allows floats  
`clear` : clears terminal and starts from first row  
`date` : date formats converter 
*	`+%s` : epoch  

`getopts OPTSTRING NAME [ARGS...]` : (built-in) get options  
*	`OPTSTRING`: made of...
	*	`A` : letter - flag
	*	`A:` : letter - flag with required arg
		*	e.g.: `-a arg` 
*	`OPTIND` : set to `1` at script start, increased at each arg or arg value read
*	`OPTAGR` : stores value for arg currently read
*	e.g.: see [examples.md](examples.md)

`history` : history of commands given  
`man [SECTION] COMMAND` : manual  
*	`-a KEYWORD` : get entries for all sections  
*	`-k REGEX` : search REGEX in short descriptions and names  
*	note: many commands need `mandb` updated
*	e.g.: `man man` : manual for manual  
*	e.g.: `man ascii` :   
*	e.g.: `man 2 SYSTEM_CALL` :   
	*	e.g.: `man 2 write` : write()  

`sudo mandb` : update `man` database  

`md5sum [FILE]` : md5 hash of `FILE`
*	e.g.: `echo -n STRING | md5sum` : hash of string (remove `\n` with `-n`)  

`reset` : reset terminal  
`script` : start printing all typed commands in a file
*	exit with `exit` or `Ctrl+D`
*	note: also captures special characters used by terminal for coloring (so should like deactivate colors/use another terminal)

`shift [N]` : shift arguments, of `N` positions  
`source FILE` : execute lines in `FILE` as a script  
*	`.` : alias for `source`

`timedatectl` : time for pc/os/hw…  
`type COMMAND` : type of command  
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
`uptime` : uptime and system load (last 15,5,1 minutes)  
  
## Packages
  
### apt  
`apt autoremove` : remove unnecessary packages  
`apt search APPLICATION_NAME` :  
`apt show ` :   
*	``-a`` : all entries  

`apt update` : check updatable packages  
`apt upgrade` : update updatable packages  

### debconf

`debconf-show PKG` : show package configuration
*	also shows questions and answers given in config phase

### dpkg

`dpkg-reconfigure PKG` : reconfigure package
*	e.g.: restart configuration if it has one

### apt
`update-grub` : update grub  
*	e.g.: boot options  
