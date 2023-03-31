# BASICS  
  
SYNTAX :  
MISC :  
; at end of line  
// comment  
# comment  
/* multiline comment */  
  
KEYWORDS :   
return	:   
TRUE  
FALSE  
  
OPERATORS :   
===	: compare  
+ 	: string concatenation  
.	: string concatenation  
+ 	: array joining  
[]	: access array index  
&&	: and  
  
STATEMENTS :   
if ( ) { }	:  
foreach (iterable as iterator) {...}	:   
  
VARIABLES :   
$var = val;	: declare and assign variable var  
$var		: use value of var  
$arr = (el1, …)		: (ordered array) array declaration, with default indexes = 0,1,...  
$arr = (ind1 => el1, …) : (associative array) array declaration, with specified indexes  
$arr = [...]		: array declaration (same)  
$arr[ind]		: access array at index  
$arr[] = val		: add val at last index of array  
$var = $arr		: pass (assign ts value) array by value (i.e. returns a copy)  
$var = & $arr		: pass (assign its value) array by reference  
  
TYPES :  
array :  
ordered  
indexed with keys  
allows multiple types (for keys and values)  
bool :   
string :  
= ‘...’	: (single quotes) string literal  
= “...”	: (double quotes) string literal with evaluation  
	e.g.	“$var” = <value of var>  
		‘$var’ = $var  
