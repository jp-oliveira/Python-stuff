area = int(input("digite o tamanho da área que irá ser pintada: "))
cob_tinta = area // 3
if area % 3 == 0:
    latas = cob_tinta // 18
    preço = latas * 80
    print("Você precisará de", latas, "latas")
    print("Você gastará", preço , "reais")
else:
    latas = ( cob_tinta // 18 ) + 1
    preço = latas * 80
    print("Você precisará de", latas , "latas")    
    print ("Você gastará R$", preço , "reais")


    
