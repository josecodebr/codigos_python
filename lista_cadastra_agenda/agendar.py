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


def salvar_dados():
    with open("agenda.json", "w") as file:
        for dados in agenda:
            json.dump(dados, file)
            file.write("\n")

def carregar_dados():
    try:
        with open("agenda.json", "r") as file:
            global agenda
            agenda = [json.loads(line) for line in file.readlines()]
    except FileNotFoundError:
        agenda = []

def cadastrar_dados():
    dados = input("Digite os dados do dados (Data, Manha, Tarde, Noite) separados por vírgula: ")
    data, manha, tarde, noite = [dado.strip() for dado in dados.split(",")]
    dados = {"data": data, "manha": manha, "tarde": tarde, "noite": noite}
    agenda.append(dados)
    salvar_dados()
    print(f"{cor.MAGENTA}Evento cadastrado com sucesso!\n{cor.FIM}")

def menu():
    limpar_tela()  # Limpa a tela antes de exibir o menu
    carregar_dados()
    while True:
        print(f"{cor.VERDE}1. Registra Evento{cor.FIM}")
        print(f"{cor.VERMELHO}2. Sair{cor.FIM}\n")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_dados()
        elif opcao == "2":
            limpar_tela()  # Limpa a tela antes de exibir o menu
            break
        else:
            limpar_tela()  # Limpa a tela antes de exibir o menu
            print(f"{cor.VERMELHO}Opção inválida, tente novamente.\n{cor.FIM}")

menu()
