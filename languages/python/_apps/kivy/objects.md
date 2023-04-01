# OBJECTS  
  
.__version__ :   
  
METRICS  
  
dp(int) : int independent from screen size/pixel density, changes  
  
OBJECTS  
add  
width() :   
height() :  
size() = tuple(width, height)  
size_hint() : tuple(width, height) : in pixel  
  
pos_hint() = dictionary{x_index: x_value, y...} : index=”x/y”, “center_x/y”, “right/top”  
     value=percent (0 to 1)  
  
padding = tuple(int left, int top, int right, int bottom) : distance from borders in pixels  
  
  
opacity  = int : (from 0=not visible to 1=completely visible)  
  
  
  
LAYOUT  
  
add_widget(widget) :  
  
  
t = BoxLayout() :  
### items stacked horizontally/vertically  
orientation = string(“vertical” / “horizontal”)  
spacing = int (pixel) : space between items  
  
t = AnchorLayout() :  
### anchors to borders  
anchor_x = “string” : right / left / center  
anchor_y = “string” : bottom / top / center  
  
t = GridLayout() :  
### columns and rows (at least one must be declared)  
cols : columns  
rows :  
col_default_width : minimum width  
row_default_height : min height  
col_force_dafult : ignore children’s size_hint and use default width  
row_force_default :	//  
  
t = StackLayout() :  
### stacks items like boxLayout but on multiple lines  
orientation = string(“lr-tb”) : left to right, top to bottom, you can rearrange letters  
spacing = tuple(int pixel, int pixel) : space between items, horizontally and vertically  
minimum_height : real height of object, changing with window’s dimensions  
  
t = ScrollView() :  
### only one child, you need to specify child’s size  
  
t = PageLayout() :  
  
### takes objects as layouts to flip as pages  
“””  
<PageLayoutExample@PageLayout>:  
	GridLayoutExample:  
	BoxLayoutExample:  
“””  
t = RelativeLayout() :  
### allows you to set a different 0,0 point, i.e. to draw canvas in pos!=0,0  
### children properties relative to RelativeLayout  
  
t = FloatLayout() :  
### allows you to freely move child widgets, setting relative coordinates for them  
### children properties relative to Window  
  
  
  
WIDGETS  
### ALLOCATE STANDARD 100X100 SPACE FOR CHILDREN  
.add_widget(some_widget) :  
.children : list of children objects  
	### to modify: for child in some_widget.children[:]:  
  
 t = Button() :  
disabled = bool : not pressable  
on_press = function()  
text = string  
background_color = string  
background_normal = string : if “” : reset texture, doesn’t make colors interfere  
  
bind(on_press=function) : assign.. (function must have an unused parameter)  
bold = bool  
size_hint = tuple(int, int)  
  
t = Label() :  
color = text color  
font_name = string : string containing font file’s name or path  
font_size = int  
text = string  
  
t = ToggleButton():  
disabled = bool : not pressable  
on_state = function()  
state : string “normal” or “down”  
text  
  
t = Switch():  
active = bool  
on_active = function()  
  
t = Slider():  
disabled = bool  
max = float  
min = float  
on_value = function()  
value = float  
  
t = ProgressBar():  
### min: always 0  
max = float  
value = float  
  
t = TextInput(multiline=bool) :  
multiline = bool  
on_text_validate = function() : when you validate input, i.e. press enter  
text = string  
  
padding_x = tuple(int, int)  
padding_y = tuple(int, int) : space from borders (vertical) (in pixels)  
size_hint = tuple(int, int)  
  
t = Image() :  
allow_stretch = bool  
keep_ratio = bool  
source = string : path to image  
  
class my_class(Widget):	### EMPTY WIDGET  
width  
def on_size(self, *args):	### RUN WHEN SCREEN SIZE CHANGES  
	…  
def on_parent(self, *args):	### RUN WHEN OBJECT GETS PARENTED  
	…  
