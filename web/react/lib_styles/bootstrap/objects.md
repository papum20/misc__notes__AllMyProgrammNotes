# OBJECTS

## TAGS

### STRUCTURE

#### Form
`Form` :  
*	`onSubmit=FUNCTION` : submit function (using `<Button type="submit">`)  

`Form.Check` :  
*	`label: string` : showed aside option  
*	`type="radio|checkbox"` :  

`Form.Control` : input  
*	`placeholder="text"` :   
*	`as="textarea"` : textarea  
	*	`rows={N}` : default n of rows  

`Form.Control.Feedback` : screen text showed when submit successfull (type=valid) or not (invalid)   
*	`type="valid|invalid"` : 

`Form.Footer` :   
`Form.Group` : group; used to send  
*	`contorlId="str"` : (accessibility)  
*	note: don't use `onSubmit` on it, but on parent `Form`  

`Form.Label` :  
`Form.*` :  
*	`onChange: function` : event handler on change  

#### Navbar
`Navbar` :  
*	`expand="sm|lg"|Bool` : if expand collapse-navbar when window large enough;
	*	`sm|lg` is the size of window such that it expands,
		*	e.g.: with `lg` only expands if it has a certain width  
*	`sticky="top"` : stick to  
`Navbar.Togggle` :  
*	`aria-cntrols=".."` : which menu this navbar is responsible for (`Collapse` id)  

`Nav` : navbar element  
`Nav.Link` : link  
*	`as={ELEM}` : behave like elem, so also use its attributes (but keep styles)  
	*	e.g.: `<Nav.Link as={Link} to="/url">` : react-router link  
*	`href="LINK"` :  
	*	note: refreshes all page; with react-router, use `Link`  

### ELEMENTS
`Alert` : alert window  
`Button` :   
*	`disabled=bool` :  
*	`form="FORM_ID"` : connect to form with id FORM_ID  

`Spinner` : (loading) spinner  
*	`animation="border"` :  

## ATTRIBUTES
`bg` :  
`variant=".."` : color   
*	`primary` : 
*	`danger` : red  
