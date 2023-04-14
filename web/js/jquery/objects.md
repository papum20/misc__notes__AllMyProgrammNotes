# OBJECTS    
    
// legend:   
el = some html element  
  
JS SYNTAX :   
$(“str”)	: select css style element (/ #id / .class …)  
	e.g. $(document) : all document  
SELECTORS (“str” arg) :   
.CLASS:nth-child(N)	: select all elements of class CLASS that are nth children (param N)  
(start from 1)  
.CLASS:even		: select all elements of class CLASS that are children in even position  
(start from 0)  
.CLASS.odd		: select all elements of class CLASS that are children in odd position  
			(start from 0)  
  
JS FUNCTIONS :   
$(document).ready( … )	: when document is ready, apply code (functions) defined inside  
  
el.addClass(str)	: add class(es) to el  
el.appendTo(str)	: move el from current parent to new parent str  
el.children()		: access children (all)  
el.clone()		: create a copy  
	e.g. el.clone().appendTo()	: copy to new parent  
el.css(property, val)	: change el’s css property  
	e.g. el.css(“color”, “blue”);  
el.html(“str”)		: replace element with str;  
			e.g. str= <tag attrs=...>text</tag>  
el.parent()		: access parent element  
el.prop(property, val)	: change html property  
	e.g. $(“button”).property(“disabled”, true);	: disable button,  
i.e. grayed out and not selectable  
el.remove()		: remove html el  
el.removeClass(str)	: remove class(es)  
el.text(“str”)		: replace el’s text with str  

## README.md  
*	[README.md](./README.md)  

