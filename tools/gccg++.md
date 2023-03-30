# gcc / g++  
  
T./file : execute file, search it in current directory  
gcc -c file_name.c : compile (not lin) -> generates obj file (file.o)  
gcc -c -lncurses file_name.c :   
gcc -c -lpthread file_name.c :   
gcc -o file.o : linking -> generates .exe  
gcc file.c -o exe_name : creates exe named exe_name from file.c  
-std=<std> : c/c++ version  
  
-Wall		: display errors  
  
INCLUDE/SEARCH PATH :  
(see man section for more info)  
-static : compiles without dynamic libraries  
-H : print included files  
-I<dir> : include dir in search path  
-iquote<dir> : include dir in search path only for quoted includes  
FROM MAN:  
***  
Directories specified with -iquote apply only to the quote form of the directive, "#include "file"".  Directories specified with -I, -isystem, or-idirafter apply to lookup for both the "#include "file"" and "#include <file>" directives.  
You can specify any number or combination of these options on the command line to search for header files in several directories.  The lookup order is as follows:  
1.  For the quote form of the include directive, the directory of the current  
               file is searched first.  
2. For the quote form of the include directive, the directories specified by  
-iquote options are searched in left-to-right order, as they appear on the  
command line.  
           3.  Directories specified with -I options are scanned in left-to-right order.  
           4.  Directories specified with -isystem options are scanned in left-to-right  
               order.  
           5.  Standard system directories are scanned.  
           6.  Directories specified with -idirafter options are scanned in left-to-right  
               order.  
***  
  
INTERMEDIATE FILES :   
.i		: after preprocessor  
.s		: after compiler  
.o		: after assembler (written  opcodes / in machine/object code)  
.out/.exe	: executable (for linux/win)  
gcc -E FILE.c : interrupts compiler after preprocessor -> returns standard output  
	returns code with preprocessor substitutions made  
cpp FILE.c : //  
-S : generates .s file in human readable assembly instead of .exe  
ld <file.o> : link  
-save-temps	: save intermediate files  
  
  
(linux)  
/usr/include/x86_64-linux-gnu/asm/unistd_64.h : system calls (c)  
