# NOTES  
  
## README.md  
*	[README.md](./README.md)  

## OS

SYSTEM CALLS :   
functions which call kernel functions (just pass own parameters to them)  
fail -> return -1  
fail info -> errno  
errno : global variable - used to return error messages  
  
WHY - USE CASES:  
managing…  
processes  
e.g.: fork, exec  
fork : duplicates process,  
i.e. creates new process, copy of current, with own memory  
i.e.: duplicates variables, allocating their own memory  
(actually uses same memory (avoids copying time), and only  
duplicates when a process tries to modify the value)  
getpid : process id  
getppid : parent process id (manager of some procs)  
wait : wait for a change of status from child processes  
C: wait(&status), int status  
memory  
brk : (asks to) increase initialized (allocated) memory in heap  
associated to process, in own virtual memory  
(used by malloc -> usually not used by programmer)  
exec : changes memory content for proc in execution  
execve : (actual exec)  
if fail:   
files:  
// file name isn’t file attribute, but parent directory attribute  
// a file stops existing when no directory/file has a reference to it (its name)  
file system: abstraction of hw memory, showing files (permissions, dirs structure…)  
note: open() = contact point file-file_system  
users:  
getresuid  
signals  
e.g.: errors, segmentation fault (signal 11 from kernel)  
IPC (inter process communication)  
time  
e.g.: execution time, global time  
networking  
misc  
e.g.: name of this system  
  
FILES:  
Process Control Block (PCB) : structure with info associated with running process  
PCB -> contains “vector” of references to own open files in open file table  
Open File Table : contains an entry for each open file (in any mode: r/w…),  
	for each process (contains duplicates if same file open by multiple procs);  
	entry = reference to V node  
V node = inode, with more info (file length, type of file opening (w/r), ...)  
not duplicated (multiple open file table entries can refer to the same)  
consequence : proc1 edits file, from entry1 in table -> v-node1 changes ->   
	proc2 sees change, from entry2, which points to the same v-node  
note : procs created with fork, keep same entry as parent (should..)  
(otherwise: race condition)  
  
USERS :  
  
  
  
real  
effective:  
(user who can do stuff)  
saved  
uid  
  
  
...  
  
  
gid  
  
  
...  
  
  
  
who can change entries :  
root (all)  
user (only effective, with some operations)  


