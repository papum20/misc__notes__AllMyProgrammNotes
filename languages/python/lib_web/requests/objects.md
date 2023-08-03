# OBJECTS  
  

## HTTP requests
//obvious methods  
//return a response  

`REQUEST(URL, cookies:Dict[str,str], data:Dict|List[tuples]|string, headers:Dict[str,str], json:Dict, params:Dict[str,str])` :  
*	`cookies`: send your own cookies to server  
*	`data` :   
	*	for send functions, i.e. post, put  
	*	sends encrypted  
*	`headers` : custom headers, passed like parameters;  
	*	notes: custom headers are given less importance than default ones;  
	*	i.e. if default are defined with same names, these ones are used;  
	*	custom headers are different from parameters: define info about cline (user-agent), server, comm. channel, resources metadata, debug info;  
	*	usually names in the form `X-header`  
*	`json` : data sent as json  
*	`params` : pass parameters (query) as params
	*	implementation: adds params to URL as query;  
	*	if `key==None`, not added;  
  
`.delete(URL)` :   
`.get(URL)` :   
`.head(URL)` : only receive headers;  
*	useful when just want some metadata, not full response (if big file)  

`.options(URL)` : list supported requests, in header Allow  
`.patch(URL)` :   
`.post(URL, data={‘key’:’value’})` : send (more used) (for web forms)  
(specific application header)  
`.put(URL, data={‘key’:’value’})` : send  
note: this get doesn’t keep data, cookies, params… as a normal browser, but establishes a new connection every time. (use Session instead)  
  

## some headers

`Accept` : response format considered “acceptable” by client, in the form of a list, in order of preference, following the types MIME (defined by IANA)  
*	`= application/html`  
*	`= application/json`  
*	`= application/xml`  
*	`= application/x-www-form-urlencoded` : only and specifically used for web forms (once);  
	*	actually obsolete and substituted, when possible, by xml and json  
(more appropriate to send structured data);  

`Allow` : allowed requests (returned by options() )  
  

## RESPONSE   
// response object  

`content` : response in bytes  
`cookies -> RequestsCookieJar` : cookies used by site  
`encoding` : encoding format  
*	`=”utf-8”|”ISO-8859-1”`  

`headers` : header  
`json` :   
`text` : response decoded as text  
`url` : processed/sent url (e.g. added params)  
  
## OBJECTS   
`.RequestsCookieJar` : acts like a dictionary, but also allows more operations  
  
`.Session` : allows to keep an established connection (session), like a browser, thus keeping   
*	data, cookies, parameters…  

`.Session.get()` :   

