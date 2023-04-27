# BASICS.MD

## install
`npm install --save-dev @types/express` : needed for typescript  

## CONCEPTS

### MIDDLEWARE
e.g. error handler function  
for async: callable in promise `(req, res, next)` with `catch(error) {next(error);}`  
for sync: no need for `try...catch` and call to `next()`  