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

salvarNumSeries()
