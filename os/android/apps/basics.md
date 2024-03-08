# BASICS


## Activity

**activity** : a screen of an app  
*	contains methods to react to events
*	android keeps **stack** of activities
	*	always only one _running_

Extend `Activity` class.  

### states/events

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

## Views

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

### events
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

### subclasses

### groups and layouts

`ViewGroup` : invisible container of views, defines layout stucture for views inside
*	extends `View`

`Layout` : extends `ViewContainer`
*	needs to specify `layout_height`, `layout_width`

`LinearLayout` : row/col  

### widgets
Views with their own behavior implemented.  

`TextView` :   
