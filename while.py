from operator import is_not
from time import process_time

contatore = 1
#esempio break
while contatore <= 5:
    print("contatore vale", contatore)
    contatore = contatore +1
    #contatore += 1
    if contatore == 4:
        print("trovato! ", contatore)
        break

print("istruzioni dopo il break")
#esempio continue
contatore = 0

while contatore <= 9: #contatore già definito prima, inserito solo per scopo visivo
    contatore += 1
    if contatore == 4:
        print("questa volta passo... ")
        continue
    print("contatore vale ", contatore)

print("istruzioni dopo il continue")
#esempio else
contatore = 1 #contatore già definito prima, inserito solo per scopo visivo
x = 7
while contatore <= 10:
    if contatore == x:
        print("trovato! ", contatore)
        break
    contatore += 1
else:
    print("non ho trovato", x)

print("istruzioni dopo l'else ")

#esempio validazione input all'infinito
password = ""

while password != "pa123":
    password = input("inserisci password: ").strip()
print("Accesso consentito")

#esempio validazione input con tentativi limitati
password = ""
tentativi = 0
risultato = ""

while password != "pa1234" and tentativi < 3:
    tentativi += 1
    mexTry = f"Ti sono rimasti {4 - tentativi} tentativi "
    mexLast = "Ultimo tentativo rimasto! "

    mex = mexTry if tentativi < 3 else mexLast
    print(mex)
    password = input("inserisci password: ")
    risultato = "accesso consentito" if password == "pa1234" else "accesso negato"
else:
    print(risultato)

