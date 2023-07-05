# OBJECTS

## SYSTEM CALLS  

### PROCESS  
`_exit()` : exit without deletes and other freeing stuff (warning)  
`access(“file”, int RIGHT)` : if user has right on file  
`atexit(FUNCTION)` : defines exit routine  
`exit(int)` : ; argument=exit value (err)  
`fork()` : “clones” current process, making both continuing from fork();  
*	return: parent->child pid, child->0  

`getcwd(NULL, 0)` : current working directory (in terminal)  
`int getpid()` : process id  
`syscall(SYSCALL_NUMBER, SYSCALL_PARAMETER(S))` :  
*	e.g.: `syscall(__NR_write_, 1, “hello”, 5)`  
  
### FILE  

default file descriptors:  
```c
#include <unistd.h>
#define STDIN_FILENO	0
#define STDOUT_FILENO	1
#define STDERR_FILENO	2
```

`int fileno(FILE *stream)` : from FILE* to fd  
`FILE *fopen(char *path, char *mode)` :  
*	`mode='r|w'` : (r -> NULL if error) (w deletes all and overwrites)  
*	e.g.: `fopen(“filename”, mode, O666)` : O=permissions (like chmod)  

`FILE *fdopen(int fd, const char *mode)` : open stream from fd  
*	note: closing the stream, closes the fd  

`lseek(fd, OFFSET, int whence)` : move “cursor” in file to OFFSET  
*	`WHENCE=`:
	*	`SEEK_SET` : set to offset
	*	`SEEK_CUR` : set to current+offset
	*	`SEEK_END` : set to eof+offset  

`open(const char *pathname, int flags, mode_t mode)` :   
*	`flags=`:  
	*	`O_RDONLY|O_WRONLY|O_RDWR` : rw  
	*	`O_CREAT` : create if file not existing  
*	`mode=`: permissions (used for `O_CREAT`)  
	*	`S_I{RWX{U|G|O}|{R|W|G}{USR|GRP|OTH}}` :  

`pread()` : read, with offset parameter=where to start  
`pwrite()` : /  
`size_t write(STREAM(?), “string”, MAX_CHARS)` :   
  
`dup(int oldfd), dup2(int oldfd, int newfd), dup3()` : duplicate file descriptor (identifier for open file (int))  
*	(only dup2 used)  
*	dup3 allows use of flags  

`pipe(int fd[2])` : write to descriptor fd[1], read, in fd[0]  
  
### EVENTS  
`poll(struct pollfd*)` : waits for a set (array) of file descriptors to become ready for I/O  
  
### MEMORY  
`execve(char *pathname, char *argv[], char *envp[])` :  
*	argv=command(s), last element = 0 (‘\0’)  
*	envp=environment (variables(?))  
`execve(char* program, char* args[], NULL)` : exec program with args  
`mmap(addr, length, prot, flags, fd, offset)` : maps files/devices into memory  
*	es. for loading libraries (dynamic libraries: only load called functions,  
*	then the mapping can be deleted, or not)  

`mmap(NULL, (struct stat s;fstat(fd,&s)).st_size, PROT_READ, 0, (fd=open(...)), 0)` :  
*	creates link in memory to file fd, at address addr, or nearby  
(or anywhere if NULL); length (size) of file, with offset  

`munmap()` :   
  
### FILE SYSTEM  
`struct stat stat(char *pathname, struct stat *statbuf)` : stat (info) of file  
*	```c
	struct stat {
		...
		st_size;	// size (bytes)
	}
	```

`lstat(char *pathname, struct stat *statbuf)` : for symbolic link,  
*	get reference to file itself, instead of referenced file  
`link()` : (called by ln)  
`chdir()` :   
`getcwd()` : pwd  
`mkdir()` :   
`rmdir()` :   
`symlink()` : (called by ln -s)  
`unlink()` :   
`chmod()` :   
`umask()` :   
  
### USERS  
`getresuid()` : users table (ref. 6. s.o.)  
`getresgid()` :   
  
### SIGNALS  
`kill()` : send signal  
`signal(..., function)` : declare how to manage (function) when received signal  
  
### NETWORKS  
`accept()` :   
`bind()` :   
`connect()` :   
`socket()` :   
  
### OTHER(?)  
`shm_open()` : create/open/unlink shared memory objects  
*	(followed by mmap for use)  
  
