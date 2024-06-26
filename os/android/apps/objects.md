# OBJECTS


## Activities

### events

`onRestoreInstanceState(Bundle savedInstanceState)` : called when passing **created**->**resumed**   
`onSaveInstanceState(Bundle savedInstanceState)` : called when passing **resumed**->**destroyed**  
`onTouchEvent(event: MotionEvent)` :  

## GUI

`setContentView(?)` :  

## IO

`Log` : logging class
*	categories (from lowest priority) :
	1.	`Log.v(TAG, MSG)` : verbose
	2.	`Log.d(TAG, MSG)` : debug
	3.	`Log.i(TAG, MSG)` : information
	4.	`Log.w(TAG, MSG)` : warning
	5.	`Log.e(TAG, MSG)` : error
	6.	`Log.wtf(TAG, MSG)` : should never happen in life (unexpected, means logic is wrong)

## Resources

### types

#### values
Tags from any file in `res/values`  

`<string>` : String value
associated to a key.  
`<integer>` : Integer value
associated to a key.    
`<string-array>` :  
*	`<item>`

`<integer -array>` :  
*	`<item>`

`<color>` :  
`<dimen>` : Dimension units of
the GUI components  
`<style>` :  

#### drawable
Tags from any file in `res/drawable`  

`<drawable>` : Images and everything that can be drawn  

#### mipmap
`<mipmap>` : images to be used as icons  

## View

`visibility` : if visible
*	`GONE` : not visible and doesn't take space
*	`INVISIBLE` : still takes space
*	`VISIBLE` : 

`findViewById()` :  
*	java requires cast until api 26

### Fragment

`parentFragmentManager` : parent's `supportFragmentManager`  

#### DialogFragment

`show(fragmentManager, TAG)` :
*	`TAG` : can be used to retrieve

##### AlertDialog
the actual dialog  

`activity` :  

`AlertDialog.Builder(activity)` : get builder, for creating dialog  

###### AlertDialog.Builder

`create()` : create alert dialog with arg supplied to builder  

`set*()` : setters for adding views to the dialog  
`setTitle()` :  
`setView()` : set any other, non pre-defined, view  

### FragmentActivity
e.g.: `AppCompatActivity`  

`supportFragmentManager` : FragmentManager for interacting with fragments associated with this activity  

### xml
`id="@+id/ID` :  
`padding=PADDING` :  

### button
`performClick()` :  

### Layout
`android:layout_*` : layout attrs, for the layout element or a child of its  

`layout_height=HEIGHT` :   
*	`=0dp` :  
*	`=match_parent` :  
*	`=wrap_content` : adapt to content  

`layout_margin=MARGIN` :  
`layout_width=WIDTH` :  

#### LinearLayout
`layout_gravity=` :  
`layout_orientation="horizontal"|"vertical"` :  
`layout_weight=NUMBER` :  
*	e.g.: if child has 1 and another 2, the 2 has double its size in direction perpendicular to "orientation" 