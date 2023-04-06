# OBJECTS  
  
## FUNCTIONS 
  
UNITY  
  
CancelInvoke(string “FunctionName”) : cancel invokeRepeating  
Destroy(GameObject) : destroy obj  
DestroyImmediate(GameObject) : x editMode  
InvokeRepeating(string “FunctionName”, time start, delta time) : repeats function string every delta time, starting from start  
StartCoroutine(IEnumerator function) : esegue function in un solo frame  
  
  
  
private void OnCollisionEnter2D(Collision2D collision) : quando c’è collisione  
private void OnTriggerEnter2D(Collider2D collision)  
OnEnable()  
OnDisable()  


GetComponent <component>() : ottieni component dell’obj  


## CLASSES
  
Animator :  
.setBool(string, value) : sets var named string to value  
.setFloat()  
  
Camera:  
(camera).screenToWorldPoint(Vector2)  
  
Debug :  
.Log(...)  
//.Log(<color=”#XXXXXX>expression</color>”) : prints expression in specified color  
  
GameObject :  
.activeSelf : locally active (inactive even if active but parent inactive)  
.activeInHierarchy : independent by parent if active or not  
  
GraphicRaycaster :  
.Raycast(EventSystems.PointerEventData eventData, List<RaycastResult> resultAppendList) : Raycast for UI  
  
Input :  
.mousePosition : Vector3  
  
LineRenderer :  
.positionCount = int : number of vertices  
.SetPosition(int i, Vector3 v) : sets v as position of vertex in index i  
  
Mathf :  
.Cos(float angle) : angle in radians  
  
Physics2D :  
.Raycast(Vector2 start, Vector2 direction, float maxDistance, LayerMask lm)  
  
SpringJoint2D :  
.distance  
  
Texture2D :  
.GetPixel(int x, int y) : Color //IMPORTANT: starts from bottom left corner of screen  
  
Transform :  
.LookAt(Transform target)  
.RotateAround(vector rotationPoint, vector rotation axis, int angle) : rotate around point  
.SetAsFirstSibling() 	: order in hierarchy  
.SetAsLastSibling() 	: 	//  
.SetSiblingIndex(int) :	//  
.TransformPoint(Vector3) : punto da local a global  
.translate(vector) : trasla di vettore direzione  
  
Vector3 / Vector2 :  
.Distance(Vector3, Vector3)  
.Magnitude : float length of vector  
.Normalized : Vector3 direction  
  
  
Vector3Int / Vector2Int :  
.RoundToInt(Vector3) : from Vector3 to Vector3Int  
  
  
  
  
  
  
  
Application :  
.isPlaying : bool se app is running  
  
.Quit() : chiude app  
   
  
AudioSource :  
.Play() : play audio  
  
  
Camera :  
.main : main camera  
(.main?).ScreenToWorldPoint : converte da pixel a world  
  
  
Collision :  
.contacts : array con punti di contatto (.point)  
.gameObject.tag : tag di obj con cui collide  
  
  
component :  
.enabled : bool se component attivo  
  
  
Color :  
  
  
Convert :  
conversioni  
  
Cursor :  
.visible = bool  
.lockState = cursorLockMode.(...) : None, Locked, Confined  
  
Debug :  
.Log(text) : scrive text in console  
  
  
ForceMode :  
.Force : constant force  
.Impulse  : instant force  
  
  
  
ForceMode2D :  
.Force : constant force  
.Impulse  : instant force  
  
  
GameObject :  
.tag  
.transform(.position) :  
  
.FindGameObjectWithTag(string) : obj named string  
.GetComponent<>() : get component (es Rigidbody2D)  
  
.Instantiate(cosa(GameObject), dove(vector posiz), rotaz, parent) : crea obj  
.setActive(bool) : setta obj attivo/disattivo  
  
  
Input :  
.GetAxis() : tra -1 e 1  
.GetAxisRaw() : -1, 0 or 1  
.GetButtonDown() : button impostati in input  
.GetKey(key) : (KeyCode.nomeTasto) se è premuto  
.GetKeyDown(key) : alla pressione  
.getMouseButtonDown(button) : es 0 = mouse sx  
.GetTouch(int index) : get touch  
.touchcount : numero di tocchi contemporaneamente  
.touches : array tocchi  
  
  
Int :  
.toString()  
  
LoadSceneMode :  
.Additive  
.Single  
  
  
Mathf :  
.Abs()  
.Ceiling()  
.Clamp(float x, float min, float max) : dà x se compreso tra estremi, se no estremi  
.RoundToInt()  
  
  
ParticleSystem :  
.Play()  
  
  
Physics2D :  
.OverlapCircleAll(center, radius, layermask) : cast cerchio intorno  
.Raycast(position, direction) : crea raycast  
  
.RaycastHit2D  
  
  
PlayerPrefs :  
GetInt()  
SetInt(string name, int value)  
  
  
Quaternion : rotazioni  
.identity : zero  
  
.LookRotation(direz, verso) :  
  
  
Random :  
.range()  
  
Renderer :  
.isVisible: bool se visibile  
  
  
  
Rigidbody :  
.AddForce(Vector, ForceMode.mode) : add forza  
  
  
Rigidbody2D :  
.AddForce(Vector2, ForceMode.mode) : add forza  
  
  
SceneManager :  
.GetSceneByName(string) : get scene  
.LoadScene(string, (optional) LoadSceneMode.* ) : carica (metti) scene; * = Single:sostituisce; Additive: aggiunge scena a presenti  
.SetActiveScene(scene) : active scene x instantiate  
.UnloadScene(string) : togli scene  
  
  
  
Screen :  
.SetResolution(width, height, bool windowed, framerate)  
  
SpriteRenderer :  
  
  
Text :  
.text : testo  
  
  
Time :  
.deltaTime : tempo x frame  
.time : tempo tot  
.timeScale : moltiplicatore tempo  
  
  
Touch :  
.position : in pixel  
.phase : stato  
  
  
ChildCount : numero figli  
.position  
.rotation  
.scale  
  
  
Vector(2/3) :  
.ClampMagnitude(int maxLength) : massima distanza vettore  
.Distance(Vector3 v1, Vector3 v2) : distanza 2 punti  
  
.normalized : ha modulo 1  
.up / down / left / right : vettori direzioni  
  
  
Vector(2/3)Int :  
  
  
  
  
  
  
Resources.Load(string) : string = nome obj to load  