def on_touch_down(self, touch):	### RUN WHEN TOUCHING  
	…  
def on_touch_up(self, touch):	### RUN WHEN STOPPING TOUCHING  
	…  
  
 t = ActionBar() :  
### like android’s actionBar   
  
 t = Bubble() :  
### pop-up menu, with items stacked horizontally or vertically and an arrow pointing where	 you choose  
  
 t = Popup() :  
  
 t = Scatter() :  
### can be moved freely  
  
Screen  
### element to be used in ScreenManager  
###you should give a screen a name when created:  
s = Screen(name = “...”)  
  
name = string  
  
  
ScreenManager  
current = string : set current active screen, with name=string  
  
PROPERTIES  
  
var = BooleanProperty(bool) :  
var = NumericProperty(int/float(?)) :  
var = StringProperty(string) : =string, can be used as string, except when declared  
var = ObjectProperty()  
  
def on_”property_identifier_name”(self, widget, value): ## RUN WHEN VALUE CHANGES  
	…  
  
Clock:  
schedule_interval(function, dt) : repeats function every t seconds; (function must have					      dt(delta t) as parameter=real time between 2 frames)  
schedule_once(function, dt) :  
  
CANVAS  
### for drawing, you can add one in every widget  
  
t = canvas() :  
### for drawing, all shapes declared inside it  
### it can be the property of whatever widget  
### always drawn at position 0,0  
Color  
Ellipse  
Line  
Rectangle  
Quad  
“””  
class my_class(Widget):  
with self.canvas:  
	Line(...)  
“””  
  
t = canvas.before() : ### DISPLAYED BEFORE WIDGET, RENDERED BEFORE  
t = canvas.after() :  
  
t = Rectangle() :  
center : pos centro  
center_x  
center_y  
pos = tuple(int, int) : dp(numero)  
  
t = Ellipse() :  
  
t = Line() :  
circle = tuple(int center_x, center_y, radius)  
ellipse = tuple(int center_x, center_y, radius_x, radius_y)  
height  
points = tuple(int Ax, int Ay, ...) : list of x and y coordinates of points  
rectangule = tuple(int x, y, width, height)  
width  
  
t = Quad() :  
points = [x1,y1,...x4,y4]  
  
t = Triangle() :  
points = [x1,y1, x2,y2, x3,y3]  
  
t = Color() :  
rgb = tuple(int, int, int) : (0 to 1)  
rgba = tuple(int, int, int, int) : (0 to 1)  
  
  
CONFIG  
Config.set(‘graphics’, ‘string’, ‘var’) : ‘width’, ‘int’ :  
					 ‘height’, ‘int’ :  
					 ‘resizable’, bool :   
	  
### TO PUT IN THE VERY FIRST LINES  
  
PLATFORM  
### = string for platform name (linux, win, macosx)  
  
WINDOW  
Window.width	= int  
Winodw.height = int  
  
Window.request_keyboard(function, self) : function=keyboard_closed  
keyboard.bind(on_key_down/on_key_up=function)  
keyboard.unbind(on_key_down/on_key_up=function)  
  
def on_keyboard_down(...)  
def on_keyboard_up(...)  
  
LANG.BUILDER  
Builder.load_file(str) : load file (like additional kivy file)  
  
JsonStore  
store.delete(“key”) : deletes object with key “key”  
store.exists(“key”) : bool if exists object with key “key”  
store.find(**filter) : returns objects which mach filters as dictionaries  
(es. key1=val1, key2=val2)  
store.get(“key”) : returns a dictionary with keys:values of key “key”  
store.put(“key”, key1=val1, … , key_n=val_n) : inserts object with key:val variables  
							(if already exists, overwrites)  
  
CORE.AUDIO.SOUNDLOADER  
SoundLoader.load(str) : load audio in path: str  
(sound).play()  
(sound).stop()  
(sound).volume = int : volume 0 to 1  


#### (to add)

kivy  
self.ids.idname : access to widget in kv file with id:”idname”  
  