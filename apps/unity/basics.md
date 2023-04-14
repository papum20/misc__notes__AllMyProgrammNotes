# BASICS  
  
## README.md  
*	[README.md](./README.md)  

## COMPONENTS  
  
Audio source : (play on awake; loop)  
Particle System : (start lifetime,rotation,speed,size:(random between 2 constants), gravity modifier; simulation space:world; shape -> shape:edge; emission -> rate over time; velocity over lifetime -> linear; color over lifetime; renderer -> material;)  
  
## Universal RP  
  
Universal Renderer Pipeline Asset, 2D Renderer..  
Global Volume : new profile-> add override-> post-processing-> bloom (bright)  
  
## ANIMATIONS  
  
ANIMATOR:  
Controller : Animator controller referring to  
Avatar : (for retargeting animations to another character)  
Root motion : if true: movement is animation based instead of script based   
(e.g.: walking animation makes character move, but it only moves if root motion is on)  
Update Mode :	Normal : animation depends on time scale  
			Animate Physics : animation happens in fixed update  
(for animation involving physics)  
			Unscaled Time : not depending on time scale  
					(for UI)  
Culling Mode :	Always Animate : animation continues even when  
not targeted by camera  
			Cull Update Transforms : animation stops when not in view,  
but it still keeps calculating, so when it will be in  
view again the position will be as it continued animating  
			Cull Completely : when not in camera, stops completely, so when  
comes in camera again continues animating from  
the point it stopped  
  
  
TRANSITION:  
Solo : if true: this transition is the only playable  
Mute : if true: transition disabled  
Has Exit Time : if true: a minimum percentage of the current animation has to be completed  
in order to perform transition  
	Exit Time : “the percentage”  
	Transition Duration : -  
	Transition Offset : from which part of animation it starts (in percentage)  
	Interruption Source : if true: can start another transition while this is still happening  
  
## PHYSICS  
  
COMPONENTS :  
(Colliders) :  
Direction :  
  
Character Joint :  
Edit Joint Angular Limits : constraints for movement  
Connected Body : (Rigidbody)  
Axis : for rotations  
  
Physics Material :  
  
  
WINDOW :  
Physics Debugger :  
Window -> Analysis -> Physics Debugger  
Show All : show all  
	Collision Geometry : colliders  
	Mouse Select : allow to select colliders by hovering over them  
	Colors :  
	Rendering :  
		Transparency :  
  
[RAGDOLLS] :  
-- requires each part of a model/body to have rigidbody, character joint, collider  
-- physics material (especially for all parts of limbs and head):   
-- for problem when parts glitch through something: set collision detection to continuous  
  
SIMPLE VERSION (JUST FOR HUMANOIDS) :  
GameObject -> 3d -> Ragdoll  
// fill with model rig parts, mass and it creates joints and colliders  


