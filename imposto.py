def somaimposto(taxaimposto, custo):
    return custo + taxaimposto*custo/100
taxaimposto =  float(input("digite o imposto em porcentagem: "))
custo =  float(input("Digite o valor do produto: "))

print("O custo recalculado com o imposto é de R$%.2f"%somaimposto(taxaimposto, custo))
