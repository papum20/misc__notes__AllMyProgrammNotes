# BASICS  
  
types of selection of files:  
*(pattern-list) : matches zero or more occurrences of the specified patterns  
?(pattern-list) : matches zero or one occurrence of the specified patterns  
+(pattern-list) : matches one or more occurrences of the specified patterns  
@(pattern-list) : matches one of the specified patterns  
!(pattern-list) : matches anything except one of the given patterns  
*(“pattern1”|”pattern2”) : both patterns (valid with all *?+@! )  
e.g.: rm !(“a.txt”|”b.txt”)  
  
  
CONSTANTS:  
. : current dir  
/ : root dir  
$HOME : ~ (user home)  
$PATH :   
(format) : path1:path2:..:path  
export PATH=$PATH:<new_path> : append (add last)  
export PATH=<new_path>:$PATH : prepend (add first)  
// changes with export are temporary, for current session;  
// to make changes permanent:  
add command to ~/.profile  
change path in etc/environment  
  
KEYS:  
Ctrl+C :   
Ctrl+D : end of file  
<command1> | <command2> :  
concatenate commands / command2 input=command1 output  
<command> !$ : last parameter in last row command  
$? : return value of last executed process  
	0 = successful  
	1 = some error  
!! : last command  
&& : and  
|| : or, evaluates other if one fails (error)  
## README.md  
*	[README.md](./README.md)  

# : comment  
  
STREAMS:  
standard input :   
standard output :  
standard error :  
REDIRECTING COMMAND OUTPUT:  
command > file.txt	: write output to file  
command >> file.txt	: append  
command &> file.txt	: also write error  
command &>> file.txt	: -  
  
  


