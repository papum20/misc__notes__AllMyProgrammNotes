# BASICS  
  
SCRIPT:  
python file:  
class ...Layout_name(...Layout):  
	pass  
## README.md  
*	[README.md](./README.md)  

### declare in py file  
  
kv file:  
line 1:  
	WindowName:  
### select the main layout/window/thing to display  
  
  
<Widget_name>:  
<> for definition  
### already declared in python file  
  
<Widget_name@class>:  
### @ if not declared in py file (CLASS DECLARATION IN KV, DERIVED FROM @)  
  
<Widget_name@class1+class2>:  
### CLASS DECLARATION IN KV, DERIVED FROM DIFFERENT CLASSES  
  
  
  
  
### VALID IN ORDER  
canvas:  
	Line:  
	Color:  
	Line:  
### ONLY SECOND LINE GETS COLOR  
  
  
  
SYNTAX:  
  
not  
  
es. size: “100dp”  
:, not =  
“dp” means real size, not changing with screen pixel density  
  
# : for comment  
  
  
self.attribute : refers to itself  
root.attribute : refers to “parent”  
root.parent.attribute : parent of parent  
“””  
<GridLayoutExample>:  
	Button:  
		on_press : self.function()	#refers to button  
		on_press : root.function()	#refers to GridLayoutExample  
“””  
  
  
Item:  
	id: name  
### you can refer to item by id  
  
  
(beginning:) #: import file  
#: set name value  


