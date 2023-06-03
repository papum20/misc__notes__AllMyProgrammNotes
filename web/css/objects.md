# OBJECTS

## README.md  
	*			[README.md](./README.md)  

## STYLES
### ANIMATIONS
// animations go from start to end state, linearly  
	*			animation-...  

`name` : name  
`duration` : duration  
`iteration-count` : n of iterations  
`fill` : ?  
`delay` : delay between iterations  
  

### COLORS
`background-color = COLOR` : (default=transparent)  
`background-image = url(link)` : “link”;  
`border-color` :
	*			default=black  
`color` : (also for a) content color (including text)  
		*				(default) for links: blue if not clicked yet, purple if clicked  

`filter` : filter  
	*			filters of boxes/contents sum  
*	`=blur(px)` : blur  

`mask-image = IMG` : mask image  
`opacity` : non-transparency, 0->1.0 / 0%->100%  
  
  
### DIMENSIONS/POSITION

#### POSITION/SIZE
`max-width` :   
	*			(default for input you can type in: 1px 2px)  

`position` : position of container with respect to stream  
*	`=absolute`	: position where specified;  
				*						in case can hide other elements in same position  
*	`=fixed` : absolute with respect to viewport,  
	*	i.e. doesn’t scroll  
*	`=relative`	: moved by a variation from its position  
*	`=static	`	: position it would normally have in the stream  
*	`=sticky` : static, but when scrolling fixed, until its position disappears from viewport, in which case it disappears immediately  

`top|right|bottom|left` : absolute position of top|... side  
`height|width` : (also for hr) element’s content height, excluding border height  

`z-index` : overlapping / 3d plan,  
		*				default=last one is placed on other  
*			`=n`	: absolute number, no unit, represents payer  

#### HTML BOX MODEL
`border = LENGTH TYPE COLOR` :   
`margin` : margin area (can implicate scrolling page horizontally/vertically)  
`padding` : border in element, around content - pads in all directions  

`*-[left|right|top|bottom]` :  
`border-left-width` :   
*	`= val1 val2` : top/bottom=val1, left/right=val2  

`* = LENGTH` :   
`* = val1 val2` : top/bottom=val1, left/right=val2  

#### DISPLAY
`display` :   
	*			(controls how items are spaced out/aligned within *	container)  
*	`=block` : stacked vertically  
*	`=contents` : contents exist, container not  
*	`=flex` : make element a flex container, and its children flex items;  
	*	flexbox is a one-dimensional layout  

*	`=float` : (?) moved to left/right edge of container, then other *	siblings float around it  
	*			=grid  
*	`=inline` : stacked horizontally; takes content's dimensions  
*	`=inline-block` : inline, has its own dimensions  
	*			=list-item  
*	`=none` : hide  
	*			=table  
	*			=table-cell  
	*			=table-row  
  
### ELEMENTS
`aspect-ratio		=val1 / val2` : aspect ratio  
`border` : (default to none) to be visible, must be set width and style  
	*			border-left		= width style color;  
`border-left-style` :   
*			`=solid	`	: full  
*			`=double`	: double  
	*			border-radius		=tl tr br bl;	//(px), corners  
	*			smooth borders (corners)   

`box-shadow` : offset=any num; >0: right/up;  
	*			blurRadius=any num; blurRadius>0 makes less sharp edges;  
		*				height/width determined by element,  
	*			but can use spreadRadius to spread  
	*			=h-distance v-distance color  
	*			= offsetX offsetY [blurRadius=0] [spreadRadius=0] color;  

`box-sizing` :   
		*				=border-box  

`clip-path` : specify clip path -> everything inside is visible, outside not  
*			`=inset(n%)`	: inside of %  

`column-gap` :   
`column-rule` :   
`column-width|height` :   
`gap` : (for layouts, i.e. grid, flex, …) set gap between container’s items  
*			`=val` :   
*			`=val1 val2` : (row, col)  

`list-style` : (for a list) styles for list elements  
`object-fit` : (for img) how content should behave regarding box (e.g. proportions)  
*			`=cover` : keep proportions, make sure to cover all element’s box  
			*					i.e. can be bigger in one dimension  

