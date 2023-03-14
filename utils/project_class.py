from utils.print_menu import menu_principal, menu_listar_palavras
from utils.data_manipulation import listar_palavras


class Menu:
    def __init__(self):
        menu_principal()
        self.ingles, self.traducao = listar_palavras()
        self.escolher_opc()

    def escolher_opc(self):
        opc = int(input("Escolha uma opção: "))
        match opc:
            case 1:
                self.add_palavra()
            case 2:
                self.listar_palavras()
            case 3:
                self.teste

    def add_palavra(self):
        pass

    def listar_palavras(self):
        menu_listar_palavras()
        for ind in range(len(self.ingles)):
            print(f"{self.ingles[ind]:-<20}"
                  f"{self.traducao[ind]:<20}")


    def teste(self):
        pass
