# BASICS  
  
MISC:  
;	//at the end of line  
  
OPERATORS:  
>= :  
<= :  
:= : assignment  
<var_array>[<index>] :   
<var_array>[<index1>, <index2>] :   
  
TYPES:  
<number> integer : (integer)number  
	es.: 0 integer  
  
KEYWORDS:  
data;						//makes it possible to separate definition/declaration  
(first declare with param, then define)  
	es.:	param <param_name1>;  
		data;  
		param <param_name1>:=<val>;  
display;					//”print”  
end;						//end of file(?)  
for {<var> in <set>}				//  
	es.:	for{...}  
		{  
			…  
		}  
<var> in <set>					//  
maximize <function_name>: <expression>;	//  
minimize <function_name>: <expression>;	//  
param	<param_name>:=<value>;		//param definition/declaration  
printf “string”;					//pretty print  
	printf “..%t..”;				//C-like  
s.t. <condition_name>: <condition>;		//condition definition  
set <set_name>;				//set declaration  
	set <set_name>:=<elem1> <elem2> …;	//set definitiion  
solve;						//  
sum {<var> in <set>} <expression>		//summation  
var <var_name>;						//variable declaration  
	var <var_name>=<expression>;				//variable declaration+definition  
	var <var_name> {<it> in <set>} >= <expression>;	//like “array”, it=index  
	var <var_name> {<it> in <set>} integer;  
	var <var_name> {<it1> in <set1>, <it2> in <set2>};  