`overflow` : behavior of content overflowing container  
*			`=hidden `	: overflowing content is hidden  
	*			don’t push content’s margin beyond box border (overflow inside)  

`=scroll` : there’s a scrollbar,  
	*			which takes up content space;  
	*			smartphone: no bar (you use fingers)  

`=visible` : container expands to contain all content  
`overflow-x|y` :   
  
### FLEX
`flex-direction` : flex direction  
		*				=row|row-reverse|column|column-reverse  

`flex-grow` :   
`flex-shrink` :   
`flex-wrap` : how items behave, when container too small  
		*				=nowrap  
*			`=unwrap` : (default) don’t wrap, shrink if needed  

`=wrap` : wrap to next row/col   
`justify-content` : (in flex) how items are positioned along main axis  
(pos, space around)  
	*			=center  
`=space-between` : first to the extreme left, last to end, and then subdivide and assign space in between  
`=space-evenly` :   
`order` :   
  
### GRID
`grid-area` : (child of grid)  
		*				= an element of parent’s grid-template-areas;  
		*				i.e. selects a space in the declared grid;  

`grid-template-areas` : (container with display=grid)  
		*				=”row1col1 row1col2…” “row2col1…” …;  

`grid-template-columns` : (container with display=grid)  
`grid-template-rows` : (container with display=grid)  
		*				rows dimensions  
  
### EVENTS
// e.g. ::hover  

`cursor` : set cursor type  
  
### MISC
`align-items` : (for flex) position items along cross axis (not main axis)  
		*				=center|flex-end  

`scroll-behavior` : scroll behavior  
		*				=smooth  
  
### TEXT
`font-family` : font type;  
		*				use“quotes” for complex names (i.e. made of more words);  
	*			order=priority (if first font not found, then 2nd, …)   
		*				(there exist some common to most browsers)  
*			`font-family: [font1], [font2];`	:  
	*			fallback font (alternative when first not found)  
*			e.g.: `sans-serif`  

`font-kerning` : text alignment  
		*				=normal|none  

`font-stretch = normal|wider|narrower` :   
`font-style = italic|normal|oblique` :  
`font-variant = normal|small-caps` : font variant    
`font-weight = bold|normal|NUM` : bolder  
`text-align = left|center|right|justified` : text alignment  
`text-align-last` :   
`text-decoration = none|underline|overline|line-through ` :
	*			e.g. underlined  
`text-transform = capitalize|uppercase|lowercase|none` :   
`white-space = normal|pre|nowrap` :   
*	`pre-line` :  
	*	e.g. print `\n` as newline  

#### LENGTHS
`* = LENGTH` :  

`font-size` :    
`letter-spacing` : letter spacing  
`line-height` : line height  
`text-indent` : indentation  
`text-shadow = H_DISTANCE V-DISTANCE COLOR` :   
`word-spacing` :   

  
### TRANSFORMATIONS
// applied to already created element (i.e. not readapted, e.g. can be stretched)  
transform:...   

`rotate(deg)` : clockwise  
	*			rotate3d()  
	*			*			scale()  
	*			*			scale3d()  
	*			skew()  
	*			translate()  
	*			translate3d()  
  
## AT-RULES
// for contexts / meta-rules  

`@keyframes` : describes initial, intermediate and final states of an animation  
@keyframe ANIMATION-NAME {  
*	`from	{...}`	: initial state (as set of properties)  
*	`to	{...}`	: final state (as set of properties)  

`@media` : each @media declaration is independent,  
	*			i.e. only one is applied, depending e.g. on device…  
	*			specifies media query (alternative properties/rules applied)  
### SYNTAX
@media (feature: value) {  
	*			selector {  
	*			styles  
	*			}  
}  
	*			e.g.  

`@media (max-width: val) {...}` : changes when screen becomes low-width;  
				*						e.g. portrait, small window  
### FEATURES
`prefers-reduced-motion` : accessibility, for sensitivity to motion (e.g. scroll)  
			*					=reduce|no-preference  
  
## FUNCTIONS
`calc(expr)` : return result of math expression  


