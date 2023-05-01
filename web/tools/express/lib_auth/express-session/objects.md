# OBJECTS

## Session
`Session` : middle-ware  

### methods
`session(options)` :  
*	`options`:  
	*	`secret` :  
	*	`resave` :  
	*	`saveUninitialized` :  
	*	`cookie{..}` :  
		*	`maxAge` :  
	*	`rolling` : expiration reset at every response, e.g. for keeping user connected  
	*	`store` :  
		*	e.g.: `store: MongoStore.create({mongoUrl: env.MONGO_CONNECTION_STRING})` :  
		
`destroy(errorHandler: (error) => {})` : destroy session (with error handler)  
