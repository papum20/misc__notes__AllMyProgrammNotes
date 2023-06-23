# GDB  
  
## README.md  
*	[README.md](./README.md)  

## PATTERN
Command `pattern OPTIONS`.  
Create a pattern in memory/registers, which can be found later: can be used to map memory, find locations..  
*	e.g.: to find addresses after compilator optimizations  

How to get the offset, after giving the pattern as input to the program:  
1.	`x/gx rdx` : read the register VALUE  
2.	`pattern offset VALUE` : get the offset  


### References:
*	https://myexperiments.io/exploit-basic-buffer-overflow.html  
