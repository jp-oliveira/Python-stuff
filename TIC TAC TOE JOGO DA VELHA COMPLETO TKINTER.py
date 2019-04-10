from tkinter import *
import tkinter.messagebox
import random

jogada = 0
modo = 0
tent = 0
        
def main():
    global window
    window = Tk()
    window.title("Dificuldades")
    window.geometry("500x250")

    selecione = Label(window, text='Selecione a dificuldade:', font=('Arial 20 bold'))
    selecione.grid(row=1, column=0, columnspan=3)

    facil = Button(window, text='EASY', font=('Arial 10 bold'),height=2,width=10, command=lambda:modfacil(), background='#fff')
    facil.grid(row=2, column=0, pady=20)

    medio = Button(window, text='MEDIUM', font=('Arial 10 bold'),height=2,width=10, command=lambda:modmedio(), background='#fff')
    medio.grid(row=2, column=1)

    dificil = Button(window, text='HARD', font=('Arial 10 bold'),height=2,width=10, command=lambda:moddificil(), background='#fff')
    dificil.grid(row=2, column=2)

def modfacil():
    global modo
    window.destroy()    
    modo = 'facil'
    tabuleiro()

def modmedio():
    global modo
    window.destroy()  
    modo = 'medio'
    tabuleiro()

def moddificil():
    global modo
    window.destroy()   
    modo = 'dificil'
    tabuleiro()

def tabuleiro():
    global celulas, c1, c2, c3, c4, c5, c6, c7, c8, c9, root
    root = Tk()
    root.title("Jogo da Velha")
    c1 = Button(root,text=' ',font=('Arial 30 bold'),height=3,width=7,command=lambda:velha(c1))
    c1.grid(row=3, column=0, stick=(N+S+E+W))

    c2 = Button(root,text=' ',font=('Arial 30 bold'),height=3,width=7,command=lambda:velha(c2))
    c2.grid(row=3, column=1, stick=(N+S+E+W))

    c3 = Button(root,text=' ',font=('Arial 30 bold'),height=3,width=7,command=lambda:velha(c3))
    c3.grid(row=3, column=2, stick=(N+S+E+W))

    c4 = Button(root,text=' ',font=('Arial 30 bold'),height=3,width=7,command=lambda:velha(c4))
    c4.grid(row=4, column=0, stick=(N+S+E+W))

    c5 = Button(root,text=' ',font=('Arial 30 bold'),height=3,width=7,command=lambda:velha(c5))
    c5.grid(row=4, column=1, stick=(N+S+E+W))

    c6 = Button(root,text=' ',font=('Arial 30 bold'),height=3,width=7,command=lambda:velha(c6))
    c6.grid(row=4, column=2, stick=(N+S+E+W))

    c7 = Button(root,text=' ',font=('Arial 30 bold'),height=3,width=7,command=lambda:velha(c7))
    c7.grid(row=5, column=0, stick=(N+S+E+W))

    c8 = Button(root,text=' ',font=('Arial 30 bold'),height=3,width=7,command=lambda:velha(c8))
    c8.grid(row=5, column=1, stick=(N+S+E+W))

    c9 = Button(root,text=' ',font=('Arial 30 bold'),height=3,width=7,command=lambda:velha(c9))
    c9.grid(row=5, column=2, stick=(N+S+E+W))

    celulas = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
    root.mainloop()    

def velha(celula):
    global jogada, modo
    celula['text'] = 'X'
    celula.config(state = DISABLED)
    celulas.remove(celula)    
    jogada += 1
    verificaRes()
    if modo == 'facil':
        easy()
    elif modo == 'medio':
        medium()
    elif modo == 'dificil':
        hard()
        
def easy():
    global jogada
    verificaRes()
    pc = random.choice(celulas)
    pc['text'] = 'O'
    pc.config(state=DISABLED)
    celulas.remove(pc)    
    jogada += 1
    verificaRes()

