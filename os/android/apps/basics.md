# BASICS

## FILE STRUCTURE

`PROJECT_NAME` : 
*	`java/` : code
	*	`MainActivity.java`/`MainActivity.kt`
*	`res/` : XMLs for resources
	*	`animator/` : XML for property animations - old framework to change properties over time.
	*	`anim/` : XML for tween animations - newer framework to change properties in a bulk.
	*	`color/` : XML files that define a state list of colors (simple colors are in values).
	*	`drawable/` : Bitmap files (.png, .jpg, .gif) or XML files compiled into other resources.
	*	`layout/` : XML files that define a user interface layout.
	*	`mipmap/` : Drawable files for different launcher icon densities
	*	`menu/` : XML files that define application menus.
	*	`raw/` : Arbitrary files to save in their raw form (they don't have a default implemented behaviour).
	*	`values/` : XML files that contain simple values, such as strings, integers, arrays.
		*	`strings.xml` : all strings, labels used in app 
	*	`xml/` : Arbitrary XML files

## CONCEPTS

### Activity

**activity** : a screen of an app  
*	contains methods to react to events
*	android keeps **stack** of activities
	*	always only one _running_

Extend `Activity` class.  

#### states/events

states :
1.	**created** : `onCreate(Bundle savedInstanceState)` - (app not visible) contains startup logic, load layout
	*	parameter for saved state
2.	**started** : `onStart()` - (app visible but not interactable) right before visible to user  
3.	**resumed** : `onResume()` - (app visible and interactable)  
4.	**paused** : `onPause()` - (app visible but not interactable) overlayed/interrupted by another one, can't receive user events  
	*	light stop, don't save data
	*	stop cpu-consuming processes
	*	e.g.: answer call (before android 14, now **stopped**)
5.	**stopped** : `onStop()` - (app not visible) when about to destroy, or another app in foreground 
	*	stop cpu-intense processes
6.	`onRestart()` : `onStart()` after **stopped**    
7.	**destroyed** : `onDestroy()` - (app not in memory) when os needs stack space, or called `finish()`   
	*	e.g.: when change layout, so then `onCreate()` again to reload layout
8.	`onFreeze()` : (not used since 2008)  

Can `@Override` default events.  

### Resources

**resource** : What is not code   
*	declared in `xml`
*	each identified (unique id) by `SUBCLASS.name` (`SUBCLASS` is the **resource type**)
	*	obs: `name` can repeat in different `SUBCLASS`es
	*	obs: `xml` file in which declared doesn't matter, as always mapped to same `R.SUBCLASS`
*	each mapped to `java` code as `public static final int [PACKAGE_NAME.]R.SUBLCLASS.name = VAL`

**resource type** : `xml` tag, subclass of `R`  

`R` : resource base class  

`[PACKAGE_NAME.]R.SUBLCLASS.NAME` : reference to a resource  
*	`PACKAGE_NAME` : needed if not in same class

### Views

`View` : a self-contained object/component of the screen 
*	also views containers (`ViewGroup`) 
*	**declarative** : declared in xml
	*	e.g.:
		```xml
		<TextView
			android:id="@+id/textView"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			android:text="Hello World!" />
		```
*	**programmatic** : created in java/kotlin
	*	e.g.: `public TextView textView = new TextView(this)` : java
	*	e.g.: `lateinit TextView textView = TextView(this)` : kotlin
		*	`lateinit` : as not exists at compile
*	e.g.: text, button

#### events
Can be handled via:
*	`android:onClick="FUNCTION"` : xml
*	`onTouchEvent()` : java/kotlin event handlers
*	`button.setOnClickListener(onClickListener)` : java/kotlin event listeners, takes as argument obj implementing OnClickListener interface
	*	```java
		button.setOnClickListener(new OnClickListener() {
			@Override
				public void onClick(View view) { /* Behavior */ }
		});
		```
		: java
	*	```java
		button.setOnClickListener(
			v -> { /* Behavior */ }
		);
		```
		: java lambda
	*	```kotlin
			button.setOnClickListener{
				/* Behavior */
			}
		```
		: kotlin lambda

#### fragments

`Fragment` : modular section of an activity, can be reused in multiple activities  
*	needs someone to contain it
*	**arguments** : data passed to fragment
	*	in constructor : to avoid, as each fragment must have a no-arg constructor, which is the one called by the system when recreating the fragment
		*	e.g. after screen rotation
	*	good alternatives :
		*	bundle
		*	factory method
		*	navigation args

#### subclasses

#### groups and layouts

`ViewGroup` : invisible container of views, defines layout stucture for views inside
*	extends `View`

`Layout` : extends `ViewContainer`
*	needs to specify `layout_height`, `layout_width`

##### static
`LinearLayout` : row/col  

##### dynamic
Dynamic layouts (which can change at runtime) need an adapter, so they can map data to a view, via a view template (a view).  

#### widgets
Views with their own behavior implemented.  

`TextView` :   
