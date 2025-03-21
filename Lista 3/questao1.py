votos = [0,0,0,0]

while True:
    print("Qual o melhor Sistema Operacional para uso em servidores?")
    print("As possíveis respostas são: \n 1 - Windows \n 2 - Linux \n 3 - Mac \n 4 - Outro")
    voto = int(input("digite seu voto (digitando 0 você encerra o sistema): "))

    if voto == 0:
        break
    elif 1 <= voto <= 4:
        votos[voto - 1] += 1
        #votos[voto - 1] = votos[voto -1] + 1
    else:
        print("digite seu voto corretamente")


print("Temos o seguinte resultado:")
print(f"Windows recebeu {votos[0]} votos")
print(f"Linux recebeu {votos[1]} votos")
print(f"Mac recebeu {votos[2]} votos")
print(f"Outros sistemas receberam {votos[0]} votos")