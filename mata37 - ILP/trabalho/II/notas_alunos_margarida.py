import csv

def matriz_gabarito():
    matriz_gab = []
    with open("gabarito.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            gabarito_junto = ''.join(row)
            matriz_gab.append(gabarito_junto.split(';'))
        print(matriz_gab)
        return matriz_gab
gabarito = matriz_gabarito()


def matriz_respostas():
    matriz_resp = []
    with open("respostas.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            respostas_junto = ''.join(row)
            matriz_resp.append(respostas_junto.split(';'))
        print(matriz_resp)
        return matriz_resp
respostas = matriz_respostas()


def lista_gabarito(matriz_gab):
    lista_gabarito = []
    for questao in matriz_gab:
        lista_gabarito.append(questao[1])
    print(lista_gabarito)
    return lista_gabarito
lista_gabarito = lista_gabarito(gabarito)


def lista_matriculas(matriz_resp):
    lista_matriculas = []
    for resposta in matriz_resp:
        lista_matriculas.append(resposta[1])
    print(lista_matriculas)
    return lista_matriculas
lista_matriculas = lista_matriculas(respostas)


def lista_nomes(matriz_resp):
    lista_nomes = []
    for resposta in matriz_resp:
        lista_nomes.append(resposta[3])
    print(lista_nomes)
    return lista_nomes
lista_nomes = lista_nomes(respostas)


def lista_respostas(matriz_resp):
    lista_respostas = []
    for resposta in matriz_resp:
        lista_respostas.append(resposta[5,7,9,11,13,15,17,19,21,23])
    print(lista_respostas)
    return lista_respostas
lista_respostas = lista_respostas(respostas)


# def lista_respostas_questao7():
#     lista_respostas_questao7 = [resposta['resposta7'] for resposta in lista_dicts_respostas]
#     return lista_respostas_questao7
# print('LISTA DE RESPOSTAS DA QUESTÃO 7: ',lista_respostas_questao7())
# lista_respostas_questao7 = lista_respostas_questao7()


# def checa_acertos_questao7():
#     i = 0
#     while i < len(lista_respostas_questao7):
#         if lista_respostas_questao7[i] == dict_gabarito['resposta7']:
#             lista_respostas_questao7[i] = 1
#         else:
#             lista_respostas_questao7[i] = 0
#         i += 1
#     return lista_respostas_questao7
# print('LISTA DE ACERTOS DA QUESTÃO 7:', checa_acertos_questao7())
# checa_acertos_questao7 = checa_acertos_questao7()

