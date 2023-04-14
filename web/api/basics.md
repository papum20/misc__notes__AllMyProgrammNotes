# BASICS  
  
Web API : HTTP interface; allows remote apps to use specific app  
  
REST : (REpresentional State Transfer) architecture model of www/ good apps;  
resource : any relevant part/concept of the web app  
URI : associated to each resource, as primary identifier / selector  
use CRUD operations, with its associated HTTP verb  
internal state of resource expressed is parametric : can be customized by requester with a Content Type  
  
CRUD model : all operations on data are of the type:  
Create : insert new record in database  
PUT  
Read: access in read mode to database  
GET  
Update : change in element  
POST  
Delete:   
DELETE  
  
(usually) use of hierarchy of contents :   
difference between :   
individuals :  
convention: no / at the end   
e.g. path/collection/element  
collections :   
convention: terminates with /  
e.g. path/collection/  
each has an URI.  
CRUD operations can be performed on each one.  
  
filters : generate a subset, through some rule.  
	use query part of URI.  
  
e.g.  
	// both add a new customer, but  
POST /customers/		: client can’t choose identified  
PUT /customers/abc123	: client chooses identifier  
  
def : API is RESTful if used REST principles  
  
DOCUMENTING API :   
need to define :   
supported end-points :   
HTTP access methods : (what happens doing get, push…)  
I/O representations : (?)  
error cases, with relative error msgs  
  
e.g. :   
Swagger : tools for creating, documenting API  
OpenAPI : language for documentation, made my swagger, public domain  
  
YAML : for data structures (like JSON, actually more powerful)  
python-like syntax  
indentation  
  
SECTIONS :   
paths :   
// contains, for each specified path, methods, specifications, parameters…  
/host/path: 			: path/endpoint  
	http method:  
	e.g. get:  
		summary: “...”  
		description: “...”  
		operationId: “...”  
		produces:  
		- e.g. “application/xml”  
		- e.g. “application/json”  
parameters :   
// (input parameters) each - represents a new parameter  
	parameters:  
		-	name: e.g. “Name”  
			in: path | query | body | …  
// where to specify parameter, in URI  
// e.g. in=”query”, URI: /path/?Name=val  
			description: “...”  
			required: true | false  
type: string | integer | array | object | …  
format: int64 | …  
			items:  
				type: …  
			schema:  
				$ref: e.g. ‘#/definitions/Name’  
		-	in: …   
name: …  
definitions :   
// (input parameters) each - represents a new parameter  
	<Name>: 	// e.g., parameter name  
		type: …  
		properties:  
			<property1>:	// property name  
				type: …  
				format: …  
				description: …  
				enum:   
					-	<val1>  
					-	<val2>  
			<property2>:	// property name  
				…  
responses :   
// output, i.e. data, error msgs, codes  
		responses:  
			‘<n1>’:		// http codes  
					// e.g. 200, 400, 404 …  
				description: …  
				schema:  
					type: …  
					items:  
						// return data  
						$ref: ‘...’  
			‘<n2>’:  
				…  

## README.md  
*	[README.md](./README.md)  

