sexo = int(input("Diga seu gênero (1 para m ou 2 para f): "))
alt = float(input("Diga sua altura em metros: "))
peso = float(input("Diga seu peso em Kg: "))
ph = pf = 0
if sexo == 1:
    ph = (72.7 * alt) - 58
    if peso > ph:
        print("Você está acima do peso pois o seu peso ideal é:", ph)
    elif peso == ph:
        print ("Você está no peso ideal!")
    else:
        print ("Você está abaixo do peso pois o seu peso ideal é:", ph)
elif sexo == 2:
    pf = (62.1 * alt) - 44.7
    if peso > pf:
        print("Você está acima do peso pois o seu peso ideal é:", pf)
    elif peso == pf:
        print ("Você está no peso ideal!")
    else:
        print ("Você está abaixo do peso pois o seu peso ideal é:", pf)
               
