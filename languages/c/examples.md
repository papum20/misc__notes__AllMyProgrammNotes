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
  

## README.md  
*	[README.md](./README.md)  

