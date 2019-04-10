"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
 
o   Fatorial de: 5
o   5! =  5 . 4 . 3 . 2 . 1 = 120
 
"""

x = int(input("Fatorial de: "))
print(x , end = ' ' )
print("! =  " + str(x) + str(". "), end = ' ')
fatorial = x
for i in range(x - 1,1,-1):
    fatorial *= i
    print(i, end = ' ')
    print(" . ", end = ' ')
print("1 = ", end = ' ')
print(fatorial)
