# SYNTAX

## Command call
Bash calls an `exec` for an invoked command, thus replacing itself (with its associated `pid`) with the new process for the command.  

## Redirections
Shell can close a proc's stream to a file, and replace it with another file descriptor
*	obs: proc doesn't see change (directly), has always the fd's

_precedence_ : right to left 
*	e.g.: `ls > file 2>&1` : first redirects `stderr` to `stdout`, then `stdout` to `file` (so both go to `file`)

`[N]> FILE` : open `FILE` for writing on fd `N`
*	if `N` doesn't exist, the new fd is **created** for `FILE` for the process
*	`> FILE` : if `N` omitted, it's `stdout`
*	e.g.: `1` for `stdout`, `2` for `stderr`
*	e.g.: `exec 2>/dev/null` : redirect **permanently** for all executions

`N>&-` : close fd `N`
*	e.g.: `exec 2>&-` : reset `exec 2>/dev/null`

`N>&M` : redirect output fd `N` to already open fd `M`  
`N>>` : `stdout` to file, appending  
`[N]< FILE` : open `FILE` for reading on fd `N`
*	`< FILE` : default `stdin`

`N<> FILE` : `N` can be used for both r/w  

use as input given multiline text :
```bash
COMMAND <<MARKER
lines here
MARKER
```
*	`MARKER` used as first and last marker, mustn't appear inside lines
*	`<<-MARKER...` : (with `-`) input stripped from input lines and line containing MARKER

`<<< "TEXT"` : use `TEXT` as input  

## Subshell
Shell calls a `fork` on itself, thus creating its own duplicate; then each resulting shell can invoke a command.  

`CMD1 | CMD2` : **pipe** - 
*	steps:
	1.	shell creates a new fd with `pipe`
	2.	shell forks (`fork`)
	3.	shell associates pipe's write to `CMD1`, and read to `CMD2` (with `dup2`)
	4.	shell closes `pipe`, to avoid bad use of pipe
		*	e.g.: `CMD2` uses pipe for write
		*	so `CMD1`'s write is `CMD2`'s read
	5.	each subshell execs its command with `exec`

`(CMD1; CMD2)` :  


## VARIABLES
`$VAR` : variable val  
`${VAR}` : variable val  
`${VAR:-DFLT}` : if `$VAR` null or not set, return `DFLT` string  
`${VAR:=DFLT}` : if `$VAR` null or not set, set `VAR=DFLT` and return `DFLT` string  
`${VAR:?DFLT}` : if `$VAR` null or not set, return `DFLT` and exit (error)  
`${VAR?DFLT}` : if `$VAR` not set (even if null), return `DFLT` and exit (error)  

`VAR=VAL` : create/assign  
*	note: no spaces important  
*	e.g.: `VAR="3*(2+5)"` 

`local VAR=VAL` : local to function  

### Arrays
`${ARR[N]}` : at index `N`  
`${ARR[@]}` : values for all defined indexes  
*	note: `ARR=VAL` : if defined, `ARR[0]=VAL`  

`${ARR[*]}` : values for all defined indexes  
`${!ARR[@]}` : all defined indexes  
`${!ARR[*]}` : all defined indexes  
`${#ARR[@]}` : len  
`{N..M}` : range `N` to `M`  

`A=(VAL1 ...)` : assign  
*	separated by spaces (shell expansion->word splitting)
*	e.g.: `A=(1 2 3)` :  
*	e.g.: `IFS='.' ARR=${VAR}` : split `VAR` by `.` and assign to `ARR`

### Known variables
`$$` : current pid (of base process, doesn't change for subprocesses)  
`$BASPID` : current pid (subprocess)  

## VALUES
`"STRING"|'STRING'` :  
`NUM` :  
  
## OPERATORS
`;` : end line  
`{}` : separate code blocks (like c)
*	e.g.: `${VAR}` : is valid, equal to `$VAR`

`(CMD)` : launch command in subshell    
`{CMD1;CM2;}` : sequence  
*	doesn't create a subshell

`$'\x0A'` : eval char (hex)  
`$((EXPR))` : eval arithmetic expr  
`` `EXPR` `` : evaluate expr before executing command  
`'STRING'` : literal string  
`"EXPR"` : string, which allows `${}` evaluation inside  

### BOOL
Any bash expression is the result of a command (true if exited with status 0, false if e.g. error).  

`EXPR` : test return value of a command  
`[ EXPR ]` : basic eval  
*	note: actually a command (a link to `test`)
*	note: recognized by any terminal/etc.
*	e.g.: `[ $var == 1 ]` : error if var not defined

`[[ EXPR ]]` : advanced eval  
*	recognizes regex, empty var
*	note: specific to bash not recognized by any terminal/etc.

`((EXPR))` : evaluate expressions with "normal" operators  
`! CONDITION` : not  
*	`CONDITION=((EXPR))|[ EXPR ]` :  

`||` :  
`&&` :  

### COMPARE
`-OP` :  
*	note: use **spaces** around compare operator  

`-e PATH` : file exists  
`-r|w|x PATH` : file has r|w|x access  	
`-s PATH` : file not empty  

`==` :  
`=~` : regex  
*	only in `[[ ]]`

`! A == B` : `!=`  
`ARG1 -le|ne|ge ARG2` : 

`-z VAR` : true if variable not set
*	i.e. not set or set to empty (string)

`-n VAR` : true if variable set to non empty string  


### MATH
`%` :  

## ARGUMENTS  
`$N` : argument N  
`$#` : arguments len  
`$@` : array of arguments  
`$*` : stringify argv, with spaces between (`"$1 $2 ..."`)
`$1` : pid of most recent bg program  
`$?` : arg where to put return val  
*	`0` : for success
*	`>1` : error codes

obs: can emulate in terminal without script, creating vars `$N` for argument `N`  

## Pattern

### extglob
The following need `extglob` (`shopt`).  

`?(PATTERN)` : 0|1   
`*(PATTERN)` : 0+   
`+(PATTERN)` : 1+   
`@(PATTERN)` : 1  
`!(PATTERN)` : all except  

## STATEMENTS

If:
*	```bash
	if [ CONDITION ]
	then
		...
	elif ...
	then
		...
	...
	else
		...
	fi
	```
*	```bash
	if [ CONDITION ]
	if ((CONDITION))
	```



Switch:  
*	```bash
	case $VAR in
		OPT1) ...;;
		OPT2) ...;;
		# OPTs can be any shell expression, e.g. including *
		?) ...;; # default
	esac
	```
*	e.g.: 
	```bash
	case "$var" in
	val1) echo val1 ;;
	val?) echo val2, vala, valz ;;
	val*) echo val11, val, valfoo ;;
	[1-9]val) echo 1val, 2val, ..., 9val ;;
	*) echo none of the above ;;
	esac
	```

while :  
*	```bash
	while ...
	do
		...
	done
	```

until : while command returns false
*	```bash
	until COMMAND
	```

For:
```bash
# ARR is any array, e.g. $@
for J in ARR 
do
    ...
	# $J is a parameter here
done
for ((i=0; i<10; i++)); do {} done
```

### FUNCTIONS
Actually a sequence of commands.  

`FUNCTION () {}` : declare  
`function FUNCTION {}` : declare  

`return EXPR` : return  
`$N` : **arguments** - argument number `N`, from `1` 
*	note: covers script args, so not accessible anymore thru `$N`

`FUNCTION [ARG1 ARG2 ...]` : call  

