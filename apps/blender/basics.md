# BASICS  
  
NAVIGATION:  
  
SELECT: Left click  
DESELECT: click fuori  
SELECT ALL: A  
DESELECT ALL: Alt+A  
ROTATE VIEW: Middle mouse+drag / assi in alto a destra  
MOVE VIEW: Middle+Shift / maninaF  
STANDARD VIEW su selected: View -> Frame selected / Numpad .  
ZOOM: lente ingrandimento / scroll mouse / numpad +/-  
CAMERA: camera / numpad 0  
GRID: switch perspective / no perspective mode  
  
EDITOR:  
  
EDITOR TYPE: in alto a destra  
SPLIT AREA / JOIN AREAS: Right click on boundary  
FOCUS ON AREA: Ctrl+Space  
TOOLS: T / Shift+Space (labelled)  
altro menu: N / drag da destra  
altro menu -> view -> 3d cursor: Shift+Right piazza cursore  
altri menu: Z, Shift+S  
SCENE: in alto a destra: più scene  
MENU A DESTRA: tool selected, rendering engine, output, view, global scene, global(sfondo), SOLID[object, predefined modifiers, particles, physics, constraints,mesh data(forma?),material]/LIGHT[..data],texture  
  
SELECT OBJECTS:  
SELECT MULTIPLE OBJECTS: selection box (tool 1) / B+drag mouse / C+drag mouse (come brush)  
ADD/DELETE ONE FROM SELECTION: Shift+Left  
CHOOSE ACTIVE OBJECT: Shift+Left  
WIREFRAME: in alto a destra  
  
TRANSFORM:  
ANNULLA MENTRE LA STAI FACENDO: Right  
MOVE/TRANSLATE: Move tool (assi (X/Y/Z, mentre free), piani (Shift+X/Y/Z mentre free) o liberamente (G) )  
ORIGINAL POSITION: Alt+G  
ROTATE: Rotate toot (R: lungo vettore, R di nuovo: free, oppure assi XYZ)  
ORIGINAL ROTATION: Alt+R  
SCALE: (S, Alt+S, S tool)  
CURSOR (TRANSFORMATION CENTER): CUrsor T -> Shift+Right; 3D Cursor in alto  
MOVE TO CURSOR: Object -> Snap -> ..to cursor / Shift+S  
ORIGINAL: Shift+S menu  
CHANGE AXIS AFTER ROTATION: Orientation in alto / press twice X/Y/Z  
PRECISIONE: Shift durante trasformazione  
SNAP: (Shift+Tab / in alto) ?  
  
ADD OBJ.:  
ADD(in alto) / Shif+A  
DELETE: Object -> delete / X / Canc  
EDIT MODE: (in alto a destra) delete è diverso  
DUPLICATE: Shift+D  
  
COLLECTIONS (GROUPS):  
ALLARGA/STRINGI: Numpad +/-  
MOVE TO COLLECTION: Right su obj / M  
NEW COLLECTION: C (su una collection)  
VIEW LAYER  
DUPLICATE AND MOVE TO ANOTHER COLLECTION (LINK TO C.): Shift+drag  
UNLINK  
  
  
WORKSPACES:  
MODEL: edit mode  
SCULPTING: liberamente  
UV..: x teexture  
TEXTURE PAINTING  
SHADING: texture, preview (=lock dev / Z..)  
ANIMATION: anima (es. sposti..)  
RENDER: result  
COMPOSITING: post-processing / effect  
SCRIPTING: code  
  
EDIT MODE:  
ADD EDGE: F  
JOIN: obj(in alto) -> join  
SEPARATE: lo stesso  
SELECTION MODE: (in alto a sinistra, 1,2,3)  
LOOP SELECTION: Alt+...  
EXTRUDE: E  
EXTRUDE VELOCE: Ctrl+Right  
CUT: Ctrl+R (wheel x aumentare n tagli)  
KNIFE: E/double Left to disengage, Space/Enter to confirm  
SUBDIVIDE: Ctrl+2 (es. trasforma cubo in sfera)  
  
