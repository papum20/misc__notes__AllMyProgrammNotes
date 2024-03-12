# BASICS

_ios philosophy_ : only use provided ways of programming, provided methods, apps, tools, ways of thinking.  

## Editor

**XCode** :  
*	note: (ios philosophy) only interact with app's files inside editor

## MVC
ios apps use mvc.  

**MVC** : Model-View-Controller design pattern
*	**controller** : controls
	*	**outlet** : to interact (control) with **view**
*	**model** : keeps data
	*	e.g.: data structs
	*	only interacts with **controller**
		*	**notification** : method to ask something to **controller**
		*	**KVC** : 
*	**view** : ui elements, interactable
	*	only interacts with **controller**
		*	**action** : method to ask something to **controller**
		*	**delegate** : 

More MVCs can be combined
*	e.g.: a controller controls all
