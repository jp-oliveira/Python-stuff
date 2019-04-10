n1 = int(input("Diga um numero diferente de zero: "))
n2 = int(input("Diga outro numero diferente de zero: "))
div = 0
if n1 > n2:
    for i in range (1, n2 +1):
        if n1%i == 0 and n2%i == 0:
            div = i
            print(div)
elif n2 > n1:
    for i in range(1, n2 +1):
        if n1%i ==0 and n2%i == 0:
            div = i
            print(div)
    
    
