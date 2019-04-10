""" 
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7
 
Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
 
Tente colocar a impressão do resultado em um único print
"""
import random

v = []
soma = 0
media = 0
name = input("Digite o nome do atleta: ")
n1 = random.uniform(7.0, 10)
n2 = random.uniform(7.0, 10)
n3 = random.uniform(7.0, 10)
n4 = random.uniform(7.0, 10)
n5 = random.uniform(7.0, 10)
n6 = random.uniform(7.0, 10)
n7 = random.uniform(7.0, 10)
v.append(n1)
v.append(n2)
v.append(n3)
v.append(n4)
v.append(n5)
v.append(n6)
v.append(n7)
v.sort()
v.remove(v[6])
v.remove(v[0])

for i in range(5):
    soma += v[i]
media = soma/5

print("Resultado final: \nAtleta: " + name + " \nMelhor nota:", v[4], "\nPior Nota:", v[0], "\nMédia:", media)
    
    


