#chiedi input all'utente
nome = input("inserisci un nome ")
posto = input("Una città che non hai mai visitato ")
aereo = input("Compagnia aerea più odiata ")
azione = input("inserisci un'azione (verbo all'infinito) ")
num = input("inserisci un numero da 10 a 80 ")
animale = input("inserisci un animale (plurale) ")
cifra = input("quanti $ vorresti ")






storia = f"""un giorno {nome} ebbe la brillante idea di acquistare un biglietto per {posto}.
ma la compagnia scelta era {aereo} e qualcosa di inaspettato era dietro l'angolo... il giorno della partenza, 
l'hostess iniziò a {azione} e guardando {nome} disse: 'mi dispiace ma oggi l'aereo non partirà,
perchè {num} {animale} hanno rapito il comandante e chiedono un riscatto di {cifra}$
"""

#stampa la storia completa
print("\nEcco la tua meravigliosa storia")
print(storia)
input("Adesso ti va di leggerla in spagnolo? ")
print(storia.replace(" ", "s "))


#quiz sulla storia
domanda = input("questa lezione di spagnolo ti è servita? ")

testo = f"Data la tua risposta {domanda}, ecco a te un bel certificato."
print(testo)