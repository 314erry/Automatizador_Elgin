import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NUMEROS_SERIES_PATH = os.path.join(BASE_DIR, "numeros.txt")

def stringLinha():
    print('-' * 40)

def salvarNumSeries():
    stringLinha()
    print("Digite os novos números de série para salvar:")
    print("(Apenas 1 nº de série por linha e pressione Enter duas vezes para finalizar):")

    try:
        linhas = []
        while True:
            linha = input()
            if linha == "":
                break
            linhas.append(linha)

        if not linhas:
            print("Digite os Nº de Série para salvar. Tente Novamente.")
            return

        with open(NUMEROS_SERIES_PATH, "w") as arquivo:
            arquivo.write("\n".join(linhas))
    except Exception as e:
        print("Erro:", e)
        
    print("Números de série salvos com sucesso!")

def menu():
    while True:    
        stringLinha()
        print()
        print("  ██╗      ██████╗  ██████╗  █████╗ ")
        print("  ██║     ██╔═══██╗██╔════╝ ██╔══██╗")
        print("  ██║     ██║   ██║██║  ███╗███████║")
        print("  ██║     ██║   ██║██║   ██║██╔══██║")
        print("  ███████╗╚██████╔╝╚██████╔╝██║  ██║")
        print("  ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝")
        print("      Automatizador TOTVS v1.9.4")
        print("         © 2024 Pierry Jonny")
        print()
        print("Menu:")
        print("1. Endereçamento")
        print("2. Transferência Múltipla")
        print("3. Solicitar")
        print("4. Baixar Pré-Requisitos")
        print("5. Salvar Nº Série")
        print("6. Listar Nº Série")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            enderacamento()
        elif opcao == "2":
            transferenciaMultipla()
        elif opcao == "3":
            solicitar()
        elif opcao == "4":
            baixar()
        elif opcao == "5":
            salvarNumSeries()
        elif opcao == "6":
            listarNumSerie()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
            
menu()
