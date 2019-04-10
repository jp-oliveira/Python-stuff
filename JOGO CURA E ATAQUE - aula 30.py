import random
vida_jog = 500
magia_jog = 100
vida_enemy = 37

# criando um vetor para armazenar a quantidade de inimigos
n = int(input("Diga quantos inimigos você quer: "))
inimigos = []
cont = 1
while cont <= n:
    inimigos.append([cont, vida_enemy])
    cont +=1
    
# vez do usuário de jogar
while vida_jog > 0:
    print ("Vida:",vida_jog)
    print ("SP:",magia_jog)
    desejo = int(input(" Deseja atacar (1) ou curar (2)? "))
    if desejo == 1:
        alvo = random.choice(inimigos)
        ataque = random.randint(10, 15)
        print ("Causou %i de dano ao inimigo %i"%(ataque, alvo[0]))
        alvo[1] -= ataque
        if alvo[1] <= 0:
            print ("O inimigo %i morreu!" %(alvo[0]))
            inimigos.remove(alvo)
    elif desejo ==2:
        if magia_jog < 10:
            print (" Você não tem mais SP suficientes para isso!")
        else:
            cura = random.randint(10,15)
            print (" Você recebeu mais %i de vida."%cura)
            vida_jog += cura
            magia_jog -= 10             

    # vez do programa de jogar
    for i in inimigos:
        dado = random.randint(1,4)
        if dado != 4:
            dano_inimigo = random.randint(1, 4)
            print ("inimigo %i causou %i de dano!" %(i[0], dano_inimigo))
            vida_jog -= dano_inimigo
        else:
            print("O inimigo %d errou o ataque!" %i[0])
    print("adversários e suas respectivas vidas:" inimigos)
    # a cada rodada se ganha mais 3 pontos de magia
    if magia_jog < 100:
        magia_jog +=3
    if magia_jog > 100:
        magia_jog = 100
    if len(inimigos) == 0:
        print ("Parabéns. Você ganhou o jogo!")
        break
if vida_jog <= 0:
    print (" Você perdeu o jogo!")
        
    

