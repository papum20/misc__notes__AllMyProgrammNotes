# EXAMPLES

## I/O STREAMS

Remove extension and path from filename (filenames in all directories):
```bash
find . -name '*' | sed 's#.*/##; s#[.][^.]*$##'
```

## dpkg
list installed packages, sorted by size (also shows pkgs uninstalled but not purged):  
```dpkg-query -Wf '${Installed-Size}\t${Package}\n' | sort -n```  
purge uninstalled pkgs:  
```dpkg --list |grep "^rc" | cut -d " " -f 3 | xargs sudo dpkg --purge```  
list installed packages, sorted by size; also hide not installed but not purged:  
```dpkg-query -Wf '${db:Status-Status} ${Installed-Size}\t${Package}\n' | sed -ne 's/^installed //p'|sort -n```  

## grub
`update-grub` : update boot grub entries  
add or uncomment `GRUB_DISABLE_OS_PROBER=false` to `/etc/default/grub` first : if problem (not showing windows in dual boot)  