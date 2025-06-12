#Calculadora 

#importando tkinter
from tkinter import *
from tkinter import ttk

#Cores
cor_preta = "#000000"  # Preto
cor_branca = "#FFFFFF"  # Branco
cor_azul = "#141b26"  # Azul
cor_cinza = "#808080"  # Cinza
cor_laranja = "#FFA500"  # Laranja

#Criando a janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.configure(bg=cor_preta)

#Criando o frame
frame_tela = Frame(janela, width=300, height=100, bg=cor_azul)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=300, height=300, bg=cor_preta)
frame_corpo.grid_propagate(False)  # Impede que o frame redimensione automaticamente
frame_corpo.grid(row=1, column=0)    


todos_valores = ""  # Variável global para armazenar os valores digitados


#Criando Funções
valor_texto = StringVar()  # Variável para armazenar o texto a ser exibido na tela

def entrar_valores(event):
    #pegando o valor do botão
    global todos_valores
    todos_valores = todos_valores + str(event)

    valor_texto.set(todos_valores) #passando valor para tela

#Função para calcular o resultado
def calcular():
    global todos_valores
    resultado = eval(todos_valores)  # Avalia a expressão matemática
    valor_texto.set(str(resultado))  # Atualiza o texto na tela

#Função para limpar a tela
def limpar_tela():
    global todos_valores
    todos_valores = ""  # Limpa a variável global
    valor_texto.set("")  # Atualiza o texto na tela
    


#Criando Label

app_label = Label(frame_tela, textvariable=valor_texto, width=18, height=2, padx=7, relief=FLAT, anchor="e", justify="right", bg=cor_azul, fg=cor_branca, font=("Arial", 20))
app_label.place(x=0, y=5)

#Criando botões
b_1 = Button(frame_corpo, command = limpar_tela, text="AC", width=16, height=2, bg=cor_cinza, fg=cor_preta, font=("Arial", 12))
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, command = lambda: entrar_valores("%"), text="%", width=8, height=2, bg=cor_cinza, fg=cor_preta, font=("Arial", 12))
b_2.place(x=153, y=0)

b_3 = Button(frame_corpo, command = lambda: entrar_valores("/"), text="/", width=8, height=2, bg=cor_laranja, fg=cor_branca, font=("Arial", 12))
b_3.place(x=229, y=0)

b_4 = Button(frame_corpo, command = lambda: entrar_valores("7"), text="7", width=7, height=2, bg=cor_cinza, fg=cor_preta, font=("Arial", 12))
b_4.place(x=0, y=50)

b_5 = Button(frame_corpo, command = lambda: entrar_valores("8"), text="8", width=8, height=2, bg=cor_cinza, fg=cor_preta, font=("Arial", 12))
b_5.place(x=72, y=50)

b_6 = Button(frame_corpo, command = lambda: entrar_valores("9"), text="9", width=8, height=2, bg=cor_cinza, fg=cor_preta, font=("Arial", 12))
b_6.place(x=153, y=50)

b_7 = Button(frame_corpo, command = lambda: entrar_valores("*"), text="*", width=8, height=2, bg=cor_laranja, fg=cor_branca, font=("Arial", 12))
b_7.place(x=229, y=50)

b_8 = Button(frame_corpo, command = lambda: entrar_valores("4"), text="4", width=7, height=2, bg=cor_cinza, fg=cor_preta, font=("Arial", 12))
b_8.place(x=0, y=100)

b_9 = Button(frame_corpo, command = lambda: entrar_valores("5"), text="5", width=8, height=2, bg=cor_cinza, fg=cor_preta, font=("Arial", 12))
b_9.place(x=72, y=100)

b_10 = Button(frame_corpo, command = lambda: entrar_valores("6"), text="6", width=8, height=2, bg=cor_cinza, fg=cor_preta, font=("Arial", 12))
b_10.place(x=153, y=100)

b_11 = Button(frame_corpo, command = lambda: entrar_valores("-"), text="-", width=8, height=2, bg=cor_laranja, fg=cor_branca, font=("Arial", 12))
b_11.place(x=229, y=100)

b_12 = Button(frame_corpo, command = lambda: entrar_valores("1"), text="1", width=7, height=2, bg=cor_cinza, fg=cor_preta, font=("Arial", 12))
b_12.place(x=0, y=150)

b_13 = Button(frame_corpo, command = lambda: entrar_valores("2"), text="2", width=8, height=2, bg=cor_cinza, fg=cor_preta, font=("Arial", 12))
b_13.place(x=72, y=150)

b_14 = Button(frame_corpo, command = lambda: entrar_valores("3"), text="3", width=8, height=2, bg=cor_cinza, fg=cor_preta, font=("Arial", 12))
b_14.place(x=153, y=150)

b_15 = Button(frame_corpo, command = lambda: entrar_valores("+"), text="+", width=8, height=2, bg=cor_laranja, fg=cor_branca, font=("Arial", 12))
b_15.place(x=229, y=150)

b_16 = Button(frame_corpo, command = lambda: entrar_valores("0"), text="0", width=16, height=2, bg=cor_cinza, fg=cor_preta, font=("Arial", 12))
b_16.place(x=0, y=200)

b_17 = Button(frame_corpo, command = lambda: entrar_valores("."), text=".", width=8, height=2, bg=cor_cinza, fg=cor_preta, font=("Arial", 12))
b_17.place(x=153, y=200)

b_18 = Button(frame_corpo, command = calcular, text="=", width=8, height=2, bg=cor_laranja, fg=cor_branca, font=("Arial", 12))
b_18.place(x=229, y=200)




janela.mainloop()