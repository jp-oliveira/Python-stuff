import random
from tkinter import *
window = Tk()
window.title("GUESS-GAME")
window.geometry("500x400")
window.configure(background = "SeaGreen1")

def jogada(event = None):
  global v, repetido, guess
  guess = int(ent.get())
  if 100 < guess or guess < 1:
    msg["text"] = "Tente um número de 1 a 100."
  elif guess in v:
    repetido=True
    msg["text"] ="Você já usou este número antes, use um que ainda não foi usado."
  else:
    v.append(guess)
    ent.delete(0,2)
    ler()
    dica()

def dica():
  global guess, aleatorio, v, window2
  if guess == aleatorio:
    msg["text"] = ''
    msg2["text"]= "Parabéns! você conseguiu descobrir o número e ganhar o jogo!"    
    msg3["text"] = ''
    again()
    return
  if abs(aleatorio -guess)<= 2:
    msg["text"]= "Está fervendo!!!"
  elif 3 <= abs(aleatorio - guess) <= 5:
    msg["text"]="Está muito quente!"
  elif 6 <= abs(aleatorio - guess) <= 8:
    msg["text"]="Está quente."
  elif 9 <= abs(aleatorio - guess) <= 10:
    msg["text"]="Está morno."
  elif 11 <= abs(aleatorio - guess) <= 12:
    msg["text"]="Está frio!"
  elif 13 <= abs(aleatorio - guess) <= 14:
    msg["text"]="Está muito frio!"
  else:
    msg["text"]="Está congelando!!!"
  if len(v) < 9:
    msg3["text"]= "Você ainda tem", 10-len(v),"tentativas para acertar o número."
  else:
    msg3["text"]= "Você tem apenas mais", 10-len(v),"tentativa!!"
  if 2 <= len(v) < 10:
    escopo()
  if len(v)== 10:
    again()    

def ajuda():
  msg2["text"]= "Escolha um número de 1 a 100 para ver se é o mesmo que eu escolhi.\n Conforme seu chute for ficando pior ou melhor, irei dando dicas. são 10 tentativas."  

def again():
  global guess
  window.destroy()
  window2 = Tk()
  window2.title("Quit")
  window2.geometry("400x200")
  lbl3 = Label(window2, font = "Arial 20", bg ="white")
  if guess == aleatorio:
    lbl3["text"] = "Parabéns! Você venceu!"
  else:
    lbl3["text"] = "Lamentavelmente você perdeu kkkk! O número era:" + aleatorio
  lbl3.pack()

def escopo():
  global guess, v
  if abs(aleatorio - v[-2]) < abs(aleatorio- v[-1]):
    msg2["text"]= "Seu palpite está se afastando.."
  elif abs(aleatorio - v[-2]) == abs(aleatorio- v[-1]):
    msg2["text"]= "Continua tão próximo quanto estava no chute anterior."
  else:
    msg2["text"]= "Isso, agora está mais próximo!"

def ler():
  lbltentativas["text"] ="Você já chutou os números:"
  for i in range (len(v)):  
    lbltentativas["text"] += str(v[i]) + ',' 
aleatorio = random.randint(1,100)
repetido=False

window.bind("<Return>",jogada)
v= []
lblInst = Label(window, text = "Seja bem vindo ao Guess game.", fg = "black", font = "Arial 23", bg = "Yellow")

lbl = Label(window, text = "Diga o seu chute:")
lbl2 = Label(window, text = "Dica:")
msg = Label(window, text = '',bg ="SeaGreen1")
msg2 = Label(window, text = '',bg ="SeaGreen1")
msg3 = Label(window, text = '',bg ="SeaGreen1")

lblChute = Label(window, text ="Diga o seu chute:", font = "Arial 20", bg ="saddlebrown")
lblDica = Label(window, text ="Dica:", font = "Arial 20", bg ="saddlebrown")
lbltentativas = Label(window, text = str(v), font = "Arial 10", bg ="SeaGreen1")

ent = Entry(window)

btn = Button(window, text = "Confirme seu chute" , fg = "black", command = jogada, font = "Arial 20", bg = "darkgoldenrod")
btn2 = Button(window, text = "clique aqui para ler as regras do jogo" , fg = "black", command = ajuda, font = "Arial 20", bg = "darkgoldenrod")

lblInst.pack()
lblChute.pack()
ent.pack()
btn.pack()
btn2.pack()
lbltentativas.pack()
lblDica.pack()
msg.pack()
msg2.pack()
msg3.pack()

mainloop()
