# SYNTAX

## DELIMITERS
format, depending on where (different commands, languages, ...)  
`REGEX` :  
`/REGEX/` :  
*	e.g.: `sed` :  

`{REGEX}` :  

## SPECIAL CHARS

`^` : start of expression  
`$` : end of expression  
`REGEX*` : REGEX repeated 0+ times  
`REGEX+` : REGEX repeated 1+ times  
`REGEX?` : REGEX repeated 0/1 times  
`.` : any single character (excluding `\n`)  
`\` : escape char  

## PARENTHESES
`(REGEX)` : **atom** - contains REGEX  
`REGEX{NUM}` : **bound** - REGEX repeated NUM times  
`REGEX{N1,N2}` : **bound** - REGEX repeated between N1/N2 times  
*	if N1/N2 missing, means any (start/end)  

`[LIST]` : **bracket expression** - any char in list  
`[^LIST]` : any char not in list  
`[A-B]` : any char in range [A;B]  
`[:CCLASS:]` : **character class** -  
*	e.g.: `[:alnum:]`  

## OLD REGEX
// obsolete  

### DIFFERENCES
many chars not reserved, so need to "escape" to use their function:  
*	`(){}|?+` : are normal chars  
*	`\(\)\{\}` : for `(){}`
*	`^$` : start/end of expression if at beginning/end of regex, else normal char
*	`*` : normal char if at beginning of regex/subexpression `()`  