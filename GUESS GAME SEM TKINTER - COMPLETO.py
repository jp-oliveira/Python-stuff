from random import randint

print ("O jogo consiste em adivinhar um número inteiro, entre 1 e 100, \
gerado aleatoriamente pelo computador. Após iniciar o jogo, você terá \
10 chances para acertar o número. O jogo terminará quando você esgotar \
suas chances ou quando o seu palpite igualar-se ao número gerado pelo computador.\n\
Dicas serão dadas conforme as tentativas forem sendo dadas. \n\
Boa sorte!\n")

aleatorio = randint(1,100)
repetido=False
cont=1
t1=0
t2=0
t3=0
t4=0
t5=0
t6=0
t7=0
t8=0
t9=0

while cont != 11:
    while True:
        try:
            print("Digite a sua tentativa de número", cont,".")
            numero = int(input("Tentativa: "))
            if 100 < numero or numero < 1:
                raise ValueError
            if numero == t1 or numero == t2 or numero == t3 or numero == t4 or numero == t5 or numero == t6 or numero == t7 or numero == t8 or numero == t9:
                repetido=True
                raise ValueError
            break
        except ValueError:
            if repetido == False:
                print("Seu número está fora dos padrões permitidos. Tente Novamente.\n\n\n\n")
            elif repetido == True:
                print ("Você já usou este número antes, aproveite melhor a sua chance com um número diferente.\n\n")
                repetido=False

    if numero == aleatorio:
        print("Parabéns! você conseguiu descobrir o número e ganhar o jogo!")
        cont=11
    else:
        if t1 == 0:
            t1=numero
        elif t2==0:
            t2=numero
            if abs(aleatorio - t1) < abs(aleatorio-t2):
                print("Seu palpite está se afastando..")
            elif abs(aleatorio - t1) == abs(aleatorio-t2):
                print("Continua tão próximo quanto estava no chute anterior.")
            else:
                print("Isso, agora está mais próximo!")
        elif t3==0:
            t3=numero
            if abs(aleatorio - t2) < abs(aleatorio-t3):
                print("Seu palpite está se afastando..")
            elif abs(aleatorio - t2) == abs(aleatorio-t3):
                print("Continua tão próximo quanto estava no chute anterior.")
            else:
                print("Isso, agora está mais próximo!")
        elif t4==0:
            t4=numero
            if abs(aleatorio - t3) < abs(aleatorio-t4):
                print("Seu palpite está se afastando..")
            elif abs(aleatorio - t3) == abs(aleatorio-t4):
                print("Continua tão próximo quanto estava no chute anterior.")
            else:
                print("Isso, agora está mais próximo!")
        elif t5==0:
            t5=numero
            if abs(aleatorio - t4) < abs(aleatorio-t5):
                print("Seu palpite está se afastando..")
            elif abs(aleatorio - t4) == abs(aleatorio-t5):
                print("Continua tão próximo quanto estava no chute anterior.")
            else:
                print("Isso, agora está mais próximo!")
        elif t6==0:
            t6=numero
            if abs(aleatorio - t5) < abs(aleatorio-t6):
                print("Seu palpite está se afastando..")
            elif abs(aleatorio - t5) == abs(aleatorio-t6):
                print("Continua tão próximo quanto estava no chute anterior.")
            else:
                print("Isso, agora está mais próximo!")
        elif t7==0:
            t7=numero
            if abs(aleatorio - t6) < abs(aleatorio-t7):
                print("Seu palpite está se afastando..")
            elif abs(aleatorio - t6) == abs(aleatorio-t7):
                print("Continua tão próximo quanto estava no chute anterior.")
            else:
                print("Isso, agora está mais próximo!")
        elif t8==0:
            t8=numero
            if abs(aleatorio - t7) < abs(aleatorio-t8):
                print("Seu palpite está se afastando..")
            elif abs(aleatorio - t7) == abs(aleatorio-t8):
                print("Continua tão próximo quanto estava no chute anterior.")
            else:
                print("Isso, agora está mais próximo!")
        elif t9==0:
            t9=numero
            if abs(aleatorio - t8) < abs(aleatorio-t9):
                print("Seu palpite está se afastando..")
            elif abs(aleatorio - t8) == abs(aleatorio-t9):
                print("Continua tão próximo quanto estava no chute anterior.")
            else:
                print("Isso, agora está mais próximo!")
            
        if aleatorio+2 >= numero >= aleatorio-2:
            print ("Está fervendo!!!")
        elif aleatorio+3 <= numero <= aleatorio+5 or aleatorio-5 <= numero <= aleatorio-3:
            print ("Está muito quente!")
        elif aleatorio+6 <= numero <= aleatorio+8 or aleatorio-8 <= numero <= aleatorio-6:
            print ("Está quente.")
        elif aleatorio+9 <= numero <= aleatorio+10 or aleatorio-10 <= numero <= aleatorio-9:
            print ("Está morno.")
        elif aleatorio+11 <= numero <= aleatorio+12 or aleatorio-12 <= numero <= aleatorio-11:
            print ("Está frio...")
        elif aleatorio+13 <= numero <= aleatorio+14 or aleatorio-14 <= numero <= aleatorio-13:
            print ("Está muito frio... =/")
        else:
            print ("Está congelando!!!")
        if cont < 9:
            print ("Você ainda tem", 10-cont,"tentativas para acertar o número.")
        else:
            print ("Você tem apenas mais", 10-cont,"tentativa!!")
        print (50*'-'+'\n')
        cont=cont+1
        
if cont == 11 and numero != aleatorio:    
    print("Que pena, não foi desta vez. \nO número correto era",aleatorio,".")
