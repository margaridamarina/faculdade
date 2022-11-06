import csv

def dict_gabarito():
    with open('gabarito.csv') as f:
        DictReader_obj = csv.DictReader(f)
        for resposta in DictReader_obj:
            return resposta
print('DICIONÁRIO DO GABARITO: ', dict_gabarito())
dict_gabarito = dict_gabarito()


def lista_dicts_respostas():
    lista_dicts_respostas = []
    with open('respostas.csv') as f:
        DictReader_obj = csv.DictReader(f)
        for resposta in DictReader_obj:
            lista_dicts_respostas.append((resposta))
    return lista_dicts_respostas
print('LISTA DE DICIONÁRIOS COM RESPOSTAS: ',lista_dicts_respostas())
lista_dicts_respostas = lista_dicts_respostas()


def lista_respostas_questao1():
    lista_respostas_questao1 = [resposta['resposta1'] for resposta in lista_dicts_respostas]
    return lista_respostas_questao1
print('LISTA DE RESPOSTAS DA QUESTÃO 1: ',lista_respostas_questao1())
lista_respostas_questao1 = lista_respostas_questao1()


def checa_acertos_questao1():
    i = 0
    while i < len(lista_respostas_questao1):
        if lista_respostas_questao1[i] == dict_gabarito['resposta1']:
            lista_respostas_questao1[i] = 1
        else:
            lista_respostas_questao1[i] = 0
        i += 1
    return lista_respostas_questao1
print('LISTA DE ACERTOS DA QUESTÃO 1:', checa_acertos_questao1())
checa_acertos_questao1 = checa_acertos_questao1()


def lista_respostas_questao2():
    lista_respostas_questao2 = [resposta['resposta2'] for resposta in lista_dicts_respostas]
    return lista_respostas_questao2
print('LISTA DE RESPOSTAS DA QUESTÃO 2: ',lista_respostas_questao2())
lista_respostas_questao2 = lista_respostas_questao2()


def checa_acertos_questao2():
    i = 0
    while i < len(lista_respostas_questao2):
        if lista_respostas_questao2[i] == dict_gabarito['resposta2']:
            lista_respostas_questao2[i] = 1
        else:
            lista_respostas_questao2[i] = 0
        i += 1
    return lista_respostas_questao2
print('LISTA DE ACERTOS DA QUESTÃO 2:', checa_acertos_questao2())
checa_acertos_questao2 = checa_acertos_questao2()

