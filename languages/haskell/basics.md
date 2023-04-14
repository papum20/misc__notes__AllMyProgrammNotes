# BASICS  
  
## README.md  
*	[README.md](./README.md)  

## TYPE/KIND SYSTEM
### TYPES

### KINDS
type of types / meta-type;  
`*` : single kind  
*	e.g.: `* -> *` : kind of function like `foo arg1 = expr1`, of type `foo :: a -> b`

## OLD
_ : anything  
  
-- comment  
{- … -} multi-line comment  
  
(some_operator) : operator  
-- es. (>) / (:) --conc.  
  
if bool then expression1 else expression2  
  
  
data x = term not_term | term.. | … deriving Show  
  
  
  
TYPES :  
newtype type_name = type_name (type_1 … type_n)  
	-- struct type_name {type_1, …, type_n}  
  
Integer  
String  
LIST :  
[] = empty list  
elem1 : elem2 : []  
: associativo a destra  
  
COPPIA:  
C ::= (a, b)  
  
DATA STRUCTURES:  
LISTA ASSOCIATIVA:  
((“a”,1):(“b”,2)...)  
  
OPERATORS :  
string ++ string = stringstring  
==  
/= : not equal  
  
FUNCTIONS :  
-- DEFINITION:  
--type:  
f :: input1 -> (input1 -> output) -> input…n -> output  
--(input1 -> output) = function as aparameter  
f parameter1 parameter2 = expression  
  
CLASS:  
-- DEFINITION:  
class class_name type where  
-- parameters, es.  
(>>>>) :: a -> a -> Bool  
  
instance class_name type where  
	-- es.  
	(>>>>) = (>)  


