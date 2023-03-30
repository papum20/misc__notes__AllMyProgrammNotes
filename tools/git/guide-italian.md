# GUIDE
## (in italian)
---

INSTALLAZIONE:  
Windows: cerca su Internet (installi un installer e fai quello che dice)  
Linux / WSL: comando: sudo apt-get install git  
(Potrebbe essere necessario riavviare VS code o il computer per far funzionare)  
  
INIZIALIZZAZIONE:  
-CREAZIONE REPOSITORY:  
repository := creazione di una “cartella” controllata da git, cioè che tiene traccia dei cambiamenti (ed eventualmente si può caricare e tenere sincronizzata su posti tipo GitHub)  
(dentro la cartella dove si vuole creare la repository) git init  
(nota: crea un file nascosto nella cartella)  
-CONFIG:  
usare questi comandi per configurare queste informazioni (necessarie) usate poi per segnare chi ha fatto i cambiamenti  
git config --global user.name <name> : inserirre nome  
git config --global user.email <email> : email  
-COLLEGAMENTO REPOSITORY REMOTA (GitHub):  
git remote add origin <link> : aggiunge in locale, sul pc, un collegamento a una repository remota (link tipo https://username/progetto…)  
oss.1: si deve essere proprietari/collaboratori/avere accesso a quella repository  
oss.2: dovrebbe chiedere un’autenticazione, tipo apre il browser e chiede di fare il login a GitHub  
-SCARICARE INTERA REPOSITORY:  
git clone <link> : sostituisce contenuto di una cartella (che deve già essere stata inizializzata con git init) con contenuto repository remota  
  
SALVARE/CARICARE/SCARICARE:  
-STATO FILE:  
ogni file passa attraverso questi stati:  
UNTRACKED (U) : file appena creato e non “registrato” per essere tenuto in considerazione quando si salva tutto  
ADDED (A) : file “nuovo”, non untracked, quindi appena “registrato”, ma mai salvato  
MODIFIED (M) : file già salvato qualche volta, è appena stato modificato e non salvato  
COMMITTED () : stato finale: il file è salvato e fa ora parte della cronologia dei salvataggi (quindi si può tornare avanti o indietro con i cambiamenti)  
-STRUTTURA A BRANCH:  
una repository git è strutturata come un albero, in cui ogni commitment costituisce un nodo, ovvero uno stato di salvataggio di tutti i file in cui si può tornare (indietro o in avanti); come un albero, presenta anche delle ramificazioni (branch): diciamo che siano stati fatti vari commitment fino a uno stato A, se da A si crea un branch chiamato tmp (oltre a quello principale che esiste sempre, chiamato master) la cronologia dei commitment sarà separata d’ora in poi, vale a dire che se in master si fanno dei determinati cambiamenti fino ad arrivare a uno stato B mentre in tmp se ne fanno di diversi fino a uno stato C, alla fine il ramo master avrà una cronologia di commitment uguale ad A+B, mentre tmp A+C: i due branch avranno dunque delle differenze nei file e ognuno non avrà accesso ai cambiamenti dell’altro (ma entrambi possono tornare allo stato A)  
-COMANDI IN LOCALE:  
git add file1.extension1 file2.extension2 … : fa passare da untracked a added tutti i file specificati come parametri …E… rende i file modified pronti per il commit  
git add * : fa l’add di tutti (tutti i file untracked / modified)  
git commit -m “string” : fa passare tutti i file pronti per il commit (di cui si è fatto l’add) a committed, registrandoli con la stringa specificata (tra virgolette)  
oss.: è utile mettere una stringa esplicativa che spiega i cambiamenti fatti  
git commit -am “string” : fa insieme l’add di tutti i file e il commit (non vale per i file untracked ma solo per i modified: gli untracked vanno prima aggiunti con add)  
git commit -m “string1” -m “string2” : permette di mettere due stringhe di descrizione  
git commit -am “string1” -m “string2” :  
-COMANDI PER REPO REMOTA:  
git push <remote_branch> <local_branch> : salva (sincronizza i cambiamenti) local_branch in remote_branch  
git pull <remote_branch> <local_branch> : contrario di push  
(solitamente) :	git push origin master :  
		git pull origin master :  
git push -u <remote_branch> <local_branch> : rende i parametri di default, così che se in seguito non verranno specificati saranno presi in automatico quelli messi dopo -u  
git pull -u <remote_branch> <local_branch> : lo stesso  
git push : vale se si è fatto almeno una volta con -u  
git pull : lo stesso  
NOTA: fare sempre pull prima di eventuali modifiche, commit e push (altrimenti si va a modificare una versione vecchia)  
  
ALTRI COMANDI:  
git branch : lista dei branch locali  
git branch <branch_name> : crea branch branch_name  
git branch -v : lista branch repository remota  
git branch -a : lista tutti branch (locali e remoti)  
git branch -d <branch> : delete branch  
git log : lista commitment branch attuale  
git log <branch_name> : log di quel branch  
git status : stato attuale, tipo quanti file sono untracked, quanti di cui fare il commit…  
git diff : differenze dall’ultimo commit  
git diff <branch/commitment> : differenza tra stato attuale e branch o commitment specificato  
git switch <branch> : cambia branch  
git checkout <commitment> : cambia branch (se inserito il nome di un branch) o commitment (se inserito l’hash di un commitment come quelli che escono scritti in log)  
git merge <branch> : unisce branch a master (ovvero crea una cronologia unica e integra i cambiamenti dei due branch in qualche modo; potrebbero esserci dei conflitti (se hanno dei cambiamenti diversi) e in tal caso si devono rimuovere manualmente le parti che creano conflitto)  
