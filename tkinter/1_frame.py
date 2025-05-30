import tkinter as tk

janela = tk.Tk() #variavel recebe tk
janela.title("Exemplo Frame") # Titulo da janela
janela.geometry("300x200") #resolucao da janela

frame =tk.Frame(janela, bg="#F00", width=200, height=100) #cria um container de tamanho 200x10, BG e cor de fundo 
frame.pack(pady=20) # espaco vertical Exibe o container na tela

#Colocando widgets dentro do Frame
label = tk.Label(frame, text="Dentro do Frame") #Variavel label recebe  elemento conteiner
label.pack() #mstra label na tela

botao = tk.Button(frame, text="Botao no Frame") #variavel botao faz Container frame receber um botao
botao.pack() #mostar na tela

janela.mainloop() #atualizacoes do codigo na tela
