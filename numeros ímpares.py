n = int(input("Digite seu número: "))
if n >= 0:
    while n >= 1:
        print((n*2)-1)
        n = n - 1
else:
    print("esse número é inválido")
