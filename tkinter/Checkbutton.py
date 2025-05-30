import tkinter as tk

janela = tk.Tk() #variavel recebe tk
janela.title("Exemplo Checkbutton") # Titulo da janela
janela.geometry("300x200") #resolucao da janela

var = tk.IntVar() #variavel 'var' e definida para recebe valores do tipo Inteiro
check =tk.Checkbutton(janela,text="Aceito os termos", variable=var) #a variavel 'check' recebe um botao associado a variavel var
check.pack() #mostra botao check na tela

# definindo a funcao verificar 
def verificar():
    if var.get()==1: # test logico se var esta com valor inteiro 1
        print(var.get()) # testa o varlo que esta sendo recebido em var
        print("Marcado") # mostrar na 
    else: #do contrario se nao tiver valor
        print(var.get()) # testa o varlo que esta sendo recebido em var
        print("Desmarcado") # mostrar na tela

botao = tk.Button(janela, text="Verificar", command=verificar) #define um botao para chamar a funcao verificar
botao.pack() #coloca botao na tela

janela.mainloop() #repeticao principal
