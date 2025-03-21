numeros = []
negativos = 0
soma = 0

for i in range(10):
    numero = float(input("Escolha o número: "))
    numeros.append(numero)

    if numero < 0:
        negativos += 1
    else:
        soma += numero
    
print(f"A quantidade de números negativos foi {negativos}")
print(f"A soma dos números positivos foi: {soma}")

