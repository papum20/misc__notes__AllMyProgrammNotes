# OBJECTS
  
## TYPES
`DIR` : directory stream  

`struct dirent` :  
*	`ino_t d_ino` : inode, file serial number
*	`off_t d_off` :  
*	`char d_name[]` : filename
*	`unsigned short d_reclen` : record length
*	`unsigned char d_type` : file type, represented by a constant

## CONSTANTS

```
DT_BLK      This is a block device.
DT_CHR      This is a character device.
DT_DIR      This is a directory.
DT_FIFO     This is a named pipe (FIFO).
DT_LNK      This is a symbolic link.
DT_REG      This is a regular file.
DT_SOCK     This is a UNIX domain socket.
DT_UNKNOWN  The file type could not be determined.
```


## FUNCTIONS

`int closedir(DIR *)` :  
`DIR *opendir(const char *)` :  
`struct dirent *readdir(DIR *)` : return pointer to `struct dirent` fof a file, like a list, i.e. use again to get following file, and returns `NULL`
*	return: also `NULL` for error, and sets `errno`
  
`int alphasort(const struct dirent **, const struct dirent **)` :  
`int dirfd(DIR *)` :  
`DIR *fdopendir(int)` :  
`int readdir_r(DIR *restrict, struct dirent *restrict, struct dirent **restrict)` :  
`void rewinddir(DIR *)` :  
`int scandir(const char *, struct dirent ***, int (*)(const struct dirent *), int (*)(const struct dirent **, const struct dirent **))` :  
`void seekdir(DIR *, long)` :  
`long telldir(DIR *)` :  
