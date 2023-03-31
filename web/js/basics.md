# BASICS  
  
SYNTAX :   
MISC :   
; 	: at end of statement (not mandatory)  
\	: escape char  
	escapable chars:  
		\’	:   
		\”	:   
		\\	:   
		\n	:   
		\t	:   
		\r	: carriage return  
		\b	: word boundary  
		\f	: form feed  
‘’, “”	: for strings, it’s the same  
case sensitive  
  
VARIABLES :   
when declaration (not	definition)	: type=undefined  
var VAR_NAME;	: declare a variable (i.e. in memory);  
			VAR_NAME can be modified / reassigned;  
let VAR_NAME;	: declare a single instance of a variable, with a name;  
			i.e. its value doesn’t change.  
VAR_NAME can be modified / reassigned, but throws error;  
const VAR_NAME	: (read-only)  
			VAR_NAME can’t be reassigned;  
(but still mutable, can be modified);  
VAR_NAME = …;	: (without declaration) define a global var  
chars allowed for VAR_NAME : letters | num | $ | _  
var|let|const OBJECT = {  
	property1: val1,	// non-string properties are converted (typecasted) to strings by JS  
	“property 2”: val2	// needed when there are spaces in the name  
};  
  
ASSIGNMENTS :   
// c-like (rvalue = by value)  
VAR=		:   
VAR++		:   
{VAR1,...}=obj		: (destructuring assignment) assign obj’s elements to VAR1, …  
{PAR1:VAR1,...}=obj	: (destructuring assignment)  
choose which obj’s parameter assign to each var  
[VAR1,..,VARK]=arr	: (array destructuring) (with k <= arr.length)  
			assign VAR i the i-th element of arr  
[VARS, …ARR]=arr	: (e.g.) destructuring via rest: assign elements to VARS,  
and remaining to ARR  
[VAR1, ,VARK]=arr	: (array destructuring) (with k <= arr.length)  
			skip positions with commas  
// automatic casting :   
	e.g. int n = 2; string s = n;	// n casted to string  
  
STATEMENTS :   
if(...) {...} else if(...) {...} else {...}	:   
switch(...) { case …: … case …: … default: …}	:   
		compared with strict equality (===);  
		(c-like) execution continues, without break;  
while() {...}		:   
do {..} while(..)	:   
for(..;..;..)		:   
for(var in obj)		: iterate on object’s elements  
var FUNCTION_NAME = function() {...}	: //  
var FUNCTION_NAME = () => {...}		: anonymous function declaration  
var FUNCTION_NAME = () => RET_VAL	: anonymous function declaration,  
which only returns a value  
var FUN_NAME	= ARG => RET_VAL	: anonymous function,  
with only one argument,  
and which only returns a value  
var FUN_NAME = (ARG1…) => ({  
ARG1:ARG1  
…  
})						: create object with parameter named ARG1 with assigned value ARG1  
var FUN_NAME = (ARG1…) => ({  
ARG1  
…  
})						: (ES6) same as above (syntactic sugar)  
var object = {  
	FUN_NAME:function() {...}  
}  
var object = {  
	FUN_NAME() {...}  
}  
return		:   
		(no return) : type undefined  
  
KEYWORDS :   
class CLASS {  
	constructor(...) {  
this.VAR = VAL;	: class field declaration  
…  
}  
get GETTER(...) {...}	: getter: for getting a private var  
set SETTER(...) {...}	: setter: for setting a private var  
}				: class declaration;  
				(ES6) default if constructor not present:  
exists empty constructor;  
new CLASS(...)	: class instantiation  
this.PARAMETER	: class field  
// note : js is prototype-based : class definition can be modified (with prototype)  
// note : no private class fields ! can be accessed  
closure : scope of function in which variable created  
	note : allows creating private fields  
function() {  
	this.VAR = VAL;	// can be accessed from outside  
var VAR = VAL;	// private: can be accessed, but can’t modify this instance  
}  
  
function FUNCTION(ARG0, …) {...}		: function declaration, with args  
function FUN(ARG0=VAL0, …) {...}		: function declaration, with default arg(s)  
function FUNCTION(...ARGS) {...}		: function with undefined number of args,  
						collected as an array ARGS  
						(rest parameter)  
function FUNCTION({ARGS}) {...}		: function declaration with destructuring  
function FUNCTION({PAR1,..}) {...}		: function declaration with destructuring,  
taking parameters from an object, and using as names the parameter names  
default parameters :   
function FUNCTION(arg1, …) {  
	arg = arg || “dflt-value”;  
	// if (arg === undefined) arg = “dflt-value”;  
	…  
}  
IIFE : immediately invoked function expression  
var VAR = (function() {...}) ()	: var is the result of an anonymous function,  
which was only created to be called once (and is called once, now)  
e.g.  
var people = (function() {  
var persone = [] ;  
return {  
add: function(p) { persone.push(p)},  
lista: function(){ return persone.join(', ') }  
}  
}) ()  
// function, and var persone, can still be accessed by add and lista  
  
// function call : if without parameters (but required), it has undefined parameters  
export {VAR1, …}				: export var(s)  
export default VAR				: make as default/fallback export value  
export default DECLARATION		:   
import {VAR1, …} from “FILE_PATH”	: import var(s) from (local) file;  
					for local file, path relative to this file path  
import * as MODULE from “FILE_PATH”	: import all as MODULE from …;  
import VAR from “FILE__PATH”		: import default export as VAR  
  
OPERATORS :   
%	: remainder;  
	different from modulus: behaves differently with <0 numbers;  
