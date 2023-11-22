# OBJECTS  
  
  
## README.md  
*	[README.md](./README.md)  

  
## I/O   
`alert(string)` : browser alert msg  
  
## BASE DATA TYPES

## CONVERSION   
`int parseInt(str)` : str to int  
`int parseInt(str, int radix)` : str to int, in base radix  

### Array   
`ARRAY.PROP` :  

`length` :   
`bool every(function)` : return true if each value evaluates function to true;  
`filter(function)` : keep elements such that function(x) = true;  
`forEach(function)` : applies function to each element;  
`from(arr)` : copy an array-like/iterable  
*	note: shallow copy

`join(sep)` : join using sep  
`indexOf(item)` : index of item  
`array map(function)` : return a copy with function(x) for each x;  
`type pop()` : remove and return last  
`undefined .push(VAL)` : append to end  
`reduce(function)` : apply function on each element, passing result of previous iteration;  
`type .shift()` : remove and return first  
`array slice(start, end)` : return from start to end (excluded)  
`bool some(function)` : true if at least one value evaluates function to true;  
`sort(function)` : sort using function;  
*	`function(a,b)` : returns 0 if equal, a negative value if first args less than second, otherwise positive

`splice(pos, n, subst)` : remove n elements at pos, add subst’ elements at pos  
`undefined unshift(VAL)` : append to start   
  
### Object 
`prototype`	: access element of class;  
*	can add/ change class (prototype) parameters  
*	e.g. `CLASS_NAME.prototype.PARAMETER`  

`freeze(“VAR”)` : make object VAR immutable  
`hasOwnProperty(str): boolean` : if obj has property named str  

#### static
`entries(obj): array` : object to array of pairs `<key, val>`  


## EVENT
`event.*` : event object properties (in event handlers)  

`currentTarget` : (some difference from target)  
`target` : "calling element", as object (containing html attributes as fields)  
*	e.g.: `event.target.value` : value attribute of calling html tag  

## HTTP
`fetch('URL', init?) -> Promise` : http request  
*	e.g.: `init={method = GET}` : http method  
	*	response fields:
	*	`ok:boolean` : true if in [200;400[  
  
### REGEX / MATCHING   
`str str.match(regex)` : try to match, and return list of matched part(s) of string,  
	*			or null if not matched  
`str.replace(regex1, str2)` : replace regex1 matched part in str with str 2;  
		*				you can use, in str2, $n for indicating n-th element found  

`bool regex.test(str)` : test (match) a regex on a string, return bool  
  
### STRING   
`.length` :   
  
`indexof(char)` :   
`.join(sep)` :   
`.log(ARG1, …)` : print args to console  
`.prototype.trim()` : remove start/end whitespaces  
`split()` :   
`.substring(start, end)` :   
`.substr(start, length)` :   
  
`Date` :   
// day=1..31, month=0..11  

`Date()` :   
`Date(string)` :   
`Date(y, m, d)` :   
  
`Date object` :   
`getDay()` :   
`toLocaleString("locales":string, {formats}?)` : convert to locales time, use optional formats (types)  
*	e.g.: `formats={year:"numeric",month:"short"}`  

toLocaleDateString(..) : just like `toLocaleString()`, only using date and not time  

`toDateString()` :   
  
### Error
`message` : error msg  


## OTHER MODULES

### Json   
`JSON.*` :  

`string .stringify(obj)` : object to json string  
`string .stringify(obj, arg, n)` : with prettify, insert newline, using n lines  
`object .parse(str)` : string to json  
  
### Math
`Math.*` :  

`PI` :    
  
`abs()` :  
`cos()` :  
`float floor()` :   
`float max(...args)` : max arg  
`float random()` : [0,1] , 0 included, 1 excluded  
`sin()` :  
`sqrt()` :  


### ?
`obj.review(str)` : ?  
`obj.newProp(str)` : ?  