# EXAMPLES

## I/O STREAMS

Remove extension and path from filename (filenames in all directories):
```bash
find . -name '*' | sed 's#.*/##; s#[.][^.]*$##'
```

## Functions

get return value from background processes, and also be able to manage job ids :
*	```bash
	out_file_1=$(mktemp)
	out_file_2=$(mktemp)
	( proc_1 > $out_file_1 ) &
	( proc_1 > $out_file_2 ) &
	wait
	out_1=$(cat $out_file_1)
	out_2=$(cat $out_file_2)
	```

## Misc

generate random password :
*	```bash
	# remove all characters that are not alphanumeric, and only take 6
	tr -dc A-Za-z0-9 </dev/urandom | head -c 6; echo
	```
	*	src: https://unix.stackexchange.com/a/230676

### getopts
```bash
#!/usr/bin/env bash
aflag=
bflag=
while getopts 'ab:' OPTION ; do
	case $OPTION in
	a) aflag=1
		;;
	b) bflag=1
		bval="$OPTARG"
		;;
	?) printf "Usage: %s: [-a] [-b value] args\n" $(basename $0) >&2
		exit 2
		;;
	esac
done
shift $(($OPTIND - 1)) # getopts cycles over $*, doesn't shift it
# so now $* only stores args, not flags
if [ "$aflag" ] ; then
	printf "Option -a specified\n"
fi
if [ "$bflag" ] ; then
	printf 'Option -b "%s" specified\n' "$bval"
fi
printf "Remaining arguments are: %s\n" "$*"
```

## Packages

### dpkg
list installed packages, sorted by size (also shows pkgs uninstalled but not purged):  
```dpkg-query -Wf '${Installed-Size}\t${Package}\n' | sort -n```  
purge uninstalled pkgs:  
```dpkg --list |grep "^rc" | cut -d " " -f 3 | xargs sudo dpkg --purge```  
list installed packages, sorted by size; also hide not installed but not purged:  
```dpkg-query -Wf '${db:Status-Status} ${Installed-Size}\t${Package}\n' | sed -ne 's/^installed //p'|sort -n```  

### grub
`update-grub` : update boot grub entries  
add or uncomment `GRUB_DISABLE_OS_PROBER=false` to `/etc/default/grub` first : if problem (not showing windows in dual boot)  