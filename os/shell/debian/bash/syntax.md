# SYNTAX

## VARIABLES
`$VAR` : variable val  
`VAR=VAL` : create/assign  
*	note: no spaces important  

`local VAR=VAL` : local to function  

## VALUES
`"STRING"|'STRING'` :  
`NUM` :  
  
## OPERATORS
`;` : end line  
`{}` : separate code blocks (like c)
*	e.g.: `${VAR}` : is valid, equal to `$VAR`

`(EXPR)` : evaluate expression  

`` `EXPR` `` : evaluate expr before executing command  
`'STRING'` : literal string  
`"EXPR"` : string, which allows `${}` evaluation inside  

### BOOL
`[ EXPR ]` : evaluate expressions with `-OP` operators  
*	note: spaces important

`((EXPR))` : evaluate expressions with "normal" operators  
`! CONDITION` : not  
*	`CONDITION=((EXPR))|[ EXPR ]` :  

`||` :  
`&&` :  

### COMPARE
`-OP` :  
`le|ne|ge` : 

`e PATH` : file exists  
`r|w|x PATH` : file has r|w|x access  	
`s PATH` : file not empty  

`==` :  
`! A == B` : `!=`  

### MATH
`%` :  

## ARGUMENTS  
`$N` : argument N  
`$#` : arguments len  
`$@` : array of arguments  
`$*` : stringify argv, with spaces between (`"$1 $2 ..."`)

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
```bash
case VAR in
	OPT1) ...;;
	OPT2) ...;;
esac
```

while :  
```bash
while ...
do
	...
done
```

For:
```bash
for J in ARR 
do
    ...
done
```

### FUNCTIONS

Declare:
```bash
FUNCTION () {
	...
}

function FUNCTION {

}
```

Return:
```bash
return EXPR
```

`$...` : **arguments** - same as script  

Call:  
```bash
FUNCTION
FUNCTION ARG1 ARG2 ...
```