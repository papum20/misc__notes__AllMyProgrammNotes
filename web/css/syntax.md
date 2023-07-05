# SYNTAX

## README.md  
*	[README.md](./README.md)  

## MISC
`/* COMMENT */`    

## SELECTORS
// SEL stands for SELECTOR  
  
```css
ELEMENTS {						/* type selector(s) */  
	property: value;  
	property: value !important;	/* property is never overwritten by later rules */  
}  
```

`TAG` : select by tag  
`.CLASS-NAME` : class selector  
`#id` : id selector  
`SEL1, SEL2` : multiple selection  
`*`	: (generic selector)  

`SEL1 SEL2` : type selector for any matching SEL2 nested in any SEL1   
`SEL1 > SEL2` : type selector for any element2 direct child of element1  

`TAG.CLASS` : elements of type TAG, with CLASS as one of their classes;  
*	i.e. they can also have other classes  

### pseudo-type selectors  
`SEL1 + SEL2` : first occurrence of 2 after 1  
`SEL1 ~ SEL2` : all sibling occurrences of 2 after 1  

`SEL:active|checked|enabled|hover` :    
`TAG:first-child|letter|letter` :  
`TAG:first-of-type` : first occurrence of type tag  
`TAG:last-of-type` : last occurrence  
`TAG:not(rule)` : all except  
*	e.g.:	`not(.class-name)`  

`SEL:nth-child(n)` : element(s) corresponding to SEL which are nth-child of their parent  
`SEL:nth-child(odd|even)` : all odd or even children  
`SEL:odd` :   
`SEL:even` :   
`type[attribute]` : all type elements with an attribute attribute set (any value)  
`type[attribute=”val”]` : attribute selector  
`SEL[attr^=”val”]` : starts with val  
`SEL[attr*=”val”]` : match any *val*  
`SEL[attr~=”val”]` : match any * val *  
*	(i.e. matches whole word val, with separators before and after)  

### pseudo-elements :   
`TAG::after` : create an element which is last child  
`TAG::before` : create an element which is first child  
  
## VALUES  
### for any value
`=inherit` : (default for all elements/properties)  
*	inherits container’s val   
`=unset` : unsets set values  

### UNITS   
// for numerical values

`percent` :   
`%` : % of parent  
`lengths` :  
`absolute` :  
`deg` : degrees  
`cm | mm | in` :   
`pc` : pica  
`pt` : point  
*	px  
`relative` :  
`ch` : 0 width  
`em` : percentage [0,1] of element’s font size  
`ex` : x height (with current font)  
`fr` : (flex unit) fraction of remaining space of container  
`lh` : row height  
`rem` : root em; percentage [0,1] of font size of html element  
`vh|vw` : viewport height/width: val% of viewport height/width  
`vmin|vmax` : min/max between vh/vw  
`functions` :   
`=max(val1, val2)` :  	  
`=min(val1, val2)` :   
`=SIZE1,SIZE2,...` : (?) multiple sizes  
`=SIZE1,*,*` : sizes for * are equally divided, once removed fixed ones  
`color values` :    
*	=rgb(int, int, int);  
`=rgba(int, int, int, float|%)` : adds alpha channel (0-1.0|%)  
`=[constant];` : color constant  
*	=#hexadecimal;  
`=#hexadecimal-alpha` : add 2 digits for alpha  
`=hsl(int, int%, int%);` : HSL (hue, saturation, lightness) color model;  
	`*	hue=0...360 (color wheel degrees, 0=top=red)`  
	`*	saturation=0…100`  
	`*	lightness=0…100`  
`hsla(...)` : add alpha  
`=linear-gradient(direction=180deg, color1 [color-stop1], color2 [color-stop2]…)` :  
*	actually an image (so use it with background);  
*	linear gradient (distributes colors evenly) between (min. 2) colors,  
in any format: default stops (3 colors-> 0,50,100%);  
optional color-stop for each color: number (px/%/…)  
*	indicating the point of the full element where it stops  