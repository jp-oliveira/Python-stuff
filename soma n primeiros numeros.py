base = int(input("digite a base: "))
expo = int(input("digite o expoente: "))
produto = 1
cont = 0
while cont < expo:
    produto = produto * base
    cont = cont + 1
print(base, "elevado à",expo,"=", produto)

