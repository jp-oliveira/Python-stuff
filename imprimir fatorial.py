n = int(input("digite seu número: "))
if n >= 0:
    fatorial = n
    cont = n - 1
    while cont > 1:
        fatorial = fatorial * cont
        cont = cont - 1
    print(" o fatorial do seu número é:", fatorial)
    
else:
    print(" esse número é inválido")
