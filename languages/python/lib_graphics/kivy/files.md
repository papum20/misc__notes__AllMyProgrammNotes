# FILES

## README.md  
*	[README.md](./README.md)  

## BUILDOZER

https://www.youtube.com/watch?v=VsTaM057rdc&t=514s

-- install buildozer
-- download adb (android debug bridge)
	for Windows: use same version as in wsl

-- inside the project folder:
-- from wsl:
buildozer init : creates a .spec file in the current folder (containing a python project)

.spec FILE:
//set…
title : 
package.name : (no spaces)
requirements : required packages, with version
(for kivy, kivymd, not python, pillow (for logo))
(es.: python3, kivy==2.0.0, kivymd==0.104.1, pillow)

//first connect phone (usb) and turn on usb debugging in developer settings
-- from PowerShell:
./adb start-server : start server on connected phone
./adb devices : list of connected android devices (on server)

-- from wsl:
sudo mount -t drvfs C: /mnt/c -o metadata :
mount C drive to make next command work (windows)
buildozer -v android debug : compile apk


