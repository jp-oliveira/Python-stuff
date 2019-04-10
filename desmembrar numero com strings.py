x = int(input("diga um número inteiro menor que 1000: "))
y = x
c = 0
d = 0
u = 0
if x >= 1000:
   print("Valor inválido. Tente novamente.")
else:
      cent = x // 100
      if cent > 1 or cent ==0 :
         c = str('centenas')
      else:
         c = str('centena')  
      y -= cent*100
      dez = y // 10
      if dez > 1 or dez ==0 :
         d = str('dezenas')
      else:
         d = str('dezena')
      y -= dez*10
      if y > 1 or y==0 :
         u = str('unidades')
      else:
         u = str('unidade')
      print("O número tem:")
      print(cent,c)
      print(dez,d)
      print(y,u)
