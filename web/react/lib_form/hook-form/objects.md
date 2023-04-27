# OBJECTS

## FUNCTIONS

`useForm<Type1>(): { register, handleSubmit, formState : { errors, isSubmitting } }` :   
*	`register(name=Type1.field1, {options?})` : register? form with Type1's field1  
	*	`required: "Text"` : if required; Text is showed if missing required field  
*	`handleSubmit(onSubmit)` : handles submit, using own `onSubmit(input: Type1)` function  