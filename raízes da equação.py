print("Dê os coeficientes da equação de 2º grau")
a = float(input("diga o valor de A: "))
b = float(input("diga o valor de B: "))
c = float(input("diga o valor de C: "))
if a == 0:
    print("Valor inválido. A equação não é de 2º Grau")
else:
    delta = b*b - (4*a*c)
    raiz = raiz1 = raiz2 = 0.0
    if delta < 0:
        print("a equação não possui raizes reais")
    elif delta == 0:
        raiz = -b/(2*a)
        print("A equação só possui uma raiz real - o número", raiz)
    else:
        raiz1 = (-b + (delta)**(0.5))/(2*a)
        raiz2 = (-b - (delta)**(0.5))/(2*a)
        print("As raizes da equação são: ",raiz1, "e", raiz2)
        
