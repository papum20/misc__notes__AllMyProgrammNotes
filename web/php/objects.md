# OBJECTS  
  
  
  
  
CHECK / BOOL :   
bool filter_var(var, filter)	: check filter  
	filter=FILTER_VALIDATE_URL  
bool in_array(el, arr)	: if el in array arr  
bool is_array(val)		: if val is array  
bool isset()			: ?  
bool pregmatch(regex, str)	: match regex on str  
  
VAR HANDLING :   
string create_function(str args, str code) : create a function with args and given code,  
and return a unique name for it  
array parse_url(url)	: return array, where each element is a part of url (if present)  
  
ARRAY :   
array array_merge(arr1, …)		: return merge of all arrays  
array_pop(arr)	: remove and return last element  
element array_shift(arr)		: remove and return first element  
array array_unshift(arr, el1, …)	: add [el1, …] to beginning of array;  
					return the array  
int count(arr)	: length of array  
string implode(str, arr)	: return a string, containing array elements joined by string str  
unset(arr[key])		: remove array element at key  
  
CURRENT :   
string $_GET[‘par’]	: value of current page’s url parameter par  
  
URIs :   
string file_get_contents(path)	: get content of link or local file  
  
I/O :   
die(string)	: print error string  
echo(string)	: print string  
