numeros = []

while True:
    numero = int(input("Digite o número escolhido(-1 encerra o programa):\n"))
    
    if numero == -1:
        break

    numeros.append(numero)

#letra a)
#len(numeros)
print(f"foram digitados {len(numeros)} números")

#letra b)
numeros.sort(reverse = True)
print("A lista de valores de forma decrescente é:", numeros)

#letra c)

if 5 in numeros:
    print("O valor 5 está na lista")
else:
    print("O valor 5 não está na lista")
