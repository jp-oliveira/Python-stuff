while True:
    try:
        c = float(input('Diga qual o tamanho do terreno: '))
        if c%6 == 0:
            cobertura = c/6
        else:
            cobertura = c // 6 + 1
        def opcao1(x):
            global litros
            if x%18 == 0:
                litros = x/18
            else:
                litros = x // 18 + 1
            preco = 80 * litros
            return preco
        def opcao2(y):
            global litragem
            if y%18 ==0:
                litragem = y/4
            else:
                litragem = y // 4 + 1
            valor = 25 * litragem
            return valor
        print('A Opção 1 gerará um valor de R$',opcao1(cobertura),'e usará',litros,'garrafas')
        print('A Opção 2 gerará um valor de R$',opcao2(cobertura),'e usará',litragem,'latas')
    except:
        print('Valor inválido.')
