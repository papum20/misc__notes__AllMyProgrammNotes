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

