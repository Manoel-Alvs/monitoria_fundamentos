repteis = []
mamiferos = []
aves = []
outros = []

for i in range (3):
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
    
print("os Répteis foram:", repteis, "e quantidade", len(repteis))

