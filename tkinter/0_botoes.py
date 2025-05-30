import tkinter as tk

janela = tk.Tk() 
janela.title("Minha Janela")
janela.geometry("300x200") #Lagura x Altura

label = tk.Label(janela, text="Ola, José!")
label.pack()

def clique():
    print("Botão clicado")
def clique2():
    print ("Botão clicado 2")

botao = tk.Button(janela, text="Clique aqui", command=clique)
botao.pack()

botao2 = tk.Button(janela, text="Clique aqui2", command=clique2)
botao2.pack()

janela.mainloop()

# Principais widgets:
# Label → Texto.
# Button → Botão.
# Entry → Campo de texto.
# Frame → Bloco/container.
# Checkbutton → Caixa de seleção.
# Radiobutton → Botão de opção.
