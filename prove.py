'''
temp = input("inserisci un nome di persona: ")
print(f"temp ora vale {temp}")
temp = temp.strip()
print(f"temp ora vale {temp}")
nome = temp.capitalize()
print(f"temp ora vale {nome}")

temp = input("inserisci il nome di una città")
print(f"temp ora vale {temp}")
temp = temp.strip()
print(f"temp ora vale {temp}")
luogo = temp.capitalize()
print(f"temp ora vale {luogo}")

#chainmetod
verbo = input("inserisci un verbo all'infinito: ").strip().lower().replace("a", "i")


print(f"temp ora vale {temp}")'''

temp = input("inserisci un nome: ").strip() or "ciao"
print(temp)