def medium():
                    # ---------- Para vencer ------------      
    if c2['text'] == 'O' and c3['text'] == 'O' and c1['text'] == ' ' or \
         c4['text'] == 'O' and c7['text'] == 'O' and c1['text'] == ' ' or \
         c5['text'] == 'O' and c9['text'] == 'O' and c1['text'] == ' ':
        c1['text'] = 'O'
        
    elif c1['text'] == 'O' and c3['text'] == 'O' and c2['text'] == ' ' or \
       c5['text'] == 'O' and c8['text'] == 'O' and c2['text'] == ' ':
        c2['text'] = 'O'
        
    elif c1['text'] == 'O' and c2['text'] == 'O' and c3['text'] == ' ' or \
         c6['text'] == 'O' and c9['text'] == 'O' and c3['text'] == ' ' or \
         c5['text'] == 'O' and c7['text'] == 'O' and c3['text'] == ' ':
        c3['text'] = 'O'
    
    elif c5['text'] == 'O' and c6['text'] == 'O' and c4['text'] == ' ' or \
         c1['text'] == 'O' and c7['text'] == 'O' and c4['text'] == ' ':
        c4['text'] = 'O'
        
    elif c4['text'] == 'O' and c6['text'] == 'O' and c5['text'] == ' ' or \
         c2['text'] == 'O' and c8['text'] == 'O' and c5['text'] == ' ' or \
         c1['text'] == 'O' and c9['text'] == 'O' and c5['text'] == ' ' or \
         c3['text'] == 'O' and c7['text'] == 'O' and c5['text'] == ' ':
        c5['text'] = 'O'

    elif c4['text'] == 'O' and c5['text'] == 'O' and c6['text'] == ' ' or \
         c3['text'] == 'O' and c9['text'] == 'O' and c6['text'] == ' ':
        c6['text'] = 'O'

    elif c8['text'] == 'O' and c9['text'] == 'O' and c7['text'] == ' ' or \
         c1['text'] == 'O' and c4['text'] == 'O' and c7['text'] == ' ' or \
         c3['text'] == 'O' and c5['text'] == 'O' and c7['text'] == ' ':
        c7['text'] = 'O'
        
    elif c7['text'] == 'O' and c9['text'] == 'O' and c8['text'] == ' ' or \
         c2['text'] == 'O' and c5['text'] == 'O' and c8['text'] == ' ':
        c8['text'] = 'O'

    elif c7['text'] == 'O' and c8['text'] == 'O' and c9['text'] == ' ' or \
         c3['text'] == 'O' and c6['text'] == 'O' and c9['text'] == ' ' or \
         c1['text'] == 'O' and c5['text'] == 'O' and c9['text'] == ' ':
        c9['text'] = 'O'  

                            # --------Evitar Jogadas ------------
    elif c2['text'] == 'X' and c3['text'] == 'X' and c1['text'] == ' ' or \
         c4['text'] == 'X' and c7['text'] == 'X' and c1['text'] == ' ' or \
         c5['text'] == 'X' and c9['text'] == 'X' and c1['text'] == ' ':
        c1['text'] = 'O'
        
    elif c1['text'] == 'X' and c3['text'] == 'X' and c2['text'] == ' ' or \
       c5['text'] == 'X' and c8['text'] == 'X' and c2['text'] == ' ':
        c2['text'] = 'O'
        
    elif c1['text'] == 'X' and c2['text'] == 'X' and c3['text'] == ' ' or \
         c6['text'] == 'X' and c9['text'] == 'X' and c3['text'] == ' ' or \
         c5['text'] == 'X' and c7['text'] == 'X' and c3['text'] == ' ':
        c3['text'] = 'O'
    
    elif c5['text'] == 'X' and c6['text'] == 'X' and c4['text'] == ' ' or \
         c1['text'] == 'X' and c7['text'] == 'X' and c4['text'] == ' ':
        c4['text'] = 'O'
        
    elif c4['text'] == 'X' and c6['text'] == 'X' and c5['text'] == ' ' or \
         c2['text'] == 'X' and c8['text'] == 'X' and c5['text'] == ' ' or \
         c1['text'] == 'X' and c9['text'] == 'X' and c5['text'] == ' ' or \
         c3['text'] == 'X' and c7['text'] == 'X' and c5['text'] == ' ':
        c5['text'] = 'O'

    elif c4['text'] == 'X' and c5['text'] == 'X' and c6['text'] == ' ' or \
         c3['text'] == 'X' and c9['text'] == 'X' and c6['text'] == ' ':
        c6['text'] = 'O'

    elif c8['text'] == 'X' and c9['text'] == 'X' and c7['text'] == ' ' or \
         c1['text'] == 'X' and c4['text'] == 'X' and c7['text'] == ' ' or \
         c3['text'] == 'X' and c5['text'] == 'X' and c7['text'] == ' ':
        c7['text'] = 'O'
        
    elif c7['text'] == 'X' and c9['text'] == 'X' and c8['text'] == ' ' or \
         c2['text'] == 'X' and c5['text'] == 'X' and c8['text'] == ' ':
        c8['text'] = 'O'

    elif c7['text'] == 'X' and c8['text'] == 'X' and c9['text'] == ' ' or \
         c3['text'] == 'X' and c6['text'] == 'X' and c9['text'] == ' ' or \
         c1['text'] == 'X' and c5['text'] == 'X' and c9['text'] == ' ':
        c9['text'] = 'O'

    elif jogada != 0:
        easy()
    verificaRes()

