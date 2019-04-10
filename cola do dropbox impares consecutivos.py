m = int(input("Digite m: "))
 
aux = 1
 
for n in range(1, m+1):
    print("O número", n, "elevado ao cubo tem como soma: ")
    if n == 1:
        print(aux)
    else:
        for aux in range(aux+2, aux+2*(n+1), 2):
            print(aux)
