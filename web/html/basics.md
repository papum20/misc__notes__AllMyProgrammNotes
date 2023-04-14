# BASICS  
  
SYNTAX:  
end line		doesn’t matter inside element  
indentation			//  
attributes order in element	//  
  
<[tag]> : opening tag  
[tag’s element]  
</[tag]> : closing tag  
  
DEFINITIONS:  
attributes : <[tag] attr1=val1 attr2=val2> </[tag]>  
can’t use all chars:  
no uppercase  
dashes automatically convert following letter in uppercase, in dataset  
e.g. an-attribute -> anAttribute  
global attributes : defined for all elements  
generic elements : no default, added features (e.g. div, span)  
self-closing tags : only <[tag] …>  
  
inline elements : “don’t appear on new line” : take the width of their content  
block-level elements : “appears on new line” : take all parent’s width (stacked as blocks)  
  
fontstyle elements : add visual effects (e.g. bold)  
phrase elements : just text  
  
SEO : search engine optimization  
	some elements (e.g. title, description, help the browser find your site)  
  
note : adding an element in new line adds a space  
  
  
FEATURES:  
whitespaces : collapsed / kept  
  
HTML BOX MODEL:  
[margin					: distance from other objs  
(from obj to other obj’ border edge);  
		overlapping with near objects’ margins:  
the resulting margin is thus the biggest one;  
no color;  
		(if e.g. content has top-distance 0 from box border,  
content’s top-margin pushes outside box;  
solution1: add small (1px) top-padding to box  
solution2: overflow: hidden  
)  
[border					: border thickness  
[padding			: inner distance, container-content   
[content=width*height	: inner content size  
]  
]  
]  
]  
  
  
ELEMENTS:  
1) SPECIAL ELEMENTS:  
<[tag]>		: (i.e. global attributes)  
class=”val”	: class, to group  
		class=”val1 val2”	: multiple classes; order doesn’t count  
		id =”val”	: element id, unique in file  
			=”region” : requires aria-labelledby=”id” of description element  
		style=”...”	: (short) css style associated to single element  
				(using css syntax)  
		title=”...”	: secondary text associated to element,  
for accessibility, additional info…  
	(event attributes, associate specified script to an action on element/document) :  
		onclick		:   
		ondoubleclick	:   
		onkeypress		:   
		onmouseover	:   
(i18n attributes (internationalization), for multiple languages/alphabets) :  
		dir=”ltr|rtl”	: text secondary stream direction (left to right / right to left)  
lang=”text”	: (usually in html element) language  
	(interactivity attributes: how to render interactive element, for forms or accessibility) :  
		accesskey	: key to focus element  
		autofocus	: specified element is focused at startup  
		inputmode	: keyboard to visualize when element is focused  
		tabindex	: element reachable via tab, after n strokes  
	(custom attributes: can be used in Javascript, alternative to names) :  
		// “modal”  
	(WAI-ARIA specification:  
Web Accessibility Initiative - Accessible Rich Internet Applications;  
for accessibility) :  
		aria-hidden=”bool”	: hided for accessibility  
aria-labelledby=”id” : needed by attr role=..  
role=”...”	: specify role, for accessibility technologies;  
set to preset values  
		tabindex	: (see above)  
<!-- [comment] -->	:	comment  
<!DOCTYPE val>	: 	what the doc should be read like  
			e.g. <!DOCTYPE html>  
			using html	-> strict mode (faster)  
			not using html	-> quirk mode (few rules)  
  
2) STRUCTURE ELEMENTS:  
<address>	: 	(in footer) for contact info  
<article>	:	part which could be stand-alone,  
removed/(re-)inserted without any problems  
<aside>	: 	linked, bu unrelated / separate  
<body>	:	all rendered elements are in it  
<div>		:	(block) denotes common elements (its children);  
		no feature: used to personalize with css, and for structure  
<footer>	:	usually for final reference/documentation  
<h*>, *=1…6	:	(block) heading elements, indicate importance of their content;  
		one occurrence per page;  
		less important (...h6) below more (h1…)  
<head>	:	alternative to body: e.g. title for tab  
<header>	: 	first part in body  
<html>	:	main: all elements should be in it  
<link>		:	link document to other sources  
		href=”link”	:   
rel=”...”	: relationship  
		rel=”stylesheet”	: <style>  
<main> 	:	(html5) for readability  
<nav>		: 	section / list of links  
(e.g. homepage bar, with website sections links)  
<p>		:	(block) paragraph   
		whitespaces : collapsed  
<pre>		:	(block) pre-formatted  
		whitespaces : kept  
<section>	:	section  
  
3) HEAD:  
<legend>	:	fieldset title  
<meta>	:	(in head) additional info  
		charset	=”...”		: charset to use  
				=”UTF-8”	:   
		name=”viewport” content=”...” : some configs  
			e.g. content=”width=device-width, initial-scale=1”  
		name=”description” content=”...” : description for browser  
<script>	: link js script;  
		normally code executed when read, asynchronously,  
		i.e. browser reads document top->bottom, and stops for executing code;  
		defer		: execute js after html has loaded  
		type=”module” :   
src=”link”	: link to js  
<title>		: (in head) document’s title;  
		gives info to search engine;  
git’s displayed in title bar / browser tab when hovering  
  
