# OBJECTS

## /etc/nginx/*.conf

### server

`server {PROPS}` : declare server

`listen PORT` :  
`listen PORT default_server` : ?  

`client_max_body_size SIZE` :  
*	`SIZE=*M` : mb

`charset CHARSET` :  
*	e.g.: `CHARSET=utf-8` :  

#### location

`location LOC {PROPS}` : location (in server)
*	when matched `DOMAIN/LOC` this is selected  
*	locations are read and tried to match in order

`location ^ LOC {PROPS}` : match prefix 
*	e.g.: `location ^ /a` : also matches `DOMAIN/a/b`

`location ~ LOC {PROPS}` : match regex  
`location ^~ LOC {PROPS}` : match both ?  

`alias PATH` : map `LOC` to `PATH` on machine  
`proxy_pass URL` : redirect as a proxy  
*	e.g.: `URL=http://service:800` : redirect to a docker service named `service` on port `800`

`proxy_pass_header Server` :  
`proxy_redirect off` :  
`proxy_http_version 1.1;` :  
`proxy_connect_timeout 7d;` :  
`proxy_send_timeout 7d;` :  
`proxy_read_timeout 7d;` :  

`proxy_set_header NAME VAL` : add header `NAME` with `VAL` to the request before redirecting to `LOC`
*	e.g.: `proxy_set_header Connection "upgrade";` :  
*	e.g.: `proxy_set_header Host $http_host` :  
*	e.g.: `proxy_set_header Upgrade $http_upgrade;` :  
*	e.g.: `proxy_set_header X-Real-IP $remote_addr` :  
*	e.g.: `proxy_set_header X-Scheme $scheme` :  
*	e.g.: `proxy_set_header X-Forwarded-Proto $scheme;` :  
*	e.g.: `proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;` :  

`internal` :  
`add_header NAME VAL` : add header `NAME` with `VAL` to request before returning to client
*	e.g.: `add_header Content-disposition "attachment"` :  
