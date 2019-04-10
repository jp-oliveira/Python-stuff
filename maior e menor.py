n1 = int(input("digite o primeiro número: "))
n2 = int(input("digite o segundo número: "))
n3 = int(input("digite o terceiro número: "))
if n1 >= n2 >= n3:
    print(" o maior número é o", n1, " e o menor é o", n3)
elif n1 >= n3 >= n2:
    print(" o maior número é o" , n1, " e o menor é o", n2)
elif n2 >= n3 >= n1:
    print(" o maior número é o", n2, " e o menor é o", n1)
elif n2 >= n1 >= n3:
    print(" o maior número é o", n2, " e o menor é o", n3)
elif n3 >= n2 >= n1:
    print(" o maior número é o", n3, " e o menor é o", n1)
elif n3 >= n1 >= n2:
    print(" o maior número é o", n3, " e o menor é o", n2)          
          
