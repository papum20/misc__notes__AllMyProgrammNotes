# OBJECTS  
    
## OBJECTS  
`.BeautifulSoup` :   
`BeautifulSoup(DOC, PARSER)` : init object with DOC containing html document  
*	`PARSER=”html.parser”`	: (default)  

`.extract()` : (?)  
`.find(...)` : (works like find_all)  
`.find_all([ELEM], [class_=CLASS], [ATTRS={...}], [recursive=BOOL])` :  
*	return array of all html elements of type ELEM, class CLASS, attributes specified, recursive if also search descendants  

`.find_all([string=STR])` : match STR (text)  
*	e.g. `str=”p” for p elements`  

`prettify()` : return pretty doc  
  
`tag` :   
`.get(ATTR)` : ATTR value  
`.string` : text in element  


