# SYNTAX

loop, using `item` in vals :
*	```yaml
	-	name: TASK NAME
		some.task:
			arg: "val{{ item }}"
		loop:
			- val1
			- val2
	```

**handler** : a task triggered by another one :
*	```yaml
	-	task1: ...
		notify: handler_name

	handlers:
		-	name: handler_name
			task2: ...
	```
*	e.g.: `task1` copies a file, `task2` restarts a service - but ansible only copies if file changed, so also handler is triggered conditionally