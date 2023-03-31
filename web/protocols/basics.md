# BASICS  
  
  
Client-server	: client starts connection, asking for a service; server accepts, authenticates him, provides the service and closes the connection.  
Generic	: not depending on the transmitted format  
Stateless	: server doesn’t keep info ->   
		client should send the context  
  
Http allows sending resources identified by URI.  
Made of sequence of requests + sequence of responses.  
  
Types of connection / features :   
non-persistent :   
non-pipeline http	: server can only process one request at a time;  
	client must wait for response before new request.  
persistent	:   
pipelined http	: can transmit more requests without waiting for response;  
responses arrive in same order.  
multiplexed http	:  pipelined, but responses can arrive in different order.  
  
performance features :   
caching in server  
HTTP/2 performance features :   
PUSH operation	: server anticipates next client’s requests  
header compression	: data transmitted compressed  
  
STRUCTURE | REQUEST :   
method / http verb	:  
server’s action required (by client)  
URI		: identifies resource local to server  
version	: http version  
header	: RFC822 lines, divided in  
general header	: transmission info, related to request/response, not resource  
e.g.:  
Date			: transmission date/time  
Transfer-Encoding	: encoding format  
Cache-Control		: requested/suggested caching type  
Connection		: connection type to use  
(keep active, close after response…)  
entity header		: transmitted data, info on body / specified resource (if body not present)  
e.g.:  
Content-Type		: MIME type of entity in body;  
mandatory if body present  
Content-Length	: body byte-length;  
mandatory, especially if connection persistent  
Content-Encoding	: encoding format  
Content-Language	: language  
Content-Location	: specific resource url  
Content-MD5		: md5 digest value  
Content-Range	: resource’s requested range  
   
request header	: client specifies, to server, info on request and himself  
e.g.:  
User-Agent	: requesting client; client’s type, version, os  
Referer	: url: page showed to user while requesting new url  
Host		: domain name - port, to which connection made  
body		: MIME msg  
  
STRUCTURE | RESPONSE :   
status code	: if request successful;  
3 digits: 1=response class | 2,3=specific response.  
classes :   
1xx = informational	: tmp response, during processing  
2xx = successful	: received, understood, accepted request  
3xx = redirection	: request correct, but needed other actions client-side to complete it  
4xx = client error	: syntax error / unauthorized request  
5xx = server error	: server’s internal problem  
e.g. :   
100 Continue			: client hasn’t sent body yet  
200 Ok				: get successful  
201 Created			: put successful  
301 Moved permanently	: url not valid, server knows new position  
400 Bad request		: syntax error  
401 Unauthorized		: missing authorization  
403 Forbidden			: can’t authorize  
404 Not found			: wrong url  
500 Internal server error	:  server-side code error  
version	: http version  
header	: RFC822 lines, divided in  
general header	: transmission info  
entity header		: resource info, transmitted data  
response header	: response info  
Content-length	: allows client to know an entity was returned  
mandatory if sent entity  
Content-type		: how client should represent received resource  
mandatory if sent entity  
Server			: server’s type, os, version  
WWW-Authenticate	: challenge used for auth mechanisms  
body		: MIME msg  
  
METHODS :   
DELETE	:  
remove info related to resource;  
-> accessing to it later results in 404 Not Found;  
delete on not existing resource is legit, no error;  
prop.: idemp., not secure  
GET	:   
e.g. clicking an URL in an HTML, or specifying an URL in the browser  
prop: secure, idempotent  
HEAD	: like get, but srver mnust respond only with related headers, no body  
prop.: secure, idemp.  
used for: check validity, accessibility, coherence in cache of uri  
OPTIONS	:  
to check options, requisites, srevices of header;  
doesn’t imply another request will follow  
PATCH	:   
to update, partially, resource;  
i.e. only shows modifications to do, not change all like put;  
prop: not secure, not idemp.  
POST	: to transmit info client -> server, regarding URI resource;  
can be used to create new resources  
e.g. send form data  
prop.: no secure, idemp.  
PUT	: info client->server, creating or substituting specified resource  
no grant check accesses, locking;  
“like get made later, with same name” (?)  
prop.: idemp., not secure   
  
METHODS - PROPERTIES :   
Security	:   
method secure if doesn’t generate changes to server’s internal state  
(except logs)  
Idempotence	:   
method idempotent if the effect on the server, of more identical requests is the same as that of just one  
obs.: can be re-executed by more agents / at different times without side-effects  
