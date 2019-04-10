"""
Faça um prog que leia 20 inteiros e os guarde num vetor. Armazene os números
pares no vetor par e os ímpares no vetor ímpar. Imprima ambos os vetores.
"""

vetor = []
par = []
impar = []
for i in range (1, 21):
    n = int(input(" diga o número %i: "%i))
    vetor.append(n)
    if n%2 == 0:
        par.append(n)
    else:
        impar.append(n)
print("Os números pares foram os seguintes: ", par)
print()
print("Os números ímpares foram os seguintes: ", impar)
