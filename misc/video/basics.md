# BASICS

"What you see".  

## colors

`hsv` : hue, saturation, value (all in range `[0,255]`)  

## image features

`brightness` : light intensity
*	note: it's relative to the person, differently from `luminance`

`interpolation` : 
*	`img1*c+(1-c)*img2` : apply interpolation with coefficient `c` (in range `[0,1]`)

`luminance` : light intensity of an image or a color (`cd/m**2`)
*	`color+brightness` : apply to a color

`saturation` : intensity/purity of the colors of an image
*	`img*saturation` : apply saturation, where `img` is represented as colors (e.g. **rgb**), and `saturation` is a scalar
