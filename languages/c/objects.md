# OBJECTS  
  

## README.md  
*	[README.md](./README.md)  

## FUNCTIONS
  
CONVERSION:  
strtol(const char *str, char **endptr, int base) : string to long, from base (0=automatic)  
  
IN/OUT:  
printf(char *format, arg1, arg2, arg3, ...);  
	% prints everything (es. %%d)  
%d int  
%10d int with min. 10 char to the right  
%-10d int with min. 10 char to the left  
%f float  
%lf double  
%lu unsigned long  
%10.5f float with min. 10 char (5 decimal)  
%p pointer  
%s all char in string  
%10s at least 10 char of a string (to the right)  
%-10s // (to the left)  
%15.10s at least 15 char, with up to 10 from string to the right  
%*10s at least <arg> chars (printf(“%*s, len, “str”))  
%c char  
	%x : hexadecimal  
	%02x : significant digits  
  
scanf(char *format, *arg1, *arg2, *arg3, ... );		(&arg)  
%c char, copied in the first byte pointed by the pointer  
%10c 10 char, copied in the first 10 bytes pointed by the pointer  
%s string, copied starting from the pointer, and added ‘\0’ at the end  
%d / f / lf  
  
write(int buffer, “string”, int dim) : prints to stream buffer (1=stdout) up to dim chars  
  
MEMORY:  
asm(“string”) : acces register named “string”  
free(pointer) : gives memory back to OS  
malloc(int size) : allocates size memory; returns pointer to it (NULL if free mem not found)  
	p=(type*)malloc(int)  
sizeof( )  
  
  
FILE :  
fclose(FILE* ) : (important for w mode, or os could not save)  
feof(FILE* ) = bool end of file  
fgets(string, int, FILE*) : reads max int char  
fgets(char*, int, *FILE) : reads max int chars in FILE (or until end of row i.e. “\n”) and stores			    it in char*  
fprintf(FILE* , “%..”, ..) :  
fread(void *ptr, size_t size, size_t nmemb, FILE *stream) : reads nmemb times,  
from stream, something of size size, and saves to ptr  
fscanf(FILE* , “..”, &..) :  
getline(char **buffer, int *buffer_len, stream) : reads line and saves in buffer;  
allocates dynamically memory, i.e. adjustes size (and modifies buffer_len)  
getopt_long(argc, argv, short_options, static struct options long_options[], NULL) :  
get program call parameters; returns short_option (? if error);  
needs a declared static struct options <name>[] =  
{{“command-name”, arg, NULL, command-short-char’},..}  
arg=(no_argument or 0, required_argument or 1)  
open_memstream(char **string, int *size) : opens file in write mode (like fopen);  
when ended writing, allocates spaces and “saves it”  
rewind(FILE * ) : restart stream  
  
<dirent.h>  
closedir(DIR *) :  
opendir(DIR *) :  
readdir(DIR *) :  
  
FUNCTIONS:  
qsort(vector, length, size, function*) : quicksort; function(a,b) returns int >= 0 if a>=b,  
else int < 0  
  
  
MACRO :  
size_t sizeof() :  
typeof() :  
  
SYSTEM CALLS :  
PROCESS:  
_exit() : exit without deletes and other freeing stuff (warning)  
access(“file”, int <right>) : if user has right on file  
atexit(<function>) : defines exit routine  
exit(int) : ; argument=exit value (err)  
fork() : “clones” current process, making both continuing from fork();  
	return: parent->child pid, child->0  
getcwd(NULL, 0) : current working directory (in terminal)  
int getpid() : process id  
syscall(<syscall_number>, <syscall_parameter(s)>) :  
	e.g.: syscall(__NR_write_, 1, “hello”, 5)  
  
FILE:  
fopen(“file_name/path”, “mode”) : FILE *fin = fopen();						“mode” = “r”/”w” (r -> NULL if error) (w deletes all and overwrites)  
	es.: fopen(“filename”, mode, O666) : O=permissions (like chmod)  
  
lseek(, offset, int whence) : move “cursor” in file to offset  
	whence=(SEEK_SET:set to offset, SEEK_CUR, SEEK_END:set to eof)  
pread() : read, with offset parameter=where to start  
pwrite() : /  
size_t write(<stream(?)>, “string”, <max_chars>) :   
  
dup(int oldfd), dup2(int oldfd, int newfd), dup3() :  
duplicate file descriptor (identifier for open file (int))  
	(only dup2 used)  
	dup3 allows use of flags  
pipe(int fd[2]) : write to descriptor fd[1], read, in fd[0]  
  
EVENTS:  
poll(struct pollfd*) : waits for a set (array) of file descriptors to become ready for I/O  
  
MEMORY:  
execve(char *pathname, char *argv[], char *envp[]) :  
argv=command(s), last element = 0 (‘\0’)  
envp=environment (variables(?))  
execve(char* program, char* args[], NULL) : exec program with args  
mmap(addr, length, prot, flags, fd, offset) : maps files/devices into memory  
	es. for loading libraries (dynamic libraries: only load called functions,  
then the mapping can be deleted, or not)  
mmap(NULL, (struct stat s;fstat(fd,&s)).st_size, PROT_READ, 0, (fd=open(...)), 0) :  
	creates link in memory to file fd, at address addr, or nearby  
(or anywhere if NULL); length (size) of file, with offset  
munmap() :   
  
FILE SYSTEM:  
stat(char *pathname, struct stat *statbuf) : stat (info) of file  
lstat(char *pathname, struct stat *statbuf) : for symbolic link,  
get reference to file itself, instead of referenced file  
link() : (called by ln)  
chdir() :   
getcwd() : pwd  
mkdir() :   
rmdir() :   
symlink() : (called by ln -s)  
unlink() :   
chmod() :   
umask() :   
  
USERS:  
getresuid() : users table (ref. 6. s.o.)  
getresgid() :   
  
SIGNALS:  
kill() : send signal  
signal(..., function) : declare how to manage (function) when received signal  
  
NETWORKS:  
accept() :   
bind() :   
connect() :   
socket() :   
  
OTHER(?):  
shm_open() : create/open/unlink shared memory objects  
	(followed by mmap for use)  
  
LIBRARIES:  
<stdarg.h>:  
<sys/epoll.h> :   
<sys/inotify.h>: ask kernel to be informed (called) when something happens  
<sys/ppoll.h> :   
va_start() :  
va_end() :  


## CONSTANTS  
EOF : =-1 (type: int; represents a character of type int;  
used int just to add it, other than 25 chars)  
errno : (errno.h)  

