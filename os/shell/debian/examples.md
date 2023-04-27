# EXAMPLES

## dpkg
list installed packages, sorted by size (also shows pkgs uninstalled but not purged):  
```dpkg-query -Wf '${Installed-Size}\t${Package}\n' | sort -n```  
purge uninstalled pkgs:  
```dpkg --list |grep "^rc" | cut -d " " -f 3 | xargs sudo dpkg --purge```  
list installed packages, sorted by size; also hide not installed but not purged:  
```dpkg-query -Wf '${db:Status-Status} ${Installed-Size}\t${Package}\n' | sed -ne 's/^installed //p'|sort -n```  
