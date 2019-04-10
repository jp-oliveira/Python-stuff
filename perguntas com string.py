print("Responda as perguntas para identificarmos a sua condição atual\
Responda S para sim e N para não.")
v = []
p1 = input("Telefonou para vítima?: ")
v.append(p1)

p2 = input("Esteve no local do crime?: ")
v.append(p2)

p3 = input("Mora perto da vítima?: ")
v.append(p3)

p4 = input("Devia para a vítima?: ")
v.append(p4)

p5 = input("Já trabalhou com a vítima?: ")
v.append(p5)

cont = 0
for i in range(5):
    if v[i] == 's':
        cont+=1

if cont == 5:
    print("ASSASSINO TU ÉS!")
elif cont == 3 or cont ==4:
    print("CÚMPLICE!")
elif cont ==2:
    print("suspeito apenas.")
else:
    print("Você não é suspeito.")
