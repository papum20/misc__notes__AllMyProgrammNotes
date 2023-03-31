# BASICS  
  
SYNTAX:  
/* comment */  
  
element(s) {			: type selector(s)  
	property: value;  
	property: value !important;	: property is never overwritten by later rules  
}  
element1 element2 {...}	: type selector for any element2 in element1  
element1 > element2 {...}	: type selector for any element2 direct child of element1  
.class-name {...}		: class selector  
.class-name element {...}	: select element nested in class  
.class e1, .class e2 {...}	: multiple //  
elem.class	{...}		: elements of type elem, with class as one of their classes;  
				i.e. they can also have other classes  
*				: (generic selector)  
multiple type selectors : (comma-separated) e1, e2, … {...}  
pseudo-type selectors :  
// <sel> stands for <selector>  
a			{...}	: (for links not visited yet)  
<selector1> + <selector2>	: first occurrence of 2 after 1  
<selector1> ~ <selector2>	: all sibling occurrences of 2 after 1  
<sel>:active|checked|enabled|hover  
<tag>:first-child|letter|letter  
<tag>:first-of-type	{...}	: first occurrence of type tag  
<tag>:last-of-type	{...}	: last occurrence  
<tag>:not(rule)	{...}	: all except  
	e.g.	not(.class-name)  
		not(#id) : exclude elements with id  
<sel>:nth-child(n)		: nth child  
<sel>:nth-child(odd|even)	: all odd or even children  
type[attribute]		{...}	: all type elements with an attribute attribute set (any value)  
type[attribute=”val”]	{...}	: attribute selector  
<sel>[attr^=”val”]		: starts with val  
<sel>[attr*=”val”]		: match any *val*  
<sel>[attr~=”val”]		: match any * val *  
(i.e. matches whole word val, with separators before and after)  
#id			{...}	: id selector  
pseudo-elements :   
<tag>::after		{...}	: create an element which is last child  
<tag>::before		{...}	: create an element which is first child  
  
all values :   
=inherit	: (default for all elements/properties)  
		inherits container’s val  
=unset		: unsets set values  
numerical values :   
// syntax: =[val][UNIT]  
UNITS :  
percent :   
%	: % of parent  
lengths :  
absolute :  
deg	: degrees  
cm | mm | in :   
pc	: pica  
pt	: point  
px  
relative :  
ch	: 0 width  
em	: percentage [0,1] of element’s font size  
ex	: x height (with current font)  
fr	: (flex unit) fraction of remaining space of container  
lh	: row height  
rem	: root em; percentage [0,1] of font size of html element  
vh|vw	: viewport height/width: val% of viewport height/width  
vmin|vmax	: min/max between vh/vw  
functions :   
=max(val1, val2)	:  	  
=min(val1, val2)	:   
=SIZE1,SIZE2,...	: (?) multiple sizes  
=SIZE1,*,*		: sizes for * are equally divided, once removed fixed ones  
color values :    
=rgb(int, int, int);  
=rgba(int, int, int, float|%)	: adds alpha channel (0-1.0|%)  
=[constant];		: color constant  
=#hexadecimal;  
=#hexadecimal-alpha	: add 2 digits for alpha  
=hsl(int, int%, int%);	: HSL (hue, saturation, lightness) color model;  
		hue=0...360 (color wheel degrees, 0=top=red)  
		saturation=0…100  
		lightness=0…100  
hsla(...)		: add alpha  
=linear-gradient(direction=180deg, color1 [color-stop1], color2 [color-stop2]…)	:  
actually an image (so use it with background);  
linear gradient (distributes colors evenly) between (min. 2) colors,  
in any format: default stops (3 colors-> 0,50,100%);  
optional color-stop for each color: number (px/%/…)  
indicating the point of the full element where it stops  
  
CASCADE ORDER:  
declaration are considered in this order (last is more important, overwrites upper ones)  
user-agent  
user  
author’s normal (declarations)  
author’s important (!important)  
user’s imortant (!important)  
also, wins the most specific;  
then wins document order;  
  
STYLES:  
ANIMATIONS :   
// animations go from start to end state, linearly  
animation-...  
name			: name  
duration		: duration  
iteration-count	: n of iterations  
fill			: ?  
delay			: delay between iterations  
  
COLORS:  
background-color	: (default=transparent)  
			=color  
background-image	: “link”;  
			=url(link);  
border-color		: (default black)  
color			: (also for a) content color (including text)  
			(default) for links: blue if not clicked yet, purple if clicked  
			=color  
filter			: filter  
			filters of boxes/contents sum  
			=blur(px) : blur  
opacity		: non-transparency, 0->1.0 / 0%->100%  
  
DIMENSIONS/POSITION:  
border			:   
			=length type color  
border-left-width	:   
display		:   
=block		: stacked vertically  
=contents	: contents exist, container not  
=flex		: make element a flex container,  
and its children flex items;  
	flexbox is a one-dimensional layout  
=float		: (?) moved to left/right edge of container, then other siblings float around it  
=grid  
=inline		: stacked horizontally  
=list-item  
=none  
=table  
=table-cell  
=table-row  
(controls how items are spaced out/aligned within container)			  
=grid  
=inline		: inline, takes content’s dimensions  
=inline-block	: inline, has its own dimensions  
=list-item  
=none		: hide  
=table  
=table-row|cell  
margin		: margin area (can implicate scrolling page horizontally/vertically)  
			=length  
			= val1 val2 : top/bottom=val1, left/right=val2  
margin-left		:   
			=auto  
margin-right		:   
max-width		:   
padding		: border in element, around content - pads in all directions  
			(default for input you can type in: 1px 2px)  
=length  
= val1 val2 : top/bottom=val1, left/right=val2  
padding-*		* = left|right|top|bottom  
position		: position of container with respect to stream  
			=absolute	: position where specified;  
					in case can hide other elements in same position  
			=fixed		: absolute with respect to viewport,  
					i.e. doesn’t scroll  
			=relative	: moved by a variation from its position  
			=static		: position it would normally have in the stream  
=sticky	: static, but when scrolling fixed, until its position disappears from viewport, in which case it disappears immediately  
top|right|bottom|left	: absolute position of top|... side  
height			: (also for hr) element’s content height, excluding border height  
(=1 up, 1 down)  
width			: (num)  
z-index		: overlapping / 3d plan,  
			default=last one is placed on other  
			=n	: absolute number, no unit, represents payer  
  
ELEMENTS:  
aspect-ratio		=val1 / val2 : aspect ratio  
border			: (default to none) to be visible, must be set width and style  
border-left		= width style color;  
border-left-style	:   
			=solid		: full  
			=double	: double  
border-radius		=tl tr br bl;	//(px), corners  
smooth borders (corners)   
box-shadow		: offset=any num; >0: right/up;  
blurRadius=any num; blurRadius>0 makes less sharp edges;  
			height/width determined by element,  
but can use spreadRadius to spread  
=h-distance v-distance color  
= offsetX offsetY [blurRadius=0] [spreadRadius=0] color;  
box-sizing		:   
			=border-box  
clip-path		: specify clip path -> everything inside is visible, outside not  
			=inset(n%)	: inside of %  
column-gap		:   
column-rule		:   
column-width|height :   
gap			: (for layouts, i.e. grid, flex, …) set gap between container’s items  
			=val :   
			=val1 val2 : (row, col)  
list-style		: (for a list) styles for list elements  
object-fit	 	: (for img) how content should behave regarding box (e.g. proportions)  
			=cover : keep proportions, make sure to cover all element’s box  
				i.e. can be bigger in one dimension  
overflow		: behavior of content overflowing container  
			=hidden 	: overflowing content is hidden  
don’t push content’s margin beyond box border (overflow inside)  
=scroll		: there’s a scrollbar,  
		which takes up content space;  
		smartphone: no bar (you use fingers)  
=visible	: container expands to contain all content  
overflow-x|y		:   
  
FLEX :   
flex-direction		: flex direction  
			=row|row-reverse|column|column-reverse  
flex-grow		:   
flex-shrink		:   
flex-wrap		: how items behave, when container too small  
			=nowrap  
			=unwrap : (default) don’t wrap, shrink if needed  
=wrap : wrap to next row/col   
justify-content	: (in flex) how items are positioned along main axis  
(pos, space around)  
=center  
=space-between : first to the extreme left, last to end, and then subdivide and assign space in between  
=space-evenly :   
order			:   
  
GRID :   
grid-area		: (child of grid)  
			= an element of parent’s grid-template-areas;  
			i.e. selects a space in the declared grid;  
grid-template-areas	: (container with display=grid)  
			=”row1col1 row1col2…” “row2col1…” …;  
grid-template-columns : (container with display=grid)  
grid-template-rows	: (container with display=grid)  
			rows dimensions  
  
EVENTS:  
// e.g. ::hover  
cursor			: set cursor type  
  
MISC:  
align-items		: (for flex) position items along cross axis (not main axis)  
			=center|flex-end  
scroll-behavior	: scroll behavior  
			=smooth  
  
TEXT:  
font-family		: font type;  
			use“quotes” for complex names (i.e. made of more words);  
order=priority (if first font not found, then 2nd, …)   
			(there exist some common to most browsers)  
			font-family: [font1], [font2];	:  
fallback font (alternative when first not found)  
			e.g.: sans-serif  
font-kerning		: text alignment  
			=normal|none  
font-size		: lunghezza | percent  
font-stretch		:   
			=normal|wider|narrower  
font-style		:   
			=italic|normal|oblique  
font-variant		: font variant  
			=normal|small-caps  
font-weight		: bolder  
			=bold|normal|100|200|...|900  
letter-spacing	: letter spacing  
			=length  
line-height		: line height  
			=length  
text-align		: text alignment  
			=left|center|right|justified  
text-align-last		:   
			=left|center|right|justified  
text-decoration	: e.g. underlined  
			=none|underline|overline|line-through  
text-indent		: indentation  
			=length  
text-shadow		:   
			=h-distance v-distance color  
text-transform	:   
			=capitalize|uppercase|lowercase|none  
white-space		:   
			=normal|pre|nowrap  
word-spacing		:   
			=length  
  
TRANSFORMATIONS :   
// applied to already created element (i.e. not readapted, e.g. can be stretched)  
transform:...   
rotate(deg) : clockwise  
rotate3d()  
scale()  
scale3d()  
skew()  
translate()  
translate3d()  
  
AT-RULES:  
// for contexts / meta-rules  
@keyframes	: describes initial, intermediate and final states of an animation  
@keyframe ANIMATION-NAME {  
	from	{...}	: initial state (as set of properties)  
	to	{...}	: final state (as set of properties)  
@media 	: each @media declaration is independent,  
		i.e. only one is applied, depending e.g. on device…  
		specifies media query (alternative properties/rules applied)  
SYNTAX:  
@media (feature: value) {  
	selector {  
		styles  
	}  
}  
e.g.  
@media (max-width: val) {...}	: changes when screen becomes low-width;  
					e.g. portrait, small window  
FEATURES:  
prefers-reduced-motion	: accessibility, for sensitivity to motion (e.g. scroll)  
				=reduce|no-preference  
  
FUNCTIONS:  
calc(expr)	: return result of math expression  