**	: exponent  
+	: (for strings) concatenation  
a?b:c	: conditional operator / ternary operator  
[]	: (bracket notation)  
access at string   
access at array  
VAR?	: (null coalescing operator) evaluate only if var exists  
	e.g. obj?.method() : only evaluates obj.method() if obj defined  
arr[i, j, ..]	: access (multi-dimensional) array  
obj[“prop”]	: access object’s property (as string);  
		it can be any expression, returning a string (or it’s typecasted later);  
		add a property if not present;  
obj.prop	: access object’s property;  
		add a property if not present;  
class.getter		: use class’ getter  
class.setter=val	: use class’ setter  
module.obj	: use module’s element  
…arr		: (spread operator) unpacks array’s elements;  
		(only in specific contexts, like in function call)  
(TYPE VAR)	: typecast var to type  
delete obj.prop	: remove obj’s property  
typeof EXPR	: type of   
		e.g. number | string | …  
comparison :   
// if different types, first performs conversions  
	e.g. string “num” -> int num  
==		: equality  
!=		: inequality  
>|<		: greater|less than  
[>|<]=		: greater|less than or equal  
===		: strict equality;  
	don’t convert, but return false, with different types;  
!==		: strict inequality  
regex : see below  
  
operators - comparison - casting :   
falsy values : // evaluated to false  
false, 0, null, undefined, “”, Nan  
truthy values :   
all others  
note : comparisons made with casting, but return is not just True/ False, but the effective value that “won”  
	e.g. var || “10” : returns var if is not a falsy, else “10”  
  
COMMENTS :   
//  
/* */  
  
MISC :   
camelCase		: first letter: lowercase; first letters inner words: uppercase;  
			(best practice) for var names (mutable);  
UpperCamelCase	:   
			(best practice) for class names  
UPPERCASE		:   
			(best practice) for const var names;  
  
DATA TYPES :   
// (with first letter uppercase)  
bigint  
boolean	:   
		=true | false  
number	:   
NaN	: “not a number”  
	result of math operation with an undefined  
null  
object		: have properties (i.e. fields);  
		properties stored as strings;  
string		:  
string literal : sequence 0+ chars, in “”;  
	immutable;  
e.g. “letters”  
template literal : `${val}`	(with backstick)  
		replaced text with evaluation  
symbol  
undefined	:   
		undefined (keyword)	: element of type undefined  
  
DERIVED TYPES :   
multiple objects :   
array		: actually an object, ordered and indexed with numbers 0,1,...;  
can store values of different types;  
	var NAME = [val1, ..];		: array definition  
	note : mutable elements, even if const array  
Date		: actually numbers, counted in secs,  
		so you can perform math operations;  
		date from 1/1/1970;  
RegExp	: regular expressions  
		=/pattern/flags  
without quotes;  
can contain regex operators;  
SYNTAX :   
.	: (wildcard / dot / period) match anything  
|	: (alternation / OR operator)  
[^chars] : (negated character sets)  
exclude all following chars  
^chars	: (caret character) only matches chars at beginning of string  
chars$	: only matches chars at end of string  
c+	: match all consecutive chars equal to c, together (at least 1)  
c*	: // (at least 0)  
c*?	: lazy match : match least possible  
	default = greedy match : match greatest possible  
c?	: there can be or not  
[chars]	: (character class) match anything specified inside  
[c1-c2]	: (hyphen) range, with numbers, letters  
c{n,m}	: (quantity specifier)  
match when c occurs between n and m times (included)  
c{n}	: exactly n occurrences  
c{,n}	: max n occurrences  
c{n,}	: min n occurrences  
(?=chars) : (positive lookahead) match if find chars ahead  
(?!chars) : (negative lookahead) match if not find chars ahead  
()	: parentheses  
(chars)	: (capture group) can be referred to later;  
	they’re saved like variables in regex;  
\n	: reference to a capture group, numbered (n) with the order of open parentheses;  
	i.e. first one = 1;  
$n	: (in .replace()) matched n-th element  
SHORTHAND CHARACTER CLASSES :   
// \c	: shortcut, with c lowercase  
// \C	: match all except …, with C uppercase  
\d	= [0-9] : digits  
\s	= [ \r\t\f\n\v] whitespace, carriage return, tab, form feed, new line  
\w	= [A-Za-z0-9_] : alphanumeric  
FLAGS : add options  
i	: ignore case  
g	: global: return all matches  
singleton types :   
// can’t be instantiated  
// there exist just one of it: Math, JSON …  
Math	:   
  
JSON	: json is a string; can easily be converted in a js object;  
	differences with simple object:  
keys are strings, so betweed “quotes”,  
in js, being a string, is all in “quotes”,  
being a string, no function calls inside (i.e. need to substitute its value),  
only “double” quotes, not ‘single’,  
no comments: convention: “_*” is a comment (st starting with underscore _)  
  
PROMISE :   
// when task completed, “you can fulfill promise or not”;  
// (usually asynchronous)  
// a promise has 3 states:  
pending	: since when created  
fulfilled		: with resolve  
rejected	: with reject  
Promise((resolve, reject) => {...})	: constructor, takes a function  
resolve(expr)	: used to declare success, passing as argument any expression/object…  
reject(expr)	: used to declare unsuccess, //  
myPromise.catch(error =>{...})	: executed if unsuccess (after reject called);  
					error = reject’s arg  
myPromise.then(result => {...})	: executed if success (after resolve called);  
					result = resolve’s arg  
