# OBJECTS

## cv2

`inpaint(img, mask, radius, flags)` :  
`resize(img:npArray, shape:Tuple)` :  

### conversion

`cvtColor(img, format)` : convert to `format`

### drawing

`circle(img, center, radius, color, thickness)` :  
`line(img, corner1, corner2, color, thickness)` :  
`polylines(img, points, draw_lines, color, thickness)` : draw any polygon  
*	`points` : list of coordinates
*	`draw_lines` : `True` also draws lines between points

`putText(img, text, corner1, fontsize, scale, color, thickness)` :  
`rectangle(img, corner1:Tuple(int,int), corner2:Tuple(int,int), color:Tuple(int,int,int), thickness:int)` : draw rectangle on `img`
*	`color` : as rgb

### formats

`COLOR_BGR2HSV` :  
