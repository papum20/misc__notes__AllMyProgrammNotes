# URI  
  
RISORSA in www:  
indipendente da meccanismo di memorizzazione;  
URI: identificatore risorsa.  
es.:  
risorsa=file in database, uri=chiave di ricerca;  
risorsa=risultato di un’elborazione, uri=parametri;  
risorsa=non elettronica (libro, persona…), uri=nome uniforme;  
  
URI (Uniform Resource Identifier):  
sintassi in www per definire nomi e indirizzi di oggetti (risorse) su Internet;  
oggetti accessibili con protocolli esistenti  
URI:  
URL (Uniform Resource Locator) : info immediatamente usabili per accedere a risorsa (es. indirizzo rete)  
OSS.: possono cambiare  
URN (Uniform Resource Names) : etichettatura permanente/verificata di risorsa  
OSS.: non cambiano, ma serve qualcosa per trasformare in link, che può cambiare  
progettati per essere:  
trascrivibili : caratteri alfanumerici  
fornire identificazione, non interazione :   
gerarchia dello spazio dei nomi :   
  
URI = schema : [//authority] path [?query] [#fragment]  
schema : (in URL: protocollo) prefisso fisso  
authority : se presente, indica gerarchia  
authority = [userinfo @] host [:port]  
userinfo : presente se schema prevede identificazione personale  
host : nome di dominio o ip  
port : può essere omessa se ci si riferisce a well-known port (http=8080)  
path : parte identificativa risorsa, in spazio di nomi dato da schema e authority  
dunque formato da /;  
importanti pseudo componenti “.” “..”  
query : parametri pe processamento (risorse dinamiche)  
fragment  : risorsa secondaria della primaria  
  
CARATTERI:  
tutti caratteri degli URI:  
curi : unreserved | reserved | escaped  
  
non riservati:  
unreserved : uppercase | lowercase | digit | punctuation  
punctuation : -_!~*’()  
  
riservati, che hanno funzioni particolari (vanno usati escaped altrimenti):  
reserved : ;/?:@&=+$,  
  
escaped:  
non US-ASCII  
di controllo (US-ASCII < 32)  
unwise []|\^[]’  
delimitatori spazio<>#%”  
riservati quando usati in contesto diverso dal loro uso riservato  
scrittura escaped:  
escaped : %XX  
	XX=codice esadecimale carattere  
  
ROUTE:  
associazione path - risorsa gestita / restituita da server web  
Managed route : server associa ogni URI a una risorsa, con  
file system locale (risorse statiche)  
computazione (risorse dinamiche)  
		es.: node.js, express.js  
File-system route : server associa radice di path a dir del file system locale  
ogni filename valido in dir genera un URI  
es.: vecchio approccio via web server (Apache, app. server-side di tipo LAMP)  
  
TIPI URI:  
URI assoluto : contiene tutte parti predefinite per suo schema, esplicitamente precisate;  
URI relativo (URI reference) : una parte di assoluto, che taglia progressivamente cose da sinistra;  
	fa sempre riferimento a uno di base  
(es. URI assoluto di documento ospitante l’URI reference)  
  
  
OPERAZIONI SU URI:  
URI resolution : input=URI -> output=URI  
	si esegue quando URI è un URI reference, o non corrisponde a risorsa fisica (non è URL)  
URI dereferencing : input=URL -> output=risorsa  
fornitura risorsa identificata da URI (es. documento cercato)  
  
(altro in slide unibo:)  
casi uri resolution  
schemi:  
ftp  
file  
data  
approfondimenti  
varianti di uri  
es. short uri  

## README.md  
*	[README.md](./README.md)  

