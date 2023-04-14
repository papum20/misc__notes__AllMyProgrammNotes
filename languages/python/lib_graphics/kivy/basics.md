# BASICS  
  
(  
PNG: can have transparency  
JPG: compressed better  
)  
  
  
  
requires a class:  
  
from kivy.app import App  
from kivy.gridlayout import GridLayout  
class class_name(App):  
	def build(self):  
		...  
		return class_name.window  
	### ...OR…  
	def __init__(self, **kwargs):		#constructor in kivy need a second ** parameter  
		super(**kwargs)  
  
## README.md  
*	[README.md](./README.md)  

### runs when file opened  
if __name__==”__main__”:  
	class_name().run()  
  
  
  
item size in layout in dp:  
	size_hint: None, None  
	width: “...dp”  
	height: “...dp”  
  
SYNTAX:  
  
es. size = dp(100) : dp() means real size, not changing with screen pixel density  
self.parent : access to class which has an attribute of the type of self  
  
  
MISC.:  
  
self.ids = {“id”:object} : dictionary with key=id_name (in kv file)  
### or it’s the same as: self.ids.id_name  


