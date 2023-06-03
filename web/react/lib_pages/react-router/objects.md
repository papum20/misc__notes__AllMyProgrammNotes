# OBJECTS

## HTML TAGS
`BrowserRouter` : main tag, wrapping pages and all contents  

`Link` : link, but don't refresh all page (like `href`), just replace right content  
*	`to="LINK"` : (required)  

`Routes` : container of `Route` elements  

`Route` : add route  
*	`path='..'` : path for routing  
*	`element=..` : element to show  

## Route
// Route object

`Route` :  
*	`path: string` : pattern which matches an the url  
*	`index: boolean` : if true, showed in parent's outlet  
*	`children: React.ReactNode` :   
*	`caseSensitive: boolean` : path case sensitive  
*	`id: string` :   
*	`loader: LoaderFunction` : executed before rendered;
*	`action: ActionFunction` : called when form submitted  
*	`element: React.ReactNode | null` : page element to load (defined here)  
*	`Component: React.ComponentType | null` : like element, but just "called" (by name)  
*	`errorElement: React.ReactNode | null` : declare error element, showed when thrown error by loader/action  
*	`ErrorBoundary: React.ComponentType | null` : use if want to use default error  
	*	`=ErrorBoundary` : default  
*	`handle: RouteObject["handle"]` :   
*	`shouldRevalidate: ShouldRevalidateFunction` :   
*	`lazy: LazyRouteFunction<RouteObject>` :   

`useLoaderData()` : use data loaded (returned) by loader  