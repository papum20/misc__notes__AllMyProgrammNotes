# OBJECTS

## Events

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
