import tkinter as tk

janela = tk.Tk() #variavel recebe tk
janela.title("Exemplo Entry") # Titulo da janela
janela.geometry("300x200") #resolucao da janela

#campo de texto
entrada = tk.Entry(janela) # variavel entrada recebe funcao cria o campo de texto
entrada.pack() # mostra na tela entrada de texto na tela
#campo 2
entrada2 = tk.Entry(janela) # variavel entrada2 recebe funcao cria o campo de texto
entrada2.pack() # mostra na tela entrada2 de texto na tela

#Definindo a funcao que vai ser chamada ao clicar no botao Mostrar
def mostrar_texto():
    texto = entrada.get() #Pega o que foi digitado no campo texto chamado entrada
    print("Você digitou: ", texto) #mostra no prompt de comando os dados digitado na caixa de texto entrada
    
    texto2 = entrada2.get() # #Pega o que foi digitado no campo texto chamado entrada2
    print ("Voce digitou na caixa2: ", texto2 ) #mostra no prompt de comando os dados digitado na caixa de texto entrada2

#botao
botao = tk.Button(janela, text="Mostar", command = mostrar_texto) # cria botao chamado Mostrar ao clicar executa a funcao mostrat_texto()
botao.pack() #mostra botao Mostrar na tela

janela.mainloop() #loop direto na funcao janela
