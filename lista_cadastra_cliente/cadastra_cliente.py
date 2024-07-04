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
    
clientes = []

def limpar_tela():
    # Verifica o sistema operacional para determinar o comando correto
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para macOS e Linux (Unix)
        os.system('clear')


def salvar_dados():
    with open("clientes.json", "w") as file:
        for cliente in clientes:
            json.dump(cliente, file)
            file.write("\n")

def carregar_dados():
    try:
        with open("clientes.json", "r") as file:
            global clientes
            clientes = [json.loads(line) for line in file.readlines()]
    except FileNotFoundError:
        clientes = []

def cadastrar_cliente():
    dados = input("Digite os dados do cliente (nome, idade, email) separados por vírgula: ")
    nome, idade, email = [dado.strip() for dado in dados.split(",")]
    cliente = {"nome": nome, "idade": idade, "email": email}
    clientes.append(cliente)
    salvar_dados()
    print(f"{cor.MAGENTA}Cliente cadastrado com sucesso!\n{cor.FIM}")

def menu():
    limpar_tela()  # Limpa a tela antes de exibir o menu
    carregar_dados()
    while True:
        print(f"{cor.VERDE}1. Cadastrar Cliente{cor.FIM}")
        print(f"{cor.VERMELHO}2. Sair{cor.FIM}\n")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            limpar_tela()  # Limpa a tela antes de exibir o menu
            break
        else:
            limpar_tela()  # Limpa a tela antes de exibir o menu
            print(f"{cor.VERMELHO}Opção inválida, tente novamente.\n{cor.FIM}")
menu()
