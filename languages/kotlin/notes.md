# NOTES

```kt
val myLiveData0: LiveData<String> = myLiveData1.switchMap { it -> MutableLiveData(it) }
val myLiveData1: LiveData<String>
	get() = myLiveData1.switchMap { it -> MutableLiveData(it) }
val myLiveData2: LiveData<String> = MutableLiveData("value")
```
*	`myLiveData0` is initialized immediately, with the given value
	*	will give error during class initialization, since it's referrring `myLiveData2`, which isn't initialized yet
*	`myLiveData2` won't give error, since doesn't have an init value, but only a `get()` function