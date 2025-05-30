import tkinter as tk

janela = tk.Tk() #variavel recebe tk
janela.title("Exemplo Radiobutton") # Titulo da janela
janela.geometry("300x200") #resolucao da janela

var = tk.StringVar()  #variavel 'var' e definida para recebe valores do tipo string

rb1 = tk.Radiobutton(janela, text=" Opeção 1", variable=var, value="1")#e definido na variavel 'eb1' uma opcao de valor 1 para a variavel 'var'
rb2 = tk.Radiobutton(janela, text=" Opeção 2", variable=var, value="2")#e definido na variavel 'eb2' uma opcao de valor 2 para a variavel 'var'
rb3 = tk.Radiobutton(janela, text=" Opeção 3", variable=var, value="3")#e definido na variavel 'eb3' uma opcao de valor 3 para a variavel 'var'

rb1.pack() # mostra na tela a opcao contida em rb1
rb2.pack() # mostra na tela a opcao contida em rb2
rb3.pack() # mostra na tela a opcao contida em rb3

# define a funcao  mostra_opcao
def mostrar_opção(): 
    print("Você escolheu a opção: ", var.get()) #mostra natela uma frasse e a opcao escolhida armazenada em 'var'

botao = tk.Button(janela, text="Mostra escolha", command=mostrar_opção) #define um botao para chamar a funcao mostrar_opção
botao.pack()#coloca botao na tela

janela.mainloop() #repeticao principal