SHADING:  
RENDER MODES: eevee (potente, fisica, come giochi), cycles (luci), workbench (preview)  
VELOCE: view -> viewport render  
COLLEGAMENTI SCHEMI: Ctrl+drag (x già fatto), F (dopo aver selezionato)  
SCHEMI: texture -> gradient t. (colore), color -> mix RGB (mischia texture)  
MUTE NODE: M  
DELETE WITH RECONNECT: Ctrl+X  
LINKS CUT TOOL: Ctrl+Right drag  
TRANSPARENCY: link to alpha; material menu a destra -> settings -> blend mode: alpha..  
Edit mode, uv mode(in basso a destra)  
  
3 LIGHTS RULE:  
base? : base  
rigging: contorno : dietro, molto forte  
fill: lato opposto, debole, x non ombre troppo forti  
  
PROPERTIES:  
RENDER ENGINES:  
RENDER: F12  
EEVEE:  
film -> transparency ( tipo per il cielo)  
simplify  
freestyle  
color management  
CYCLES:  
device: CPU/GPU x render  
light paths (accuracy light / render time)  
volume  
hair (particles)  
performances (tiles)  
bake  
WORKBENCH:  
Lightning (matcap)  
color (random)  
options  
  
OUTPUT:  
RENDER REGION: standard: camera, change: view -> view regions -> render region / Ctrl+B  
CLEAR RENDER REGION: view -> view regions -> clear.. / Ctrl+Alt+B  
CROP TO RENDER REGION: il resto non diventa trasparente ma qualcos’altro?  
FRAME START, END, STEP, RATE  
TIME REMAPPING: ?  
STEREOSCOPY: 3D glasses  
output -> METADATA  
BURN INTO IMAGE: conferma metadata  
OUTPUT:  
	PLACEHOLDERS: crea file prima che sia finito  
	CACHE..: crea file cache, che velocizza render  
	se video: encoding -> audio -> ricorda di mettere audio codec  
  
RENDER: CYCLES:  
RENDER: regola precisione/tempo  
OROLOGIO AFFIANCO A SEED: migliora  
DENOISE: denoise  
  
RENDER: EEVEE:  
AMBIENT OCCLUSION: realismo; distance = distance from corners(?); factor -> + scuro;   
BLOOM: forte emissione di luce, riflessione (x vedere effetti: aumenta emission/metti surface: emission): threshold: soglia minima; knee: gradual threshold; radius, color, intensity, clamp: max (se != 0)  
DEPTH OF FIELD: select camera -> go to camera properties: focus distance  
SUBSURFACE SCATTERING: samples = qualità; material -> subsurface al max + settings->subsurface translucency; jitter threshold: randomizza  
SCREEN SPACE REFLECTIONS: riflessi pavimento (Material pavimento -> -roughness); trace precision: quality (x noise: sampling -> viewport); mx roughness: what’s above wont display reflections; half res trace: worse and faster; refraction: rifrazione (x vetro) (vetro: material: glass; settings: screen space refraction; refraction depth regola)  
MOTION BLUR  
VOLUMETRIC: (volumetric texture: surface remove, volume: volume scatter; density) start/end: limiti entro cui si vede; tile size, samples : quality; distribution: edge quality  
SHADOWS: cube size: quality; cascade size: quality solo x sun light; high bitdepth: quality; soft shadows: soft borders; light threshold  
INDIRECT LIGHTING: add -> reflection cubemap: riflessi di oggetti su oggetti; refl. plane: like surface..;  
  
RIGGING:  
CONSTRAINTS PROPERTIES  
  
PARENTING:  
parent: ctrl+P select prima figlio e poi padre)  
se duplichi figlio avrà stesso padre  
annulla: Alt+P (clear and keep transformation x keep transformation)  
  
