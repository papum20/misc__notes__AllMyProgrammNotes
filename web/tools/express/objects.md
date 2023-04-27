# OBJECTS

## FUNCTIONS

## OBJECTS
### Express
`express()` : create (and return) express application  
`.json()` : can use json (receive/send)   
`listen(PORT, () => {})` : listen for connections, with function as callback  
`use(function)` :   
*	e.g.: `use((error: unknown, req: Request, res: Response, next: NextFunction) => {})` : use error handler  
	*	note: next is not used, but required by express  
		*	(you can disable eslint warning)
	*	note: Request is the one from express library  
`Router()` : return router, i.e. a way to refer to already created express() object  

#### HTTP REQUESTS
`REQUEST_NAME('URL', (req,res) => {})` :  
`URL=something/:param1` : specify space for param1 (usable later)  

`get('URL', (req,res) => {})` : response to get request at URL, using function  
`patch(..)` :  
`post('URL', (req,res) => {})` :  

note: can use same endpoint for multiple http methods (but not for multiple instances of same method)  

### Next Function
function `next(error)` for middleware  

### Request
`body` :  
`Object params` : parameters  


### RequestHandler
`type RequestHandler` :  
`type RequestHandler<PARAMS, RES, REQ, QUERY>` : type with specified types  
*	put `unknown` if want to leave default  

### Response
`json(body)` : send json response with body  
*	body of any type (then transformed to json)  
`sendStatus(int)` : set status code and use as body  
`status(int)` : set status code  