4) TEXT ELEMENTS:  
<a>		:	(inline) anchor for links;  
		can’t nest in each other  
	href=”link”		: link (URI) start  
		=”#ID”		:   
	name=”...”		: link target  
	target	=”...”		: where to display link  
		=”_self”	: in same tab  
		=”_blank”	: new tab  
	title	=”str”		: legend when hover  
	text : <a href=”link”>[element]</a> : link’s text  
<b>		:	(inline) bold  
<br>		:	new line  
<em>		:	emphasize  
<i>		:	(inline) italicized  
<label>	:	(inline) around input, make its text trigger input  
		for	=”[id]”		: associate label’s text with element [id]  
<span>	:	no feature (like div)  
<strong>	:	bold  
  
5) LIST / TABLE ELEMENTS:  
<dd>		: 	<dl> element, definition data  
<dl>		:	definitions list  
<dt>		: 	<dl> element, definition term  
<li>		:	list item, in <ul>  
<ol>		:	ordered list (numbered elements)  
<ul>		:	unordered list (of elements) (i.e. order doesn’t change meaning)  
  
<table> 	:	table  
<caption>	: 	(in table, first element) description (accessibility)  
<td>		: 	(in tr) table data  
<th>		: 	(in table/thead) table header: col name (first row)  
<tr>		: 	(in table/body) table row  
		col=”..”		:   
		colgroup=”..”	:   
colspan=”..”	: n of rows occupied by cell  
rowspan=”..”	: n of cols occupied by cell  
<tbody>	: 	(in table) table body  
<tfoot>	: 	(in table)   
<thead>	: 	(in table) table headers  
  
6) INTERACTABLE ELEMENTS:  
<form>	:	(form’s widgets container)  
		action		=”link”	: where to send form output (server-side)  
		method	: HTTP method  
				=”get”		: get request via URL  
				=”post”	: post request  
form elements:  
<*>		:   
		name=”...”	: used by server-side app to identify received data  
<button>	:	(inline) (in form) button;  
		onclick=”...”		: function called on click  
			=”code	“	: js code   
		type	=”...”		:  
=”submit”	: (default) in form, by default  
sends input element to form’s action  
<datalist>	: 	(for input -> list)  
<input>	:	(self-closing) (inline) (in form)  collect data  
		checked		: checked by default  
		list=”LIST_ID”	: value must be in the associated <datalist>  
(with id=LIST_ID)  
min|max		: (with type=number)  
		minlength		=”[num]”  
name	=”val”		: identifier (needed to be used in figure->action);  
					need same name in radio inputs  
to make only select one  
pattern		: value must match pattern (regular expression)  
placeholder =”val”	: input placeholder value  
readonly		: non modifiable  
required		: input value is required in order to submit  
type	=”...”		: input type / expected input;  
			some types come with default validation  
	=”checkbox”	:   
=”color”	: shows color wheel to select one  
=”date|month|week|time” :  
browser shows a calendar/… where to select a date/…  
=”email”	: (default validation to valid email)  
		verify @ is present and domain is (syntactically) correct  
=”file”		: input file (defaults to browser’s values)  
=”number”	:   
=”password”	:   
	=”radio”	: multiple options  
	=”search”	: (?)  
=”submit”	: submits its nearest parent form element  
			=”text”	:    
			=”url”		: verify that follows URL specifications  
		value	=”...”		: value sent  
					(default) in radio: [name]=on  
<option>	: (in select, datalist) option for <select>;  
should have a value to submit, usually  
<select>	: (in form) dropdown select menu  
<textarea>	: (in form) multiline input  
cols		: 		  
rows		:   
placeholder	:   
  
7) EMBED:  
<audio>	:   
<embed>	: embed multimedial object  
<iframe> 	: embed html page in html page  
<img>		:	(self-closing) (inline) image  
		src=”link”	: image link  
		alt=”text”	: alternative value (if src not available)  
		height=”...”	: force image height (pixel)  
		width=”...”	: force image width (pixel)  
		notes :	in pixel bad idea, useful to pre-load (readjust later);  
			if not given, image is rendered at last;  
			only giving height is a good idea  
(1. proportions are kept, calculated; 2; height gives structure)  
		srcset=”..., …”	: alternative images, for different displays;  
		sizes=”..., …”		: sizes with which to use each element in srcset  
		note: svg images include a path, so allow resizing without loss of quality  
<object> 	: (old) generic (like div)  
<video>	:   
  
8) OTHER ELEMENTS:  
<fieldset>	:	group form elements and related labels  
<figure>	:	put around img, add info  
<figcaption>	:	in figure, add caption  
<hr>		:	(self-closing) line separator  
<style>	:	add style to elements  
		e.g. <style>[CSS-like styles/rules]</style>  
  
ENTITIES:  
// for writing reserved chars (used in syntax) / non present in 7 bit ASCII  
use (code):  
&CODE  
use (numerical entities) :  
&#...  
&#x…  
“A|a”acute  
Aelig AE  
Agrave  
agrave  
amp &  
auml (..)  
ccedil  
gt  
lt <  
nbsp (non-breaking space)  
ntilde  
quot  
reg  
  
MEASURES:  
COLORS:  
// 16 pre-defined, (256 in some browsers…)  
// suggested to only use in css  
use :  
## README.md  
*	[README.md](./README.md)  

#HEX : hexadecimal  
SIZES:  
// (same as css)  
px  
%  
multiple -sizes  


