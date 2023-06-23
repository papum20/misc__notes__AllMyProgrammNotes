# OBJECTS  
  

## README.md  
*	[README.md](./README.md)  

## FUNCTIONS
  
### CMD
`getopt(nt argc, char *argv[], const char *optstring)` : reads command line arguments (starting with `-`), returns the next one, or `-1` if read all  
*	`optstring` : sequence of letters (args); `A:` requires a value, `A::` has optional val  
*	`char *optarg` : stores the argument value  
*	`int optind` :  
*	`int opterr` :  
*	`int optopt` :  

### CONVERSION  
`strtol(const char *str, char **endptr, int base)` : string to long, from base (0=automatic)  
  
### I/O  
`printf(char *format, arg1, arg2, arg3, ...)` 
*	`%` : prints everything
*		e.g.: `%%d`  
*	%d int  
*	%10d int with min. 10 char to the right  
*	%-10d int with min. 10 char to the left  
*	%f float  
*	%lf double  
*	%lu unsigned long  
*	%10.5f float with min. 10 char (5 decimal)  
*	%p pointer  
*	%s all char in string  
*	%10s at least 10 char of a string (to the right)  
*	%-10s // (to the left)  
*	%15.10s at least 15 char, with up to 10 from string to the right  
*	%*10s at least ARG chars (printf(“%*s, len, “str”))  
*	%c char  
*	`%x` : hexadecimal  
*	`%02x` : significant digits  
  
`scanf(char *format, *arg1, *arg2, *arg3, ... )` :		(&arg)  
*	%c char, copied in the first byte pointed by the pointer  
*	%10c 10 char, copied in the first 10 bytes pointed by the pointer  
*	%s string, copied starting from the pointer, and added ‘\0’ at the end  
*	%d / f / lf  
  

`write(int buffer, “string”, int dim)` : prints to stream buffer (1=stdout) up to dim chars  
  
### MEMORY  
`asm(“string”)` : acces register named “string”  
`free(pointer)` : gives memory back to OS  
`malloc(int size)` : allocates size memory; returns pointer to it (NULL if free mem not found)  
*	e.g.: `p=(type*)malloc(int)` :  

`sizeof( )` :  
  

### FILE   
`fclose(FILE* )` : (important for w mode, or os could not save)  
`feof(FILE* )` : bool end of file  
`fgets(string, int, FILE*)` : reads max int char  
`fgets(char*, int, *FILE)` : reads max int chars in FILE (or until end of row i.e. “\n”) and stores it in char*  
`fprintf(FILE* , “%..”, ..)` :  
`fread(void *ptr, size_t size, size_t nmemb, FILE *stream)` : reads nmemb times, from stream, something of size size, and saves to ptr  
`fscanf(FILE* , “..”, &..)` :  
`getline(char **buffer, int *buffer_len, stream)` : reads line and saves in buffer;  
*	allocates dynamically memory, i.e. adjustes size (and modifies buffer_len)  
`getopt_long(argc, argv, short_options, static struct options long_options[], NULL)` : get program call parameters; returns short_option (? if error);  
*	needs a declared static struct options NAME[] = {{“command-name”, arg, NULL, command-short-char’},..}  
*	arg=(no_argument or 0, required_argument or 1)  
`open_memstream(char **string, int *size)` : opens file in write mode (like fopen);  
*	when ended writing, allocates spaces and “saves it”  
`rewind(FILE * )` : restart stream  
  
#### dirent.h  
`closedir(DIR *)` :  
`opendir(DIR *)` :  
`readdir(DIR *)` :  
  

### FUNCTIONS  
`qsort(vector, length, size, function*)` : quicksort; function(a,b) returns int >= 0 if a>=b,  
*	else int  0  
  
  
## MACRO   
`_Generic(VAR, type1:"STR1", ...)` : return the STR associated with the type of VAR  
*	done at run-time  
*	error if no case for VAR type  
*	(works like switch)  


`size_t sizeof()` :  
`typeof()` :  
 
## LIBRARIES  
### stdarg.h  

### sys/epoll.h   
### sys/inotify.h
// ask kernel to be informed (called) when something happens  
### sys/ppoll.h   
`va_start()` :  
`va_end()` :  


## CONSTANTS  

`EOF` : =-1 (type: int; represents a character of type int;  
*	used int just to add it, other than 25 chars)  
`errno` : (errno.h)  

