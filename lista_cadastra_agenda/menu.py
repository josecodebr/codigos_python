import subprocess
import os  # Importe o módulo os para usar os comandos do sistema operacional

# Códigos ANSI para cores no terminal
class cor:
    VERDE = '\033[92m'
    VERMELHO = '\033[91m'
    AZUL = '\033[94m'
    AMARELO = '\033[93m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    FIM = '\033[0m'

def limpar_tela():
    # Verifica o sistema operacional para determinar o comando correto
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para macOS e Linux (Unix)
        os.system('clear')

def menu():
    limpar_tela()  # Limpa a tela antes de exibir o menu
    while True:
        print("Menu Agenda Jose\n")
        print(f"{cor.VERDE}1. Registrar Evento{cor.FIM}")
        print(f"{cor.AZUL}2. Consultar Agenda{cor.FIM}")
        
        #print("3. Sair\n")
        # Mensagem com cores
        print(f"{cor.VERMELHO}3. Fechar Agenda{cor.FIM}\n")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            limpar_tela()  # Limpa a tela antes de exibir o menu
            subprocess.run(["python", "agendar.py"])
        elif opcao == "2":
            limpar_tela()  # Limpa a tela antes de exibir o menu
            subprocess.run(["python", "consuntar.py"])
            
        elif opcao == "3":
            limpar_tela()  # Limpa a tela antes de exibir o menu
            print("Saiu...")
            break
        else:
            limpar_tela()  # Limpa a tela antes de exibir o menu
            print("Opção inválida, tente novamente.\n")

menu()
 
