#Esercizi su metodi e funzioni delle stringhe

nome = input("come ti chiami? ")

#A L I B A B A
#0 1 2 3 4 5 6
cognome = input("cognome? ")
#stampa numero dei caratteri #len è una funzione
print(len(nome))
#i seguenti sono tutti metodi
#prima occorrenza di un singolo carattere #posizione della lettera "a" nel nome digitato #si parte da 0
print(nome.find("a"))
#prima occorrenza di una substring
print(nome.find("ab"))
#ultima occorrenza di un singolo carattere
print(nome.rfind("l"))
#ultima occorrenza di una substring
print(nome.rfind("ba"))
#trasforma in MAIUSCOLO
print(nome.upper())
print(cognome.upper())
#trasforma in minuscolo
print(nome.lower())
print(cognome.lower())
#trasforma la prima lettera in maiuscolo e tutte le successive in minuscolo
print(nome.capitalize())
print(nome.capitalize() + " " + cognome.capitalize())
#controlla se sono tutte lettere
print(nome.isalpha())
#controlla se sono tutti numeri
print(cognome.isdigit())
#controlla substring iniziale
print(nome.startswith("A"))
#controlla substring finale
print(nome.endswith("ba"))
#conta il numero di occorrenze di una substring
print(nome.count("a"))
#conta il numero degli spazi nella stringa
print(nome.count(" "))
#sostituisce una substring con un'altra
print(nome.replace("a", "u"))
print(cognome.replace('"' , "'"))

#carattere di escape (\)
#indica di considerare cio' che segue letteralmente e non come funzione sintattica
print("manzoni ha scritto i \"promessi sposi\"")
#metodo furbo invertire le (") con (')
print('manzoni ha scritto i "promessi sposi"')
#metodo furbo non applicabile quando sono presenti entrambi i caratteri (" e ')
print("manzoni ha scirtto i \"promessi sposi\" sotto l'albero")

#rimuove gli spazi all'inizio e alla fine della stringa
print(nome.strip())
#rimuove una substring dall'inizio e dalla fine della stinga
print(nome)
print(nome.strip("a"))
#visualizza tutte le informazioni
print(help(str))