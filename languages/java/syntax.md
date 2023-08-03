# SYNTAX

## README.md  
*	[README.md](./README.md)  

## MISC
```java
...;										//end of command  
public static void main(String[] args) {}	// needed in main class of each executable file  
//comment
/* multi-line comment */  
```
note: `class, file` : must have same name  
  
## ASSIGNMENT  
type var_name = val;  
`final type var = val;` : constant  
//not-initialized value: default (0, false, ‘\u0000’ (0) )  
  
## KEYWORDS  
`if-else / for / while / try-catch()` : like c++  
`import` : import some_path;  
`new` : some_class var = new some_class();  
`try {}` :  
`catch(ExceptionType var_name) {}` :  
`finally {}` : execute anyway after try-catch  
`throw obj` :  
*	`//throw new SomeException(String s)` : throws exception  
`for(type var` : array) {}  
  
## TYPES  
## PRIMITIVE  
boolean  
char  
int  
long  
float  
*	`es. 10f`  
double  
## NON-PRIMITIVE / CLASS  
String  
*	`es. String s = “some_string”;`  
enum  
*	`es. public enum EnumClass {val1, val2};`  
*	`EnumClass obj = EnumClass.val;	//obj can only have a value from EnumClass`  
  
## ARRAY  
type[] var = {elements};  
type[] var = new type[int size];  
`type[] var = new type[]{};` : empty  
*	type[] var = new type[]{elements};  
  
## WRAPPER CLASSES  
//boxing: each primitive type var can be instantiated as object of wrapper class  
wrapperClass var = val;  
//unboxing: primitive type var from wrapper class  
type var = new wrapperClass(val);  
*	`//es.: int x = new Integer(1);`  
  
## OPERATORS  
`+ (String)` : concatenate  
  
## CLASSES  
(access_modifier) class ClassName {}  
<access_modifier> method…;  
*	`// =public, private, protected`  
  
`abstract` : some methods are to be defined in sub-classes (with override)  
	`*	//public abstract class ClassName {}`  
`extends` : inherits (only from one)  
	`*	//class SubClass extends SuperClass {}`  
`implements` : defines interface(s) (even more than one)  
	`*	//class ClassName implements OtherClass1, OtherClass2 {}`  
`interface` : only contains public definitions, not implementation (with implements)  
	`*	//ACCESS-MODIFIER interface ClassName {}`  
`@override` : subclass overrides superclass’s method (must have same arguments)  
//ACCESS-MODIFIER TYPE parentMethod(...) {}  
`super` : superclass  
	`*	//super.method(...)`  
	`*	//super.parameter`  
	`*	//super(...)`	: constructor  
`this.attribute` : this object  
  
## ACCESS MODIFIERS  
static some_method ();  
//can be used without instantiating an object (class.some_method())  
## CONSTRUCTOR  
--default: empty constructor: public Class() {};  
(JAVA) GENERICS:  
--generic types, usable in class  
## CLASS DECLARATION  
class ClassNameT1,T2-.. {}  
  
class ClassName<T extends SomeClass<T>> {}  
*	`--`  
*	`--extends even for interfaces (not implements)`  
*	`--can use extended class’s methods in class`  
## OBJECT INSTANTIATION  
ClassNameTYPE object = new ClassNameTYPE();  
ClassNameTYPE object = new ClassName();  
## INHERITANCE  
class inheriting_class extends inherited_class {}  
  
e.g.:
```java
public class Parent {  
	private int parameter; 
}  
public class Child extends Parent {  
	int parameter;
}  
note :
*	Parent.parameter only accessed from Parent  
*	Child.parameter and Parent.parameter different  
  
dynamic binding:  
```java
class ParentClass {  
	method1(){}
}  
class ChildClass {  
	@override 
	method1(){} 
}  
ParentClass obj = new ChildClass();  
obj.method1();	// ChildClass’s method1  
```
  
overriding :  
*	`Object` class : each class extends Object class  
*	polymorphism : methods can have different forms (inheritance)  
  
## INTERFACE  
<access_modifier> interface virtual_class1 {  
*	`some_type some_method ( ); }`  
class instance_class implements virtual_class1, virtual_class2 {  
*	`some_type some_method (some_args) {`  
	`*	…`  
} }  
interface IClass1 {}  
interface IClass2 extends IClass1 {}  
*	`--interface 2 extends (not implements) interface 1`  

## MAIN  
public class ClassName {  
public static void main(String[] args) {}  
}  
COMPARABLE interface:  
//only one method:  
public int CompareTo(Object obj);  
*	`//returns if -1 if lt obj, 0 eq, 1 gt`  
  
  
## EXCEPTIONS  

note: `Exception` is a class (root class of all exceptions)  
```java
try {  
	...
	throw new Exception("TEXT");
}  
catch (ExceptionType1 var_name1)	{...}  
catch (ExceptionType2 var_name2)	{...}  
catch (Exception var_name)			{...}	//for all exceptions  
finally {...}  
``` 
  
e.g.: definition of new exception:
```java
package exceptions;  
public class BadException extends Exception {  
	private static final long serialVersionUID = 1L;  
	public String getMessage() {  
		return "This is a really bad exception...";  
	}
}
```

  
## PACKAGES  
`package packageName;` : folder named packageName  
`import packageFolder.Class;` : import class in package  
*	import packageFolder.subPackage.Class;  
`import packageFolder.*` : import all package  