ARMATURES:  
HIDE: H  
MODES: pose, edit (Tab / Ctrl+Tab)  
HEAD (sotto, centro), BODY, TAIL (edit mode x seleziona parti)  
PARENT (HEAD-TAIL) / SUBDIVIDE (Right) / EXTRUDE (E)  
DISCONNECT (Alt+P): clear parent / bones (non clear parent)  
ROLL: =rotate lungo asse (assi: object data properties -> viewport display -> axes) (bone properties: rotation)  
BONE SIZE: (obj data prop. -> viewport display -> display as B-Bone/Envelope)  
X ANIMAZIONE: Pose Mode: Right -> INSERT KEYFRAME -> location, rotation and scale  
Object Mode: Parent -> Armature deform (Automatic o altro) (selez prima corpo poi armature)  
  
CONSTRAINTS:  
es.: COPY rotation, location.. (invert, space); disable influence -> keep when delete constraint  
LIMIT.. : limite (affect transform x non far andare oltre i limiti, altrimenti ci va lo stesso anche se non lo vedi)  
X BONES: Pose mode -> bone constraints prop. (maintain volume, limit distance)  
TRACK TO: oggetto guarda sempre target  
LOCKED TRACK: track solo per due assi  
STRETCH TO: allunga se si allontana  
DAMPED TO: =dampedparent  
CLAMPED TO: (target: curve) obj segue curva (segue path)  
TRANSFORMATION: combina copy loc/rot/sca; (Extrapolate x far continuare all’infinito)  
LIMIT DISTANCE: (clamp region: inside/surface/outside: dove sta obj)  
MAINTAIN VOLUME: changes shape to maintain volume  
  
HUMAN SKELETON (ADD-ON):  
PIVOT POINT (in alto): (median -> 3D cursor(cursor to world origin: Shift+S -> ..) )  
menu nascosto a destra -> tool -> options -> X-axis mirror: quello che fai a sinistra si fa speculare (simmetrico)  
X OSSA PER BENE: (armature) obj data prop. -> generate rig; then parent (cosi puoi mettere constraint)  
  
ANIMATION: INVERSE KINEMATICS:  
(opposite: FORWARD KINEMATICS: parent influenza figlio, non contrario)  
INVERSE: figlio influenza parent, non contrario (menu nascosto a destra -> auto IK x fare veloce, ma non va bene x animaz.)  
BONE CONSTRAINTS PROP.: (es. x hand) Inverse kinematics -> target: armature; bone: hand; disconnect hand but not unparent; set chain; create new hand: unparent and make it target; copy rotation constraint (real hand copies second); duplicate second hand and put it behind the elbow: set it as pole (x ik constraint); set pole angle so elbow points to false elbow  
x elbow: bend it slightly backwards; angle constraint  
  
WEIGHT PAINT (MODE):  
select prima armature, poi mesh, poi metti weight paint  
BRUSH: cambia zone influenza; menu alto a destra: weight: color; radius, strength; advanced -> front faces only; falloff: pitta anche dietro (2d falloff a me non ci sta); puoi modificare zone influenza anche da edit mode -> object data properties -> vertex groups  
BLUR: più soft  
AVERAGE: soft, ma average  
SMEAR: carry weights from one place to another  
GRADIENT  
vertex group: può essere usato x modifier (es. wireframe)  
  
BONE LAYERS:  
obj. data properties  
MODIFICA: Pose mode: Pose-> change bone layer / press M  
BONE GROUPS: sempre là (colori…)  
  
