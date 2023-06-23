# BASICS

## README.md  
*	[README.md](./README.md)  

## VARIANTS
`gcc-multilib` : for cross-compiling (i.e. for different architectures from current)  

## INCLUSION ORDER

// From man:  
Directories specified with -iquote apply only to the quote form of the directive, "#include "file"".  Directories specified with -I, -isystem, or-idirafter apply to lookup for both the "#include "file"" and "#include FILE" directives.  
You can specify any number or combination of these options on the command line to search for header files in several directories.  The lookup order is as follows:  
1.  For the quote form of the include directive, the directory of the current file is searched first.  
2.	For the quote form of the include directive, the directories specified by -iquote options are searched in left-to-right order, as they appear on the command line.  
3.  Directories specified with -I options are scanned in left-to-right order.  
4.  Directories specified with -isystem options are scanned in left-to-right  
	order.  
5.  Standard system directories are scanned.  
6.  Directories specified with -idirafter options are scanned in left-to-right order.  

  
