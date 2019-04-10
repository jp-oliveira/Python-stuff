def mult():
    a = float(input("Vá inserindo números para serem multiplicados\
(o número um interromperá o processo): "))
    mul = 1*a
    while a!=1:
        a = float(input("Continue a multiplicação!(1 interrompe o processo): "))
        mul*=a
    print (mul)


mult()
        
