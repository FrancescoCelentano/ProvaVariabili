# input -> quale operazione vuoi fare?

# input -> primo numero
# input -> secondo numero

# controllare il calcolo

#stampare

num1 = float(input("scrivi il primo numero "))
    #if num1.isalpha():
         #print("devi inserire un numero. \n\nRiproviamoci ")
         #continue
messaggio = input("che operazione vuoi fare? ").strip().lower()
if messaggio != "addizione" or "divisione":
        print("operazione non disponibile ")
num2 = float(input("scrivi il secondo numero "))
    #if num2.isalpha():
         #print("devi inserire un numero. \n\nRiproviamoci ")
         #continue

if messaggio == "addizione":
        ris = num1 + num2
elif messaggio == "sottrazione":
        ris = num1 - num2
elif messaggio ==  "divisione":
    if num2 == 0:
            ris = "sei un cretino!"
    else:
            ris = num1 / num2
elif messaggio == "moltiplicazione":
        ris = num1 / num2

print(f"Ecco il vostro risultato {ris}")
act = input("\n Desideri ricominciare? SI/NO ").upper().strip()
if act == "SI":
    print("Ripartiamo! ")

else:
    print("Addio. ")
