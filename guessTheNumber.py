import random
numero_segreto = random.randint(1,100)
#DEBUG
print(numero_segreto)
print("\nBenvenuto alla ruota della fortuna")

tentativi = 7

while tentativi > 0:
    num = int(input("Prova ad indovinare il numero").strip())
    tentativi -= 1
    if num == numero_segreto:
        print("Hai indovinato il numero!!! ")
        break
    elif num < numero_segreto:
        print("Il numero che cerchi è maggiore")
    elif num > numero_segreto:
        print("Il numero che cerchi è minore")
else:
    print(f"Tentativi finiti " f"il numero era {numero_segreto}, ritenta. ")







