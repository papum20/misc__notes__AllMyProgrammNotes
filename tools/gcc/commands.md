# COMMANDS

## gcc / g++  
`T./file` : execute file, search it in current directory  
`gcc -c file_name.c` : compile (not link) -> generates obj file (file.o)  
`gcc -c -lncurses file_name.c` :   
`gcc -c -lpthread file_name.c` :   
`gcc -o file.o` : linking -> generates .exe  
`gcc file.c -o exe_name` : creates exe named exe_name from file.c  
`-std=STD` : c/c++ version  
  
`-Wall` : display errors  
  
### ARCHITECTURE
`-m32` : generate code for 32bit  

## INCLUDE/SEARCH PATH   
`-static` : compiles without dynamic libraries  
`-H` : print included files  
`-IDIR` : include dir in search path  
`-iquoteDIR` : include dir in search path only for quoted includes  


## INTERMEDIATE FILES   
`gcc -E FILE.c` : interrupts compiler after preprocessor -> returns standard output  
*	`returns code with preprocessor substitutions made`  
`cpp FILE.c` : //  
`-S` : generates .s file in human readable assembly instead of .exe  
`ld FILE.O` : link  
`-save-temps` : save intermediate files  
  
## SECURITY / MITIGATIONS
`-z execstack` : no nx  
`-fno-stack-protector` : canary  
`-no-pie` : no pie  
`−D_FORTIFY_SOURCE=1` : enable `fortify`  
*	i.e. simple checks, relative to specific compiler  
