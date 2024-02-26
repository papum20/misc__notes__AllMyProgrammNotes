# OBJECTS  
  
  
## README.md  
*	[README.md](./README.md)  

  
## I/O   
`alert(string)` : browser alert msg  
  
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
`fromEntries(ARR)` : object from array of arrays, each containing the pair of key and val (val optional)  
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


## DOM

### document
The HTML DOM Document Object is the owner of all other objects in your web page.   
`document` : the object of the following attrs/methods   

#### Finding HTML Elements
`getElementById(ID)` :  
`getElementsByClassName(NAME)` :  
`getElementsByTagName(NAME)` :  

#### Adding and Deleting Elements
`appendChild(ELEM)` :  
`createElement(ELEM)` : create an HTML element  
`removeChild(ELEM)` :  
`replaceChild(NEW, OLD)` :  
`write(TEXT)` : Write into an HTML output stream opened with open  

#### Adding Events Handlers
`getElementById(id).onclick = function(){code}` : Adding event handler code to an onclick event  

#### Finding HTML Objects
`anchors` : Returns all `<a>` elements that have a name attribute  
`applets` : Deprecated  
`baseURI` : Returns the absolute base URI of the document  
`body` : Returns the `<body>` element  
`cookie` : Returns the document's cookie  
`doctype` : Returns the document's doctype  
`documentElement` : Returns the `<html>` element  
`documentMode` : Returns the mode used by the browser  
`documentURI` : Returns the URI of the document  
`domain` : Returns the domain name of the document server  
`domConfig` : Obsolete  
`embeds` : Returns all `<embed>` elements  
`forms` : Returns all `<form>` elements  
`head` : Returns the `<head>` element  
`images` : Returns all `<img>` elements  
`implementation` : Returns the DOM implementation  
`inputEncoding` : Returns the document's encoding (character set)  
`lastModified` : Returns the date and time the document was updated  
`links` : Returns all `<area>` and `<a>` elements that have a href attribute  
`readyState` : Returns the (loading) status of the document  
`referrer` : Returns the URI of the referrer (the linking document)  
`scripts` : Returns all `<script>` elements  
`strictErrorChecking` : Returns if error checking is enforced  
`title` : Returns the `<title>` element  
`URL` : Returns the complete URL of the document  

### element
`element` :  

#### Changing HTML Elements
`attribute = new value` : Change the attribute value of an HTML element  
`innerHTML =  new html content` : Change the inner HTML of an element  
`outerHTML = new html content` : Change the outer HTML of an element  
`setAttribute(attribute, value)` : Change the attribute value of an HTML element  
`style.property = new style` : Change the style of an HTML element  


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