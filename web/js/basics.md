# BASICS  
  
## README.md  
*	[README.md](./README.md)  



## DATA TYPES   

### Basic types
// (with first letter uppercase)  
*	bigint  

`boolean` : =`true|false`  

`number` :   
`NaN` : “not a number”  
*		result of math operation with an undefined  

`null` :    
`object` : have properties (i.e. fields);  
	*			properties stored as strings;  

`string` :  
`string literal` : sequence 0+ chars, in “”;  
*	immutable;  
*	e.g. “letters”  
template literal : `${val}`	(with backstick)  
	*	replaced text with evaluation  
*	symbol  

`undefined` :   
*	`undefined` : (keyword) element of type undefined  
  
### Derived types  
#### multiple objects   
	**array**
	*	actually an object, ordered and indexed with numbers 0,1,...;  
	*	can store values of different types;  
	`*	var NAME = [val1, ..];	`	: array definition  
	`*	note` : mutable elements, even if const array  
	**Date**
	*	actually numbers, counted in secs, so you can perform math operations;  
	*	date from 1/1/1970;  

#### RegExp
*		regular expressions;  

=`/PATTERN/FLAGS`  
*	without quotes;  
*	can contain regex operators;  


## BROWSER OBJECTS HIERARCHY
`window` : main window  
*	position  
*	size  
*	other windows  
`navigator` : client properties  
*	name  
*	version number  
*	installed plug-ins  
*	cookies  
`location` : current doc URL  
`history` : URLs accessed in navigation  

## EVENTS
// e.g. `onClick`, `onMouseHover`...  
can be assigned an event-handler function, like:  
```js
eventHandler(event) {
	...
}
...
<Button onClick="eventHandler"/>
```
where the event parameter is passed automatically.  

## SHORTHAND CHARACTER CLASSES 
// \c	: shortcut, with c lowercase  
// \C	: match all except …, with C uppercase  

`\d	= [0-9]` : digits  
\s	= [ \r\t\f\n\v] whitespace, carriage return, tab, form feed, new line  
`\w	= [A-Za-z0-9_]` : alphanumeric  
`FLAGS` : add options  
`i` : ignore case  
`g` : global: return all matches  
`singleton types` :   
// can’t be instantiated  
// there exist just one of it: Math, JSON …  

`Math` :   
  
`JSON` : json is a string; can easily be converted in a js object;  
*		differences with simple object:  
*	keys are strings, so betweed “quotes”,  
*	in js, being a string, is all in “quotes”,  
*	being a string, no function calls inside (i.e. need to substitute its value),  
*	only “double” quotes, not ‘single’,  
no comments: convention: “_*” is a comment (st starting with underscore _)  
  
## PROMISES
// when task completed, “you can fulfill promise or not”;  
// (usually asynchronous)  
// a promise has 3 states:  

`pending` : since when created  
`fulfilled` : with resolve  
`rejected` : with reject  

