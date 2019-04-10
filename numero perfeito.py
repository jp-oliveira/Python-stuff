"""
exemplo: 6 é perfeito, pois 1 + 2 + 3 = 6
28 = 14 + 7 + 4 + 2 + 1
dado um number inteiro positivo n, verificar se n é perfeito.
"""

n = int(input("digite o número a se verificar se é perfeito: "))
cont = 1
divisor = 0
while cont < n:
    if n%cont == 0:
        divisor = cont + divisor
    cont += 1
if divisor == n:
    print("Esse número é perfeito")
else:
    print("esse número não é perfeito")
        
        
