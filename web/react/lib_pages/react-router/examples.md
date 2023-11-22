# EXAMPLES

A router with its declared paths used.  
*	note: `Nav.Link` using `href` refreshes the page, `Brand` with `as` not. 
```jsx
<BrowserRouter>
	<Route path='/' element={<MyComponent />} />
</BrowserRouter>
<Navbar>
	<Container>
		<Navbar.Brand as={Link} to='/'>Brand</Navbar.Brand>
		<Nav>
			<Nav.Link href='/'>a link</Nav.Link>
		</Nav>
	</Container>
</Navbar>
```