n1 = int(input("Diga um número positivo diferente de zero: "))
n2 = int(input("Diga um número positivo diferente de zero: "))
n = int(input("Diga quantos naturais você quer: "))
mult = cont = 0
while cont <n:
    if mult %n1 == 0 or mult%n2 == 0:
        print (mult)
        cont = cont + 1
    mult = mult +1
               
