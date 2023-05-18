# OBJECTS  
  
## README.md  
*	[README.md](./README.md)  

## FUNCTIONS  
  
## BASICS  
`Comparable` : (interface)  

`.compareTo(Object obj)` : returns -1 if caller < obj, 0 =, 1 >   
  
*	Object  
`.getClass()` :  
`.hashCode()` :  
`.toString()` : class to string  
  
## ERRORS  
`new SomeException()` : returns error  
`new SomeException(String s)` : returns error with string s  
  
## TYPES  
### Arrays  
`.asList(array)` : array to list (collection)  
  
### Array  
`.length` :  
  
### Double  
`.parseDouble(string)` : converts from string to double  
  
### Integer  
`int .compareTo(Integer)` : compare values  
`.parseInt(string)` : converts from string to int  
`.valueOf(int)` :  
  
### String  
`.length()` :  
`.substring()` :  
`.toLowerCase()` :  
`.toUpperCase()` :   
  
## INPUT/OUTPUT  
`BufferedReader` :  
`InputStreamReader isr = new InputStreamReader(System.in)` :   
`BufferedReader br = new BufferedReader(isr)` :  
`String br.readLine()` :   
  
### Scanner  
// import java.util.Scanner;  
// Scanner s = new Scanner(System.in);  
`s.next()` : return input string  
`s.nextByte()` :   
`s.nextDouble()` :   
`s.nextFloat()` :   
`s.nextInt()` :   
`s.nextLong()` :   
  
### System  
`.currentTimeMillis()` : current time (ms)  
  
### System.out  
//std output  
`System.out.println(string / object)` : prints argument and line separator  
*				if object: calls objectType.toString()  
  
## TIME  

`System.currentTimeMillis()` :  
  
### Calendar  
// import java.util.Calendar;  
`int DAY_OF_MONTH` : value for get/set  
`int MONTH` : value for get/set  
`int YEAR` : value for get/set  
  
`int get(int field)` :   
  
### Data  
// import java.util.Date;  
  
### GregorianCalendar  
// import java.util.GregorianCalendar;  
//extends Calendar  
`GregorianCalendar(int year, int month, int dayOfMonth)` : constructor  
  
### Year  
// import java.time.Year;  
`int .getValue()` : year to int  
*	//es.: int y = Year.now().getValue()  

`static Year Year.now()` : current year  
`Year Year.of(int )` :  year from int to Year  
  
## MATH  
// Math  
// import java.lang.Math;  
`max(int a, int b)` :  
`min(int a, int b)` :  


