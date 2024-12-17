#prove di funzioni
#prova di acquisto e calcolo di spesa
#metodo 1
item = input("cosa vuoi comprare? ")
price = input("quanto costa? ")
qnt = input("quante ne vuoi comprare? ")

tot = round(float(price) * int(qnt), 2)

print("hai appena speso " + str(tot) )

#metodo 2
print(f"Per comprare {qnt} di {item} devi pagare {round(int(qnt) * float(price), 2)}")

#metodo 3
item1 = input("cosa vuoi comprare? ")
price1 = float(input("quanto costa in $? "))
qnt1 = int(input("quante ne vuoi comprare? "))


print(f"per comprare {qnt1} di {item1} devi pagare {round(qnt1 * price1, 2)}$")