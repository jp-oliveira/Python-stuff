"""
Faça um programa que leia 4 notas, mostre as notas e a média na tela.
"""

lista = []
media = 0
for i in range (1,5):
    n = float(input(" diga a %i ª nota: "%i))
    lista.append(n)
    media += n
print("as notas foram: ", lista)
print (" a média das notas foi: %.2f"%(media/4))
    
    
