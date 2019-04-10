n = int (input("diga quantas temperaturas serão registradas: "))
soma = maior = menor = float(input(" digite a temperatura 1: "))
for i in range (2, n+1):
    t = float(input("diga a temperatura %i: " %i)) 
    if t > maior:
        maior = t
    elif t < menor:
        menor = t
    soma += t
media = soma / n
print(" a maior temperatura foi:", maior)
print(" a menor temperatura foi:", menor)
print(" a média entre as temperaturas foi de %.2f"%(media))
