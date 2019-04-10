n=int(input("diga quantos funcionários existem:" ))
for i in range (1, n+1):
    sal = float(input(" esse é o funcionário número %i. Diga o seu salário: "%i))
    if sal <= 280:
        print("seu salário atual é:", sal)
        print("seu percentual de aumento será de 20%")
        print("seu aumento será de %.2f" %(sal*0.2))
        print(" seu novo salário será de %.2f" %(sal*1.2))
        print()
    elif sal > 280 and  sal <= 700:
        print("seu salário atual é:", sal)
        print("seu percentual de aumento será de 15%%")
        print("seu aumento será de %.2f" %(sal*0.15))
        print(" seu novo salário será de %.2f" %(sal*1.15))
        print()
    elif sal > 700 and sal <= 1500:
        print("seu salário atual é:", sal)
        print("seu percentual de aumento será de 10%")
        print("seu aumento será de %.2f" %(sal*0.1))
        print(" seu novo salário será de %.2f" %(sal*1.1))
        print()
    else:
        print("seu salário atual é:", sal)
        print("seu percentual de aumento será de 5%")
        print("seu aumento será de %.2f" %(sal*0.05))
        print(" seu novo salário será de %.2f" %(sal*1.05))
        print()
        
