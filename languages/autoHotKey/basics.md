# BASICS  
  
run the script with AutoHotKey to apply it  
  
at the end of each command:  
...  
return  
  
; some comment  
  
def:  
var_name := some_value  
  
HOTSTRING:  
short form for another string  
  
::short:: full string  
return  
  
HOTKEY:  
keyboard shortcut  
  
SYMBOL  
KEY  
^  
Ctrl  
!  
Alt  
+  
Shift  
#  
Win  
  
  
symbol+key:  
es.  
^q::  
…  
return  
  
#:  
  
#IfWinActive window_name (es. file_name - Notepad) : script only works if window active  
#IfWinExist window_name (es. file_name - Notepad) : script only works if window open  
