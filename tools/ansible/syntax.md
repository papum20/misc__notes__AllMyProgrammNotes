# SYNTAX

**task**s : executed in order
*	all handlers executed in order, but all after all tasks

loop, using `item` in vals :
*	```yaml
	-	name: TASK NAME
		some.task:
			somearg: "text...{{ item }}...text"	# use {{ item }} to refer to current value
		loop:
			- val1
			- val2
	```

loop, using `item` with more fields :
*	```yaml
	-	name: TASK NAME
		some.task:
			arg1: "val{{ item.field1 }}"
			arg2: "val{{ item.field2 }}"
		loop:
			- { field1: val1, field2: val2 }
			- { field1: val3, field2: val4 }
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