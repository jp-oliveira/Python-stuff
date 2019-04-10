"""
A telefonista digitará um numero(1-23). quando ela digitar zero, o programa foi encerrado.
se um numero errado for digitado, o programa deve ignora-lo, mostrando uma mensagem de aviso e pedir outro numero. ao final, devemos calcular:
1 - total de votos computados
2 - os numeros e respectivos votos de todos os jogadores que receberam voto
3 - o percentual de votos de cada um destes jogadores
4 - o numero do melhor jogador da partida
"""
total = []
cont = 0
voto = int(input("Essa é a enquete para saber quem foi o melhor jogador da partida!!\
digite um valor entre 1 e 23 ou 0 para sair. Começe agora: "))
total.append(voto)

while voto != 0:
    voto = int(input("Vamos continuar!Digite o número do melhor jogador(0 para parar): "))
    total.append(voto)
    cont += 1
    if voto > 23 or voto < 0:
        print("Voto inválido.Tente novamente!")

print("\nResultado da Votação: \n")

print("O número total de votos foi de", cont)
 
print("Jogador          Votos          %")
 
melhor = 1
maior_n_votos = 0
porcentagem = 0
for i in range(1, 24):
    total_de_votos_em_i = total.count(i)
    porcentagem_de_votos_em_i = 100*total_de_votos_em_i/cont
    if total_de_votos_em_i > 0:
        print("%4.i             %4.i          %.1f%%"%(i, total_de_votos_em_i, porcentagem_de_votos_em_i))
 
        if total_de_votos_em_i > maior_n_votos:
            maior_n_votos = total_de_votos_em_i
            melhor = i
            porcentagem = porcentagem_de_votos_em_i
 
print("O melhor jogador foi o número %i, com %i votos, correspondendo a %.1f%% do total de votos."%(melhor, maior_n_votos, porcentagem))
    
    
    
    


