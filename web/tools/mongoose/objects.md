# OBJECTS

## TYPES
`InferSchemaType<typeof schemaInstance>` : obtain schema type from schema instance  
`model<TYPE>("TYPE", schema)` : to export schema, with associated type  
*	e.g.: `type Type = InferSchemaType<typeof TypeSchema>` : create correct Type  

### Document
`deleteOne()` : remove from DB  
`remove()` : (?? not existing)  
`save()` : save document in DB  

### Model
`modelName` : model name  
*	e.g.: =collection name (usually)  


### Schema
`Schema(PARAMS)` : schema constructor, creating schema with PARAMS elements, as arrays  
*	each PARAM contains elements ELEM: PARAM={ELEM1: {...}, ...}
*	ELEM contains:
	*	`required: Bool` : if required  
	*	`select: Bool` : not returned by default  
		*	e.g. : hide user's password  
	*	`timestamps: Bool` : automatically save tmiestamps  
		*	e.g.: `{title:{...},text:{...}},{timestamps:true}` : put outside  
	*	`type: TYPE` : type  
	*	`unique: Bool` : must be unique in db    

`create({FIELDS})` : instantiate schema with fields; return a promise  
*	note: no need for `exec()` (not a query)  
`find()` : find query, i.e. return all elements which match filter  
*	note: to use return val as var, need to call `.exec()`  
`findById(id)` : find, with id  
`findByIdAndUpdate(ID)` :   
`Bool isValidObjectId(ID)` : if ID in valid format for mongoDB  

#### Schema.Types.ObjectId
`ObjectId` :  

`equals(otherId)` : compare  

## DATABASE
`Promise connect(URL)` : connect to mongoDB URL  

### QUERIES
`Query` : object  
#### methods
`exec()` : execute query  
`select("str"): Query` : also select specified fields  
*	e.g.: `findOne({username:name}).select("+password +email")` : also return passw, email (normally only username)  
