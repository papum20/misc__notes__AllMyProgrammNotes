# GDB  
  
  
  
## DEBUG
disassemble function_name : disassemble function content,  
showing offset of instructions with respect to function addr  
info, i :  
info breakpoints, b : list breakpoints  
info registers, r : show registers  
print expr	:   
	e.g. expr=$reg_name		: register  
	e.g. expr=&var		: var   
	e.g.: expr=(function_name) : call function  
print/f 		: f=format = d|x|u|f (=signed,hex,unsigned,float)  
p		= alias for print  
set {type}address = value : variable at address of type  
	e.g. set {int}0x… = 0x…  
x/nfu addr	: examine : inspect memory content  
		n = (default = 1) how many elements to print  
		f = (default = x) print format  
		f=s(string) | i(disassembly) | x(hex) | f(float) | d(signed)  
		u = (default = w) size of each element to print  
		u = b(bytes) | h(halfwords=2B) | w(words=4B) | g(giant words=8B)  
		addr=mem address (e.g. 0x…) | $reg | arithmetics (e.g. $reg+1)  
  
## MISC 
exit : exit  
file FILE_NAME : execute  
	file must have exe mode  
help COMMAND : get help on command  
  
## RUNNING
break		: add breakpoint  
break *addr	: add breakpoint when executed instruction at address  
break LOCATION : add breakoìpoint on function  
b		= break  
*	LOCATION = function_name | *address  

continue	: continue after breakpoint  
delete N : delte breakpoint number N  
next, n		: next step, i.e. through subroutines  
run		: start debugging  
start : start (no run)  
step, s		: next line of instruction  

## README.md  
*	[README.md](./README.md)  

