HTTP:  
Hyper Text Transfer Protocol  
tipo Stateless: richiesta indip da altre  
  
HTTPS: cripta  
  
URL:   
http://foobar.com:8080/view.php?id=1  
http : schema  
foobar.com : host  
8080 : port (8080=http)  
view.php : URL-path: file being accessed  
id=1 : (after ?) parameter (more separated by &)  
  
URL Encoding : for special chars (%hex)  
  
TOOL: cyberChef : many tools  
	e.g. URL Decode  
  
—  
  
METODI RICHIESTE:  
request line  
header fields  
body field  
  
GET:  
dati nell’url  
facile ripetere, riprendere  
non sicuro  
salva in cronologia  
lunghezza limitata (2083 char)  
  
POST:  
nel body  
sicurezza, privacy  
bisogna reinserire (es form)  
  
HEAD:  
solo campi header (es utile per data)  
  
OPTIONS:  
metodi permessi per interazione con una risorsa  
  
  
RISPOSTA:  
Status-line  
header fields  
body field  
  
ERRORI:  
1xx  
2xx  
3xx  
4xx  
5xx  
200  
400  
404  
500  
  
COOKIE:  
stringhe di testo che Client e Server si scambiano ad ogni richiesta  
gestione sessioni  
tracking  
  
composti da:  
nome  
caratteri alfanumerici  
meta–info:  
origine: dove nasce  
scadenza  
altro  
  
TOOL: burp  
  
  
testing…  
blackbox: senza sapere niente, senza avere codice (si prova a “rompere”..)  
whitebox: si ha codice, si può debuggare  
  
COMMAND e CODE INJECTION/SUBSTITUTION:  
input utente eseguito e interpretato da app vittima  
substitution: es. $(command) / ‘command’ : valuta  
  
sanificazione codice: analizzare prima di eseguire  
  
[challenge 1 : localhost]  
  
BROWSER:  
firefox:  
inspect -> network -> edit & resend : puoi vedere tutte le richieste, e resend (firefox si, chrome no)  
ctrl+U : codice sorgente  
console : interact with javascript  
debugger (chrome: source) : ?  
network : scambio pacchetti  
  
BURP:  
PortSwigger  
webhook: server hoster  
ngrok: host a server in local  
crackStation : cose già hashate  
PayloadsAllTheThings : vulnerabilità  
hacktricks : vulnerabilità  

## README.md  
*	[README.md](./README.md)  

