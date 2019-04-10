def resposta():
    global resp
    while True:
        resp = input("Você deseja criptografar ou descriptografar?(c ou d): ").lower()
        if resp in 'c d'.split():
            return resp
        else:
            print("digite c ou d apenas.")
 
def chave():
    global key
    while True:        
        key = int(input("Diga qual a chave desejada de 1 a 26: "))
        if 1 <= key <= 26:
            return key
        else:
            print("digite apenas um numero de 1 a 26.")

resposta()
frase = input("Diga qual frase você quer modificar: \n") 
chave()        
new = ''
v2 = frase.split(' ')
mais = []
cript = []

#For para saber os caracteres maiúsculos
for i in(frase):
    if i.isupper():
        mais.append(i)
        
if resp == 'c':
    for caracter in frase:
        if caracter.isalpha():
            num = ord(caracter)
            num += key
            if caracter.isupper():
                if num > ord('Z'):
                    num = (num- ord('Z')) + (ord('A') - 1)
                elif num < ord('A'):
                    num = (ord('Z') + 1)- (ord('A') - num)
            elif caracter.islower():
                if num > ord('z'):
                    num = (num - ord('z')) + (ord('a') - 1)
                elif num < ord('a'):
                    num = (ord('z') + 1) - (ord('a') - num)
            new += chr(num)
        else:
            new+= caracter

elif resp == 'd':
    for caracter in frase:
        if caracter.isalpha():
            num = ord(caracter)
            num -= key
            if caracter.isupper():
                if num > ord('Z'):
                    num = (num- ord('Z')) + (ord('A') - 1)
                elif num < ord('A'):
                    num = (ord('Z') + 1)- (ord('A') - num)
            elif caracter.islower():
                if num > ord('z'):
                    num = (num - ord('z')) + (ord('a') - 1)
                elif num < ord('a'):
                    num = (ord('z') + 1) - (ord('a') - num)
            new += chr(num)
        else:
            new+= caracter          

print("Agora essa é a frase: \n", new)
    

