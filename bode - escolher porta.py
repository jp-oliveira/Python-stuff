import random
chances = [1,2,3]
chances2 = [1,2,3]
right = random.randint(1,3)
chances.remove(right)
erro1 = chances[0]
choices2 = 0
    
choice = int(input("Olá, bem vindo ao programa. Vejamos se você irá ganhar um carro ou não!\
Escolha uma porta de 1 a 3: "))

chances2.remove(choice)

newchoice = int(input("Você escolheu a porta %i, mas eu lhe informo que  na porta \
%i há um bode. Deseja trocar de porta?(1 - sim/ 0 - não): "%(choice, erro1)))

if newchoice == 0:
    if choice == right:
        print("Parabéns. Você acertou!!")
    else:
        print("Você errou!")

elif newchoice == 1:
    choices2 = random.choice(chances2)
    if choices2 == right:
        print("Parabéns. Você acertou!!")
    else:
        print("Você errou!")
        

