# OBJECTS

## FUNCTIONS
`exit STATUS` :  

### ARGUMENTS
`getopts FLAG1:FLAG2:` : flags passed as arguments to command, via terminal  
*	`FLAG:` : (colon) means required arg
*	e.g.: `while getopts FLAG1:FLAG2: FLAG ...` : loop through
*	`OPTARG` : where stored arg value

`shift NUM` : shift start of `$@`  
*	e.g.: `shift 1` : on `some_cmd arg1 arg2` : makes `$1=arg2`  

