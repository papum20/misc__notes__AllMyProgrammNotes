# SYNTAX

## KEYWORDS AND STUFF, FROM HTML/CSS/etc.
Keywords, html tags names, css properties names are similar, but usually use lowerCamelCase to replace dashes, and sometimes differ.  
e.g.:  
*	html:
	*	`class` attribute is `className`  
	*	`style` attribute is now an object, where keys are without quotes (so single words) and values are strings
		*	e.g.: `<.. style={{width: "10%"}}>`
*	css:  
	*	dashes replaced by lowerCamelCase
	*	e.g.: `border-radius` property is `borderRadius`
*	bootstrap:
	*	uppercase first letter
	*	e.g.: `Form`

## EXPRESSIONS
`{EXPR}` : use var value in html parts  
*	e.g.: `<Button id={ID}>{SOME_TEXT}</Button>`  

## COMPONENTS
`const Component = (arg) => {...}` : component with one arg of tipe object, parameters arguments passed  
`const Component = ({arg}) => {...}` : component with one arg, which was passed as parameter  

## HTML
`<> </>` : **fragment** (empty tag)  
*	e.g.: `{<>{}</>}` is valid, `{{}}` not  