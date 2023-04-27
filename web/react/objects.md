# OBJECTS

## FUNCTIONS
`useEffect(effect(), deps?)` : call effect whenever deps updated (and once at decaration by dflt)  
*	if `deps` not specified, called at every page update  
*	note: use `deps=[]` instead, to only call once  

`useState<ValType>(val0) -> [val1, set(new_val)]` : returns a stateful value, initialized to `val0`, and a function `set` to update it  
*	`set(new_val)` : updates val  
*	`<ValType>` can be omitted  

## HTML
### ATTRIBUTES
`className=CLASS` : class argument  
*	note: class word was reserved for js  

`key=KEY` : unique key required to indentify and refer to element  

