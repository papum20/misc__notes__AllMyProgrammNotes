# OBJECTS  
  

## README.md  
*	[README.md](./README.md)  

## CLASSES  

### STRUCTURE
#### CARD
`card` : panel
##### ELEMENTS
`card-header` : 
`card-body` : 

#### FLEX
`d-flex` : display=flex  
`flex-{row|column}` : flex direction  

#### MEDIA
`media` : some media positioned alongside content that doesn't wrap around said media  
##### ELEMENTS
`media-body` : 

#### NAVBAR
`navbar` : nav (required)  
`navbar-expand{-sm|-md|-lg|-xl}` : responsive collapsing  
##### ELEMENTS
`navbar-brand` : brand  
`navbar-toggler` : toggle button  
*	`data-parent=URL` :   
*	`data-target=URL` : target url for toggle  
	*	e.g.: `=#ID` : id in document  
*	`data-toggle` : 
	*	=`collapse|dropdown`  

### FEATURES  
#### COLLAPSE  
`collapse` : toggle element (required)  
`show` : show collapse element  

### TEXT  
`text-center` : center text  

### ELEMENTS
#### BUTTONS  
`btn` : button (required)  
`btn-block` : display=block (stretch to full width)  
`btn-danger` : a color (for a dangerous action)  
`btn-default` : default color  
`btn-link` : button forwarding to link  
*	e.g.: `<button class="btn btn-link" data-toggle="collapse" data-target="#PANEL_ID>"` : toggle collapse of div with id=PANEL_ID  
`btn-info` : a color (intended for a button about info)  
`btn-primary` : a color (intended for primary button)  

#### IMAGES  
`img-responsive` : make img adapt to screen, viewport  



