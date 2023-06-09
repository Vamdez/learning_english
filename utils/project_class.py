from utils.print_menu import menu_principal, menu_listar_palavras
from utils.data_manipulation import listar_palavras
from random import choice

class Menu:
    def __init__(self):
        self.ingles, self.traducao = listar_palavras()
        self.escolher_opc()

    def escolher_opc(self):
        while True:
            menu_principal()
            opc = int(input("Escolha uma opção: "))
            match opc:
                case 1:
                    self.add_palavra()
                case 2:
                    self.listar_palavras()
                case 3:
                    self.teste()
                case 4:
                    break

    def add_palavra(self):
        add_ingles = input(str("Digite a palavra em Inglês que deseja add: "))
        add_traducao = input(str("Digite a traducao: "))
        with open("utils/palavras.txt", "a") as lista:
            lista.write(f"\n{add_ingles} - {add_traducao}")

    def listar_palavras(self):
        menu_listar_palavras()
        for ind in range(len(self.ingles)):
            print(f"{self.ingles[ind]:-<20}"
                  f"{self.traducao[ind]:<20}")
        print("\n")

    def teste(self):
        temp = self.ingles[:]
        count = 0
        while temp:
            value = choice(temp)
            print(value, end="")
            resp = input(str("- "))
            print(f"{resp} - {self.traducao[self.ingles.index(value)]}")
            certo = input(str("Acertou? [s/n]"))
            if certo == "s":
                count += 1
            temp.remove(value)
        print(f"Acertos {count}/{len(self.ingles)}")
