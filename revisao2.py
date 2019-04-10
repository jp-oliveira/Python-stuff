while True:
    try:
        a = float(input('Diga um número(para acabar, escreva fim): '))
        if a > 0:
            print('Esse número é positivo.')
        else:
            print('Esse número é negativo.')
    except:
        if a == 'fim':
            break
        print('caracter inválido. Tente outro.')
