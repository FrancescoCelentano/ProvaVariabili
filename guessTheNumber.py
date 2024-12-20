import random
numero_segreto = random.randint(1,100)
#DEBUG
print(numero_segreto)
print("\nBenvenuto alla ruota della fortuna")

tentativi = 5

while tentativi > 0:
    print(f"Hai {tentativi} tentativi ")
    num = ""
    while not num.isdigit():
        num = input("Prova ad indovinare il numero (solo numeri consentiti) ").strip()
    else:
        num = int(num)

    tentativi -= 1
    if num == numero_segreto:
        print("Hai indovinato il numero!!! ")
        break
    else:
        print("Hai sbagliato! ")
        if tentativi == 0:
            print(f"Il numero era {numero_segreto}, ritenta. ")
            continue
        elif num < numero_segreto and tentativi != 0:
            print("Il numero che cerchi è maggiore ")
        elif num > numero_segreto and tentativi != 0:
            print("Il numero che cerchi è minore ")
        #elif tentativi <= 5:
            #print(f"ti rimangono {tentativi} tentativi")

#else:
   # print(f"Non hai piu tentativi \nIl numero era {numero_segreto}, ritenta. ")







