# OBJECTS

## TYPES
`InferSchemaType<typeof schemaInstance>` : obtain schema type from schema instance  
`model<TYPE>("TYPE", schema)` : to export schema, with associated type  
*	e.g.: `type Type = InferSchemaType<typeof TypeSchema>` : create correct Type  

### Document
`deleteOne()` : remove from DB  
`remove()` : (?? not existing)  
`save()` : save document in DB  

### Schema
`Schema(PARAMS)` : schema constructor, creating schema with PARAMS elements, as arrays  
*	each PARAM contains elements ELEM: PARAM={ELEM1: {...}, ...}
*	ELEM contains:
	*	`required: Bool` : if required  
	*	`timestamps: Bool` : automatically save tmiestamps  
		*	e.g.: `{title:{...},text:{...}},{timestamps:true}` : put outside  
	*	`type: TYPE` : type  

`create({FIELDS})` : instantiate schema with fields; return a promise  
*	note: no need for `exec()` (not a query)  
`find()` : find query, i.e. return all elements which match filter  
*	note: to use return val as var, need to call `.exec()`  
`findById(id)` : find, with id  
`findByIdAndUpdate(ID)` :   
`Bool isValidObjectId(ID)` : if ID in valid format for mongoDB  

## DATABASE
`Promise connect(URL)` : connect to mongoDB URL  

### QUERIES
// query objects methods
// `QueryObject.METHOD()`
`exec()` : execute query  
