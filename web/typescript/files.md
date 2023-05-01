# FILES

## SOURCE
`.ts` : source files extension  

## TYPES
`.d.ts` : types definition  
*	e.g.: in `@types/` : help ts recognize type definitions  
*	note: for npm, in tsconfig.json, edit `typeRoots`: defaults to `node_modules/@types`, add `@types` folder  
*	note: for `ts-node` and npm, in tsconfig.json, add `{{all_pkgs..}, "ts-node": {"files":true}}`  