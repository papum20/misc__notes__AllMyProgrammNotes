# batch  
  
OPERATORS:  
EQU : ==  
NEQ : !=  
LSS : <  
LEQ : <=  
GTR : >  
GEQ : >=  
  
STATEMENTS:  
:function : function declaration  
EXIT : exits function  
Call :function, value1, … valuen : call function with parameters  
%~n : function parameter  
  
IF condition (  
	…  
) ELSE (  
	…  
)  
  
USES:  
%var% : use value of var  
::text : comment  
%n : parameter number n  
  
COMMANDS:  
format:  
<command> ..  
title  
  
@echo : prints command output  
	title <text> : title showed for window  
@echo off : (quicker(?))  
	  
  
call : executes command internally (in current terminal)  
cd : cd (only while script)  
pause : waits for input  
rem : comment  
setlocal : makes set (command) set variables as local  
set <var>=<string> : set environment variable (new or existing)  
	set /p <var>=<string> : print string and get input to set var  
start : executes command externally (in another terminal)  
