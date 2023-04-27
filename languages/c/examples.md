# EXAMPLES

// like a macro for functions  
typedef void (* voidfun) (void *argc);  
es.:	//function as paramter  
void fun(voidfun f, void *opaque) {  
	f(opaque);  
}  
  
  
SWAP:  
int a,b;  
a ^= b ^= a ^= b;  

## FUNCTIONS
`execv(argv[1], argv+1)` : exec argv[1] with, as args, all following args  
  

## README.md  
*	[README.md](./README.md)  

