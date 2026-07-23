# NOTES

```kt
val myLiveData0: LiveData<String> = myLiveData1.switchMap { it -> MutableLiveData(it) }
val myLiveData1: LiveData<String>
	get() = myLiveData2.switchMap { it -> MutableLiveData(it) }
val myLiveData2: LiveData<String> = MutableLiveData("value")
val myLiveData3: LiveData<String> by lazy {
	myLiveData2.switchMap { it -> MutableLiveData(it) }
}
```
*	`myLiveData0` is initialized immediately, with the given value
	*	will give error during class initialization, since it's referrring `myLiveData2`, which isn't initialized yet
*	`myLiveData1` won't give error, since doesn't have an init value, but only a `get()` function
	*	warning : the `get()` will instantiate a new `LiveData` on every call, so may create leaks, or too many calls, calls loops, mess
*	`myLiveData3` initialized lazily, so (probably) without errors, like with `get()`