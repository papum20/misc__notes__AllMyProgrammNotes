# OBJECTS  
  
CONVERSION :   
int parseInt(str)		: str to int  
int parseInt(str, int radix)	: str to int, in base radix  
  
document :   
.createElement(elementType)  
.createTextNode(string)  
.getElementById(“id”)	:   
.getElementsByName(“id”)	: if has name attribute  
.getElementsByTagName(“id”) :   
.getElementsByClassName(“id”) :  
.querySelector(selector)	: css selector  
.querySelectorAll(selector)	:  css selector  
.write(string)			:   
  
DOCUMENT ELEMENTS :   
.<attribute>	: access any html attribute  
.innerHTML	: content (excluding tags), i.e. including children  
.outerHTML	:content, i.e. including children, including tags  
.innerTEXT	: content text (excluding tags)  
.outerTEXT	: text, including tags  
  
.appendChild(element)  
.removeAttribute(“attr”)  
.setAttribute(“attr”)  
  
history :   
.current  
.length  
.next  
  
.back()  
.forward()  
.go(int)  
  
window :   
.location  
.location.href  
function .onclick	: mouse  
function .onkeypress	: keyboard  
  
.moveBy(x,y)  
.moveTo(x,y)  
.onload=function	: function executed when document fully loaded  
.open(URLname, WindowName,[opt]) : open new window  
.resizeBy(x,y)  
.resizeTo(x,y)  
  
I/O :   
alert(string)	: browser alert msg  
  
(ANY) OBJECTS :   
Object.freeze(“VAR”)	: make object VAR immutable  
obj.review(str)		: ?  
obj.newProp(str)	: ?  
  
ARRAY :   
.length	:   
bool .every(function)	: return true if each value evaluates function to true;  
.filter(function)	: keep elements such that function(x) = true;  
.forEach(function)	: applies function to each element;  
.join(sep)		: join using sep  
.indexOf(item)	: index of item  
array .map(function)	: return a copy with function(x) for each x;  
type .pop()		: remove and return last  
undefined .push(VAL)	 : append to end  
.reduce(function)	: apply function on each element, passing result of previous iteration;  
type .shift()		: remove and return first  
array .slice(start, end) : return from start to end (excluded)  
bool .some(function)	: true if at least one value evaluates function to true;  
.sort(function)		: sort using function;  
			function returns 1 / -1;  
.splice(pos, n, subst)	: remove n elements at pos, add subst’ elements at pos  
undefined .unshift(VAL) : append to start   
  
OBJECT :   
CLASS_NAME.prototype	: access element of class;  
				can add/ change class (prototype) parameters  
e.g. CLASS_NAME.prototype.PARAMETER  
boolean .hasOwnProperty(str)	: if obj has property named str  
  
REGEX / MATCHING :   
str str.match(regex)	: try to match, and return list of matched part(s) of string,  
or null if not matched  
str.replace(regex1, str2)	: replace regex1 matched part in str with str 2;  
			you can use, in str2, $n for indicating n-th element found  
bool regex.test(str)	: test (match) a regex on a string, return bool  
  
STRING :   
.length	:   
  
indexof(char)		:   
.join(sep)		:   
.log(ARG1, …)	: print args to console  
.prototype.trim()	: remove start/end whitespaces  
split()			:   
.substring(start, end)	:   
.substr(start, length)	:   
  
Date :   
// day=1..31, month=0..11  
Date()  
Date(y, m, d)  
  
Date object :   
.getDay()		:   
.toLocaleDateString()	:   
.toDateString()		:   
  
JSON :   
string .stringify(obj)	: object to json string  
string .stringify(obj, arg, n) : with prettify, insert newline, using n lines  
object .parse(str)	: string to json  
  
Math :   
.PI  
  
.abs()  
.cos()  
float .floor()		:   
float .max(...args)	: max arg  
float .random()	: [0,1] , 0 included, 1 excluded  
.sin()  
.sqrt()  
  
MODULES :   
  
  


## BROWSER OBJECTS

window : main window  
position  
size  
other windows  
navigator : client properties  
name  
version number  
installed plug-ins  
cookies  
location : current doc URL  
history : URLs accessed in navigation  
