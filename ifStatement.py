# Esercizio costrutto if (mutualmente esclusivi)

pippo = 8

if pippo >= 7:
    print("pippo vale almeno 7")
elif pippo == 8:
    print("pippo vale 8")
else:
    print("pippo non vale 6")

numero = int(input("inserisci un numero"))
# verificare se il numero è un multiplo di 2 oppure di 3
# metodo 1
if numero % 2 == 0:
    print(f"{numero} è un multiplo di 2")
if numero % 3 == 0:
    print(f"{numero} è un multiplo di 3")
if numero % 5 == 0:
    print(f"{numero} è un multiplo di 5")
if numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0:
    print(f"{numero} non è multiplo di 2, 3 e 5")

# DRY --> Don't Repeat Yourself
# metodo 2: utilizzo dei booleani
print("metodo2 con booleani")
flag = False

if numero % 2 == 0:
    print(f"{numero} è un multiplo di 2")
    flag = True
if numero % 3 == 0:
    print(f"{numero} è un multiplo di 3")
    flag = True
if numero % 5 == 0:
    flag = True
    print(f"{numero} è un multiplo di 5")
if not flag:
    print(f"{numero} non è un multiplo di 2,3 e 5")

# operatore ternario
print("operatore ternario")

messaggio = f"{numero} è pari" if numero % 2 == 0 else "numero è dispari"
print(messaggio)

