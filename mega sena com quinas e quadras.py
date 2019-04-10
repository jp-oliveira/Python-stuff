import random
premio = []
jogada = []
parcial = []

sorteio2= list(range(1,61))
cont = 1
lucro = 0
luc = 0
quantia = random.uniform(1500000, 70000000)

print("Bem vindo ao jogo da mega sena. Escolha 6 números dentre 60 sem repetir nenhum para ver se ganhará algum prêmio.")

while len(jogada) != 6:
    x = int(input("Escolha o %iº número: "%(len(jogada)+1)))
    jogada.append(x)
    sorteio2.remove(x)
jogada.sort()

while cont <= 50063860:
    sorteio = list(range(1,61))
    while len(premio) != 6:
        y = random.choice(sorteio)
        premio.append(y)
        sorteio.remove(y)
  
    premio.sort()

    for i in range(6):
        if jogada[i] == premio[i]:
            parcial.append(jogada[i])

    if len(parcial) == 4:
        luc = random.uniform(1/5000, 1/30000)
        lucro = luc * quantia
        print("Parabéns. Você ganhou a quadra, que corresponde a 4 números corretos.")

    elif len(parcial)== 5:
        luc = random.uniform(0.1 , 0.4)
        lucro = luc* quantia
        print("Parabéns. Você ganhou a quina, que corresponde a 5 números corretos.")

    elif len(parcial) == 6:
        lucro = 0.94 * quantia
        print("Parabéns. Você ganhou a megasena!")

    quantia+= random.uniform(1500000, 70000000)
    cont +=1
    lucro = lucro - 2.5
    parcial = []
    premio = []

print("Em 50063860 tentativas, o lucro foi de %i reais" %(lucro))
                            


