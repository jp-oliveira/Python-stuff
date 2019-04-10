atletas = []
notas = []

for i in range(2):
    linha = []
    atleta = input("Diga o nome do %dº atleta: "%(i+1))
    atletas.append(atleta)
    for j in range(5):
        nota = float(input("Diga a %dª nota que esse atleta recebeu: " %(j+1)))
        linha.append(nota)
    notas.append(linha)

for i in range(2):
    for j in range(5):
        menor = notas[0][0]
        maior = notas[0][0]
        media = 0
        if notas[i][j] > maior:
            maior = notas[i][j]
        if notas[i][j] < menor:
            menor = notas[i][j]
    notas[i].sort()
    media = (notas[i][1] + notas[i][2] + notas[i][3])/3
    print("Resultado Final:")
    print("Atleta:",    atletas[i])
    print("Melhor Nota:",maior)
    print("Pior Nota: ",  menor)
    print("Média: ",     media)
