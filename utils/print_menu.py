from utils.data_manipulation import listar_palavras

def linha():
    print("-"*40)


def menu_principal():
    print("-------APRENDER INGLÊS COM PYTHON-------\n")
    print("1- Adicionar nova palavra")
    print("2- Listar todas as palavras")
    print("3- Começar Teste")


def menu_listar_palavras():
    linha()
    print(f"{'Listas de Palavras':>28}")
    linha()
    print(f"\033[1;32m"
          f"{'Inglês':<21}"
          f"\033[1;34m"
          f"{'Tradução':<20}"
          f"\033[m")

