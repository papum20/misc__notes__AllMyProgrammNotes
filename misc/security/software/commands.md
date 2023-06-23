# COMMANDS


## MITIGATIONS
`echo 0 > /proc/sys/kernel/randomize_va_space` : deactivate ASLR  
`gcc -g -z execstack -fno-stack-protector ...` : compile without NX  
*	`-no-pie` : no pie  
*	note: `-g` : needed??  
*	note: `-fno-stack-protector` : canary

### CANARY

Implementation: when activated, this code is added to the program:  
```c
long in_FS_OFFSET;
char buf [72];
long canary;

canary = *(long *)(in_FS_OFFSET + 0x28);
/*	...some code...
	gets(buf);
*/
if (canary != *(long *)(in_FS_OFFSET + 0x28))
	/* check if canary was modified */
	__stack_chk_fail();
```


## TOOLS
`checksec` : check security (mitigations) on  
`readelf ELF` : read elf  
*	`-h`	: header  
*	`-l`	: segments  
*	`-S`	: sections  
