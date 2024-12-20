# COMMANDS

Set-Location : (cd) change directory  
  
Get-Childitem : (dir) list of files in current directory  
Get-Command : list of available commands  
Get-Command -commandtype <command_type> : only shows commands  
	of that type (cmdlet, function, alias)  
Get-Help : (help)   
	Get-Help <command> : help for command (local man)  
	Get-Help <command> -online : help for command (online man)  
  
Rename-Item <old-file> -NewName <new-file> : (rename)  
  
Restart-Computer : (shutdown /r)  
Stop-Process -Name <process> :  
Stop-Computer : (shutdown /s) shutdown  
  
Test-Connection -ComputerName (hostname) : (ipconfig)  
  
gcm : path of PATH executable file  