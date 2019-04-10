"""
Sabe-se que um número da forma n***3 é igual a soma de n ímpares consecutivos.
ex: 1**3 = 1 / 2**3= 3 + 5 / 3**3 = 7 + 9 + 11 / 4**3 = 13 + 15 + 17 + 19
Dado m, determine os ímpares consecutivos cuja soma é igual a n**3 para n
assumindo valores de 1 a m.
"""

m = int(input("Digite m: "))
soma = 0
n = 1
impares = 1
while n <= m:
    quer = n**3
    if soma != quer:
        impares += 2
        soma = soma + impares
        n+=1
    elif soma == quer:
        print(impares)
   


    