KEYFRAME:  
INSERT: I / Right -> insert keyframe / obj properties -> Right on mode / autoframe (pallino su barra in basso)  
SELECT FRAME: frecce / Alt+scroll wheel / drag  
PLAY/PAUSE: Space  
DUPLICATE FRAME: Shift+D  
CHANGE SPEED: select all (A) -> S (size) (puoi anche premere un numero uguale al rapporto)  
(Right -> delete (all) keyframes / Alt+I)  
Right -> Keyframe type -> COLOR  
es. bouncing ball: Right quando tocca terra -> HANDLE TYPE (V) -> vector  
USE PREVIEW RANGE: (icona orologio)  
MARKER (edit: select -> click marker)  
Playback -> No-Sync / (Frame dropping (-fps x - lag), AV (audiovideo) sync)  
ADD AUDIO: workspace: video editing -> video editing (view -> waveform display (non so perché))  
KEYING: (keying set, key type, ..)  
  
DOPE SHEET:   
(animation workspace / editor type in alto a sinistra)  
forma: handle type (cerchio: auto clamped, square: vector)  
INTERPOLATION MODE: T (constat, bezier)  
SELECT COLUMN OF KEYFRAMES: Alt+Left  
CHANNEL: =group (Ctrl+G)  
UNGROUP: // / Ctrl+Alt+G  
icone in alto a dope sheet: mostra solo selezionato; mostra nascosti;   
metti a posto visuale: tasto Home / View -> frame all  
View -> SET PREVIEW RANGE: =tasto orologio  
View -> SHOW SLIDERS: mostra slider keyframe modificabile  
View -> SHOW CURVE EXTREMES: mostra andamento nei pallini  
  
GRAPH: (graph editor / View -> toggle graph editor / Ctrl+Tab) curve (interpolation modes) (anche modificare)  
Channel -> hide unselected curves (Shift+H)  
unhide: Alt+H  
MODIFIERS: (menu nascosto a destra):  
	NOISE: restrict frame range; influence, ..  
CHIAVE INGLESE AFFIANCO A KEYFRAME: modifier on/off  
lock icon: ..  
  
SCULPT MODE (EDITOR):  
Ctrl+Left: effetto opposto  
Shift+Left: smooth effect  
F: scale brush  
Shift+F: strength  
brush -> reset brush (options) (F3 -> cerca opzione)  
togliere cosa antipatica che si sminchia quando muovi visuale: options -> fast navigate off  
BRUSHES:  
	DRAW: normale  
	CLAY: più piatto  
	CLAY STRIPS: clay, ma quadrato  
	LAYER: ha un limite  
	INFLATE: toglie flat (utile x cose sottili x es)  
	BLOB e CREASE: magnify (?)  
	SMOOTH: fa average x smooth (come quando premi Shift)  
	FLATTEN:  
FILL e SCRAPE (opposti): aggressive  
PINCH: (tipo blob?)  
GRAB  
SNAKE HOOK: (rake: segue rotation brush)  
THUMB: (tipo grab)  
ROTATE: vortici  
MASK: places mask che impedisce di modificare quell’area (Ctrl+M: hide, Ctrl+I: alterna, ALt+M: remove)  
BOX MASK: uguale  
BOX HIDE: nasconde una parte  
	ANNOTATE  
brush settings: brush -> autosmooth; accumulate: remove strength limit: puoi sculpt all’infinito; texture (mapping: way texture projected; angle; rake); stroke -> spacing distance: uniforme; stabilize stroke; falloff; cursor: look; DYNTOPO: autogenera poligoni, so you never run out (resolution, detailing); resolution modifier  
  
  
  
  
  
MODIFIERS:  
MIRROR: clipping: riempie centro; mirror object  
SUBDIVISION SURFACE: smooth e più detail  
  
SHADING:  
uv -> pack uv islands: raggruppa e ordina  
uv -> average.. fa tutti di dimensioni medie  
  
TEXTURE PAINT:  
options (alto a destra) -> bleed: 6px (espand paint fino a 6 pixel)  
  
camera/lights:  
N menu -> camera to view: ?  
  
  
  
  
  
ZOOM PROBLEM:  
preferences -> navigation -> enable auto depth  

## README.md  
*	[README.md](./README.md)  

