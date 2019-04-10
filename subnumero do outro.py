
p = int(input("Digite um número inteiro: "))
q = int(input("Digite um numero inteiro com + dígitos que o anterior: "))
p2 = p
v = []
v2 = []
r = str(p)
s = str(q)

if r in s:
    print("%i é um subnumero de %i." %(p,q))
else:
    print("%i não é um subnumero de %i." %(p,q))



def calculadigitop(v):
    var = len(r)
    for i in range(var-1, -1, -1):
        v.append(ord(r[i]))
          
def calculadigitoq(v2):
    var2 = len(s)
    for i in range(var2 -1, -1, -1):
        v2.append(ord(s[i]))

calculadigitop(v)
calculadigitoq(v2)
v.sort()
v2.sort()
print(v, v2)
for j in range (len(v) - 1):
    if v[j] == v2[j]:
        print ("voila")
    else:
        print("not right")
    
