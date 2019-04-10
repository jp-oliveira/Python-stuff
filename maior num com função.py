def maiornum():
    numeros= []
    x = int(input("diga quantos números existirão na sua sequência: "))
    for i in range (x):
        a = float(input("Diga o %iº número da sequência:"%(i+1)))
        numeros.append(a)
        numeros.sort()
    maior = numeros[x-1]
    print("O maior número da lista é o", maior)
        
maiornum()    



