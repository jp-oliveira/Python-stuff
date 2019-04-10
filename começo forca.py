import random 
imagens= ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
 
palavras = 'babuino ignobil verossimil torque crocodilo suriname meteoro meandros selvageria juscelino coloquio colombiano'.split()

def main():
    global erros, tentativa, palavra
    jogando = True
    palavra = random.choice(palavras).upper()
    print("Bem vindo ao jogo da forca.")
    erros = []
    while len(imagens) >= 1:
        tamanho = '_ ' * len(palavra)
        print(imagens[0], "\n")
        print(tamanho, "\n")
        print("letras erradas:", erros)
        check()
        if tentativa in palavra:
            acertos()
        else:
            mistakes()
           
#para checar se a tentativa está correta
def check():
    while True:
        global tentativa
        tentativa = input("Diga qual letra você quer: ").upper()
        if len(tentativa) != 1:
            print("Coloque uma única letra.")
        elif tentativa in erros:
            print("Você já chutou esta letra. Escolha novamente.")
        elif not 'A' <= tentativa <= 'Z':
            print("Por favor escolha apenas letras.")
        else:
            return tentativa

def acertos():
    global tentativa, palavra
    print("Parabéns. A letra", tentativa,"está na palavra secreta!")
    for i in palavra:
        if palavra[i] == tentativa:
            print("oi")
              
def mistakes():
    global erros, tentativa
    erros.append(tentativa)
    imagens.remove(imagens[0])
    print("letra errada!")
    return erros

main()
