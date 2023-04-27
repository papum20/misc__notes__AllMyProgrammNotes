# NOTES

## README.md  
*	[README.md](./README.md)  

## ACCESSIBILITY
### STRUCTURE
*	follow structure  
*	don't rely on graphical features  
	*	e.g.: colors, font size, relative position (to the left/right/top..)  
	*	note: browsers can display differently  
*	use lists  
	*	e.g. in nav  
*	def: **landmark**: landing point  
#### aside
for info not fundamental  
*	if screen wide: show on side  
*	else: show below  
#### article
wraps (small) title, header, body..  
*	note: can contain header  
### ELEMENTS
#### HEADERS
*	use headers right  
#### TABLES
*	tables:
	*	use caption, th, thead...  
#### FORMS
##### input
for label referring to input  
*	option 1: `<label><input ..>..</label>`  
*	option 2: `<label for=INPUT>..`
##### text/textarea
*	`title`  
*	`placeholder`  
##### fieldset
for grouping related fields  

### ATTRIBUTES
#### role
for some features not provided by html  
*	e.g.: `role="search"` : search bar  
values:  
`navigation` : landmark  
:  
:  