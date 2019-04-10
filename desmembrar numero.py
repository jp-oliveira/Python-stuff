"""
Faça um Programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.
    Observando os termos no plural a colocação do "e", da vírgula
    entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301,
    101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
    """

n = int(input("digite o seu número: "))
c = 0
d = 0
u = 0
msgc = 0
msgd = 0
msgu = 0
if n < 1000:
    c = n//100
    resto = n - (c*100)
    if c == 1:
        msgc = str("centena")
    else:
        msgc = str("centenas")
    if resto !=0:
        d = resto // 10
        resto2 = resto - (d*10)
        if d == 1:
            msgd = str("dezena")
        else:
            msgd= str("dezenas")
        if resto2 != 0:
            u = resto2
                
        if u == 1:
            msgu = str("unidade")
        else:
            msgu = str("unidades")
        print ("esse número tem: ",c,msgc," e ", d,msgd, "e", u, msgu)
else:
    print("esse número é inválido para esse programa")
