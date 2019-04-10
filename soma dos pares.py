n = int(input("digite o número: "))
cont = 0
soma = 0
while cont < n:
    n2=int(input("digite o número: "))
    if n%2 == 0:
        soma += n2
    cont = cont + 1
print(soma)    
