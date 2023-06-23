# OBJECTS  
  

## README.md  
*	[README.md](./README.md)  

## CLASSES  

### LAYOUT
#### Container
`Container` : container  
*	required for grid  
`container-fluid` : 100% width  

#### Flex
`d-flex` : display=flex  
`flex-{row|column}` : flex direction  
`flex-WRAP` : wrap options  
*	`WRAP=wrap|nowrap|...`  

`justify-content-SIZE-VAL` : justify-content=VAL  

#### Grid
// implemented with flexbox  
// each grid (i.e. row or col) has 12 available slots, which you can dispose and distribute as you want  
// need inside a `container`  
`row` :  
`col` :  

`*-SIZE-N` :  
*	e.g.: `col-md-4` : column wide `md`, taking `4` out of 12 slots from parent row  

##### alignment
`align-TARGET-[start|center|end]` : flex vertical alignment  
*	`align-self-*` : itself (e.g. for col)  
*	`align-items-*` : children (e.g. for row)  

`justify-content-[start|center|end|around|between|evenly]` : flex horizontal align  

##### order
// 6 predefined order priorities, from 0 (no order specified) to 5 (less important, i.e. last element)  
`order-[first|last|N]` :  
`order-BREAKPOINT-N` : (order is also responsive)  

#### hr
`[v|h]r` : vertical/horizontal layout divider
*	`<hr class=hr />` :    
*	`<div class=vr></div>` :    
`[v|h]r[-blurry]` : hr blurried at ends  
*	`<hr class="hr hr-blurry" />` :  

#### Table
`table` :  

`table-COLOR` : (for either `table`, `tr`, `th` elements)  
`table-bordered` : all borders around  
`table-borderless` :   
`table-sm` : cut paddings  
`table-striped` :  

`table-active` :  
`table-hover` : hover effect on row  

`table-align-[top|middle|bottom]` : vertical align  

`caption` : (accessibility) table content description   
*	`<caption>DESCRIPTION</caption>` :  
`caption-top` : show caption above table  
`table-responsive` : wrap a table to make responsive (horizontal scrolling)  
*	`<div class="table-responsive">` :  

### FORMS
// bootstrap slightly changes html forms  

`form-control` : allows bootstrap forms customization  

`form-floating` : wrap an `<input>` and a `<label>` in a `.form-floating` to create one  
*	e.g.:
	```html
	<div class="form-floating">
		<input ..>
		<label>..</label>
	</div>
	```
  

### COMPONENTS

`accordion` : vertically collapsing accordion  
`alert` : alert msgs  
`badge` :  
`breadcrumb` : navigate in pages hierarchy  
`close-btn` :  
`collapse` :  
`dropdown` :  
`list-group` :  
`modal` : dialog  
`navbar` :  
`offcanvas` : hidden sidebar  
`pagination` : pagination counter  
`placeholder` : e.g. while loading content  
`popover` : msg when hover  
`progress` : progress bar  
`scrollspy` : automatically update nav or list-group, based on scroll position, to indicate which link is currently active in the viewport  
`spinner` : loading  
`toast` : push notification  
`tooltip` : ?  

#### Button
`btn` : button (required)  

`btn-block` : display=block (stretch to full width)  
`btn-COLOR` : predefined colors  
*	`btn-danger` : a color (for a dangerous action)  
*	`btn-default` : default color  
*	`btn-link` : button forwarding to link  
	*	e.g.: `<button class="btn btn-link" data-toggle="collapse"	data-target="#PANEL_ID>"` : toggle collapse of div with id=PANEL_ID  
*	`btn-info` : a color (intended for a button about info)  
*	`btn-primary` : a color (intended for primary button)  

`btn-group` : group btns (hrizontal)  
`btn-group-veertical` :  

#### Card
`card` : panel/content container
`card-header` : 
`card-body` : 

#### Carousel
`carousel` :  
`carousel-inner` : content  
`carousel-item` : content element  
`carousel-control[prev|next]` : control `button`s  

#### Nav
`nav` : navigation elements container  
`nav-item` : nav element  
`nav-link` : nav `<a>`  

#### Panel
`panel` : some text with padding around  

### MEDIA
`media` : some media positioned alongside content that doesn't wrap around said media  

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


### ELEMENTS
#### image
`img-responsive` : make img adapt to screen, viewport  

#### modal
`Modal` : dialog box  
*	`show=bool` : if showed  

`Modal.Body` :  
`Modal.Header` :  


## STYLES

### SIZING
`w*` : width  
`h*` : heigth  
`m[w|h]*` : max width/height  

`g*` : gutters  
`m*` : margin  
`p*` : padding  

`X-N` : set on all sides to N  
`Xx*` : x size of property X  
`Xy*` : y  
`Xb-N` : bottom = N (pixel?)  
`Xe-N` : end (of text)  
*	e.g.: `me-N` : margin end  
`Xs-N` : start (of text)  

### COLORS
`COLOR=[primary|secondary|succcess|danger|info|light|dark|white]` :  

`[bg|border|text]-COLOR` :  

### VISUAL
`d-[none|inline|inline-block|block|table|table-cell|table-row|flex|inline-flex]` : display  
`well` : shadow, pad.. well  

### TEXT  
`text-[start|center|end]` : text alignment  
*	`text-[left|right]` : until **bootstrap 4**  
`text-[justify]` :   
`text-[nowrap|truncate]` :   
`text-[lowercase|uppercase|capitalize]` :   
`text-muted` : grayed out  
`font-weight-[bold|normal|light]` :   
`font-italic` :   
