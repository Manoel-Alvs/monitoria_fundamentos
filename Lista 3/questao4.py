numeros = []
quadrados = []

for i in range (10):
    numero = float(input("escolha o seu número: "))
    numeros.append(numero)

    quadrado = numero**2
    quadrados.append(quadrado)

print("Os números escolhidos são:", numeros)
print(f"Os quadrados dos números escolhidos são: {quadrados}")