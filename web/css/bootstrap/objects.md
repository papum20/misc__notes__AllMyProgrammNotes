# OBJECTS  
  

## README.md  
*	[README.md](./README.md)  

## CLASSES  

### STRUCTURE
#### Container
`Container` : container, required for grid  
inside:  
`Row` : grid row  
*	`xs,md,xl={n}` : n of cols for screen dimensions  


#### Card
`card` : panel
inside:  
`card-header` : 
`card-body` : 

#### Flex
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
`text-muted` : grayed out  

### ELEMENTS
#### button
`btn` : button (required)  
`btn-block` : display=block (stretch to full width)  
`btn-danger` : a color (for a dangerous action)  
`btn-default` : default color  
`btn-link` : button forwarding to link  
*	e.g.: `<button class="btn btn-link" data-toggle="collapse" data-target="#PANEL_ID>"` : toggle collapse of div with id=PANEL_ID  
`btn-info` : a color (intended for a button about info)  
`btn-primary` : a color (intended for primary button)  

#### image
`img-responsive` : make img adapt to screen, viewport  

#### modal
`Modal` : dialog box  
*	`show=bool` : if showed  

`Modal.Body` :  
`Modal.Header` :  

## STYLES
### BOX MODEL
#### marign
`mb-N` : margin bottom = N (pixel?)  
`me-N` : margin end (of text)  
`ms-N` : margin start (of text)  
