numeros = []
quadrados = []

for i in range (10):
    numero = float(input("escolha o seu número: "))
    numeros.append(numero)

    quadrado = numero**2
    quadrados.append(quadrado)

print("os números escolhidos são:", numeros)
print(f"os quadrados dos números escolhidos são: {quadrados}")