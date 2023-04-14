# NOTES  
  
AJAX : Asynchronous JavaScript And XML  
not a language, but a set of technologies  
for asynchronous updates of portions of html pages  
use of :   
html, css  
DOM (in js)  
js: library XMLHttpRequest (XHR), for msgs browser - web server  
xml/js : meta-language for msgs  
note : first version, by microsoft, named XMLHttpRequest  
  
e.g. activation (creation XMLHttpRequest object) :   
if (window.XMLHttpRequest) { // Mozilla, Safari,...  
http_request = new XMLHttpRequest();  
} else if (window.ActiveXObject) { // Internet Explorer  
try {  
http_request = new ActiveXObject("Msxml2.XMLHTTP");  
} catch (e) {  
try {  
http_request = new ActiveXObject("Microsoft.XMLHTTP");  
} catch (e) {  
…  
}  
}  
}  
  
OBJECT :   
XMLHttpRequest()	: constructor of object to interact using ajax  
  
function .onreadystatechange : function which will manage server response,  
and open connection with server;  
		needed for synchronous connection;  
int .readyState	: state  
0 = uninitialize  
1 = loading  
			2 = loaded  
			3 = interactive  
			4 = complete  
.responseText	: response as plain text  
.responseXML	: response as XMLDocument  
int .status		: http status (code);  
			e.g. 200, 404…  
  
FUNCTIONS :   
// http_request = new XMLHttpRequest();  
// http_request.<>  
.open(“method”, “url”, bool sync, [username], [password])   
 connect to url with method;  
		bool = true if synchronous (blocking) connection, else async;  
		if true, need .onreadystatechange;  
		optional: username, password;  
.send([“Content-Type”], “mime/type”)	: send body of previously open connection;  
		e.g. POST -> body=query string;  
		e.g. GET -> body = null;  
		e.g. other cases, need to specify content-type;  

## README.md  
*	[README.md](./README.md)  

