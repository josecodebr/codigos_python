import json
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
    
    
agenda = []

def limpar_tela():
    # Verifica o sistema operacional para determinar o comando correto
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para macOS e Linux (Unix)
        os.system('clear')
        
def carregar_dados():
    global agenda
    try:
        with open("agenda.json", "r") as file:
            agenda = [json.loads(line.strip()) for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        agenda = []

def listar_agenda():
    carregar_dados()
    if not agenda:
        print(f"{cor.CIANO}Nada Encontrado.\n{cor.FIM}")
    else:
        for cliente in agenda:
            print(cliente)
        print()

def menu():
    limpar_tela()  # Limpa a tela antes de exibir o menu
    while True:
        
        print(f"{cor.AZUL}1. Consultar Agenda{cor.FIM}")
        print(f"{cor.VERMELHO}2. Sair{cor.FIM}\n")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            listar_agenda()
        elif opcao == "2":
            limpar_tela()  # Limpa a tela antes de exibir o menu
            break
        else:
            limpar_tela()  # Limpa a tela antes de exibir o menu
            print(f"{cor.VERMELHO}Opção inválida, tente novamente.\n{cor.FIM}")

menu()
