#prova di acquisto e calcolo di spesa

Cosa = input("cosa vuoi comprare? ")
prezzo = input("quanto costa? ")
qnt = input("quante ne vuoi comprare? ")

tot = float(prezzo) + int(qnt)

print("hai appena speso " + str(tot) + "$")