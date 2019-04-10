for i in range (1, 11):
    n = int (input(" diga o número desse aluno: "))
    alt = float (input("diga sua altura: "))
    nma = nme = i
    menor = maior = alt
    if alt > maior:
        nma = i
        maior = alt
    elif alt < menor:
        nme = i
        menor = alt
print (" o aliuno mais baixo é o de número %1. \
sua altura é %.2f"%(nme, menor))
print (" o aliuno mais alto é o de número %1. \
sua altura é %.2f"%(nma, maior))