def hard():
    global tent    

    if jogada ==1:
        if c1['text'] == 'X':
            sec2 = random.choice([c3,c7,c9])
            sec2["text"] = 'O'

        elif c2['text'] == 'X':
            sec2 = random.choice([c1,c3])
            sec2["text"] = 'O'

        elif c3['text'] == 'X':
            sec2 = random.choice([c1,c2,c5,c6,c7,c9])
            sec2["text"] = 'O'

        elif c4['text'] == 'X':
            sec2 = random.choice([c1,c5,c6,c7])
            sec2["text"] = 'O'

        elif c5['text'] == 'X':
            sec2 = random.choice([c1,c3,c7,c9])
            sec2['text'] = 'O'

        elif c6['text'] == 'X':
            sec2 = random.choice([c3,c4,c5,c9])
            sec2["text"] = 'O'

        elif c7['text'] == 'X':
            sec2 = random.choice([c1,c3,c4,c5,c8,c9])
            sec2["text"] = 'O'

        elif c8['text'] == 'X':
            sec2 = random.choice([c2,c5,c7,c9])
            sec2["text"] = 'O'

        elif c9['text'] == 'X':
            sec2 = random.choice([c1,c3,c5,c6,c7,c8])
            sec2["text"] = 'O'       
    elif jogada >= 2:
        medium()            
    verificaRes()

def verificaRes():
    if (c1['text'] == 'X' and c2['text'] == 'X' and c3['text'] == 'X' or \
        c1['text'] == 'X' and c5['text'] == 'X' and c9['text'] == 'X' or \
        c1['text'] == 'X' and c4['text'] == 'X' and c7['text'] == 'X' or \
        c4['text'] == 'X' and c5['text'] == 'X' and c6['text'] == 'X' or \
        c7['text'] == 'X' and c8['text'] == 'X' and c9['text'] == 'X' or \
        c3['text'] == 'X' and c5['text'] == 'X' and c7['text'] == 'X' or \
        c2['text'] == 'X' and c5['text'] == 'X' and c8['text'] == 'X' or \
        c3['text'] == 'X' and c6['text'] == 'X' and c9['text'] == 'X'):
        tkinter.messagebox.showinfo('Vencedor X', 'Jogador X venceu o Jogo.\n Para jogar novamente, selecione a dificuldade.')
        newgame()
        
    elif (c1['text'] == 'O' and c2['text'] == 'O' and c3['text'] == 'O' or \
          c1['text'] == 'O' and c5['text'] == 'O' and c9['text'] == 'O' or \
          c1['text'] == 'O' and c4['text'] == 'O' and c7['text'] == 'O' or \
          c4['text'] == 'O' and c5['text'] == 'O' and c6['text'] == 'O' or \
          c7['text'] == 'O' and c8['text'] == 'O' and c9['text'] == 'O' or \
          c3['text'] == 'O' and c5['text'] == 'O' and c7['text'] == 'O' or \
          c2['text'] == 'O' and c5['text'] == 'O' and c8['text'] == 'O' or \
          c3['text'] == 'O' and c6['text'] == 'O' and c9['text'] == 'O'):
        tkinter.messagebox.showinfo('Vencedor O', 'Voce perdeu o jogo!!!\n Para jogar novamente, selecione a dificuldade.')
        newgame()
        
    elif (c1['text'] != ' ' and c2['text'] != ' ' and c3['text'] != ' ' and \
          c4['text'] != ' ' and c5['text'] != ' ' and c6['text'] != ' ' and \
          c7['text'] != ' ' and c8['text'] != ' ' and c9['text'] != ' '):
        tkinter.messagebox.showinfo('Ninguém venceu.', 'Deu velha!\n Para jogar novamente, selecione a dificuldade.')
        newgame()
    
def newgame():
    global jogada, modo
    root.destroy()
    jogada = 0
    modo = 0
    main()
main()
