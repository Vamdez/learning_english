
def listar_palavras():
    ingles_palavras, traducao_palavras = [], []
    palavras = open("utils/palavras.txt", "rt")
    dados_limpos = palavras.read().split("\n")
    if dados_limpos != [""]:
        ingles_palavras, traducao_palavras = separar_listas(dados_limpos)
        palavras.close()
    return ingles_palavras, traducao_palavras

def separar_listas(lista):
    temp, ingles, traducao = [], [], []
    for itens in lista:
        temp = itens.split("-")
        ingles.append(temp[0])
        traducao.append(temp[1])
    return ingles, traducao

