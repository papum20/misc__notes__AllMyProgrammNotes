# SYNTAX

## Variables

`val VAR` : const declaration, with inferred type  
`const val VAR` : "macro" declaration (replaced at compile-time), only global (e.g. not in functions)  
`var VAR` : var declaration, with inferred type  
`var VAR:TYPE` : var declaration, with `TYPE`  
`var VAR = if (CONDITION) VAL1 else VAL2` : conditional assignment  

### classes
`val V: IntArray = intArrayOf(1, 2, 3)` : `[1,2,3]`  
`val V = IntArray(5)` : `[0, 0, 0, 0, 0]`
`val arr = IntArray(5) { 42 }` : `[42, 42, 42, 42, 42]`  
`var arr = IntArray(5) { it * 1 }` : `[0, 1, 2, 3, 4]` - lambda, with `it` index  

`val myList = listOf<String>("one", "two", "three")` : immutable list  
`val myMutableList = mutableListOf<String>("one", "two", "three")` : mutable List (referenced by a val because it is the pointer)  

#### operators
`val resultList = numbers.map { it.length }.filter { it > 3 } ` :  

## Types
`Int` :  
`Long` :  
`Short` :  
`Byte` :  
`Float` :  
`Double` :  
`Boolean` :  
`Char` : `'c'`    
`String` : `"string"`  
`TYPE?` : nullable type  

`VAL as TYPE` : **cast** to `TYPE` -  

### inference
`42` : int  
`42L` : long  
`42.1` : double  
`42.1f` : float  
`true` : boolean  
`'4'` : char  
`"42"` : string  

## Operators
`+ - * / %`: arithmetic Operators  
`&& || !` : logical Operators  
`< > == >= <= !=` : comparison operators

`VAR?.PROP` : return null if nullable `VAR` is `null`  
`VAR!!.PROP` : cast `VAR` to non-nullable
*	can throw err  

`VAR?.PROP ?: VAL` : _elvis operator_ - dflt `VAL` if `null`  
 
## Statements
```kotlin
if(CONDITION) {} else 

when ( x ) {
	in 0..21 -> println("One line clause")
	in 22..42 -> println {
		println("Multiple line clause")
	}
		else -> println("Default clause")
}
for(item in myListMutable)
	println("hi")
while() {}
```

## Classes
```kotlin
class Animal ( // Constructor is within round brackets
	val name: String,
	val legCount: Int = 4 // Default value if not passed
) {
	// Properties not initialized by the constructor
	var foo: String = "Hey"
	private var bar: String = "Oh"
	// every prop must be inited at obj declaration, unless lateinit
	// (make sure that the variable is initialized somewhere else, e.g. init fun)
	lateinit var late_foo: String
	// lazy, w/ callback
	val name_lazy: String? by lazy {
		retrieveValue()
	}

	// Equivalent notation
	// setter and getter defined by dflt, can be overridden
	var sound: String = "Hey"
		get() = field
		set(value) { field = value } // Keyword field refers to the property
	// Custom notation
	var sound: String = "Hey"
		get() = this.name
		private set // Setter is private

	// static props (tied to class)
	companion object {
		const val Kingdom: String = "Animalia"
	}
	
	init {
		println("Hello I am a $name") // Function executed at instantiation time
	}
}

// extend
class Dog: Animal("dog") {
	fun bark() {
		println("WOOF")
	}
}

abstract class AbstractAnimal (
	val name: String,
	val legCount: Int = 4
) {
	abstract fun makeSound()
}
class Cat: AbstractAnimal("cat") {
	override fun makeSound() {
		println("MEOW")
	}
}

val dog = Animal("dog") // Instantiation of a class into an object
val duck = Animal("duck", 2)

dog.sound // Will access the getter, not the property
```

**setters**, **getters** : are implicit
*	e.g.: `className.prop = val` : calls `setProp()`, so can use even if `prop` private

**scope functions** : (6) -  
```kotlin
// `this` refers to the obj
val snake = Animal("snake") // Without “apply”
snake.legCount = 0
snake.sound = "Hiss" 
val snake = Animal("snake").apply { // With “apply”
	legCount = 0
	sound = "Hiss"
	this.function()
}
val numbers = mutableListOf("one", "two", "three", "four", "five")
numbers.map { it.length }.filter { it > 3 }.let { // With Let
	println(it)
} 
with(snake) { // With “with”
	makeSound()
}
// context object is the receiver “this”, but returns the lambda result
val legNumbers = snake.run() {
	legCount = 0
	howManyLegs()
}
// context object is the lambda argument “it”, but returns the object
numbers.also { // With Also
	it.add("six")
	println(it)
} 
```

**interface** and **delegation** of implementation:  
```kotlin
interface Animal {
	val legCount: Int
}
class Cat (override val legCount: Int) : Animal
class PersianCat (val cat : Cat) : Animal by cat { // delegated implementation of interface to cat
	fun someOtherMethod () {}
}
// (This will automatically implement all the interface members of Animal in PersianCat by invoking the same member on cat)
```

## Functions
```kotlin
fun isEven(number: Int = 0): Boolean {
	return number % 2 == 0
}
isEven(14)

// Extend the class Int
fun Int.isEven(): Boolean {
	return this % 2 == 0
}
14.isEven()

// higher order functions
fun List<String>.customCount(function: (String) -> Boolean): Int {}
fun <T> List<T>.customCountAllTypes(function: (T) -> Boolean): Int {}
```

## Misc
`// comment` :  