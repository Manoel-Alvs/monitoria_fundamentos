repteis = []
mamiferos = []
aves = []
outros = []

for i in range (10):
    nome = input("escolha o animal: ")
    categoria = int(input("escolha o tipo:"))

    if categoria == 1:
        repteis.append(nome)
    elif categoria == 2:
        mamiferos.append(nome)
    elif categoria == 3:
        aves.append(nome)
    elif categoria == 4:
        outros.append(nome)
    
print(f"Os répteis escolhidos são: {repteis} e a quantidade foi: {len(repteis)}")
print(f"Os mamiferos escolhidos são: {mamiferos} e a quantidade foi: {len(mamiferos)}")
print(f"As aves escolhidas são: {aves} e a quantidade foi: {len(aves)}")
print(f"Os outros são: {outros} e a quantidade foi: {len(outros)}")

