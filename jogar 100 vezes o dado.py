"""
faça um programa que simule um lançamento de dados. lançe o dado 100 vezes e
guarde os resultados num vetor. Depois mostre quantas vezes cada valor foi
conseguido.
"""

import random
vetor = []
for i in range (1, 101):
    jogada = random.randint(1,6)
    vetor.append(jogada)
for i in range (1,7):
    print(" Em 100 jogadas o número %i saiu %i veze(s)."%(i, vetor.count(i)))
