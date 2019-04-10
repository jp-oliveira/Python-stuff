"""
dados dois naturais m e n determinar, entre todos os pares de numeros naturais
(x,y) tais que x < m e y < n, um par para o qual o valor da expressão
x*y - x**2 + y seja máximo e calcular esse máximo.
"""
exp = x = y = 0
m = float(input("digite o valor de m: "))
n = float(input("Digite o valor de n: "))
for x in range (1,m):
    for y in range (1,n):
       if x*y - x**2 + y > exp:
           exp = x*y - x**2 + y
           x = x
           y = y
print ("O maior par é (%i,%i) e seu valor máximo é %i" %(x, y, exp)           
