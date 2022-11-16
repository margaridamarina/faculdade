import csv

def coleta_matriz_gabarito():
    matriz_gab = []
    with open("gabarito.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            gabarito_junto = ''.join(row)
            matriz_gab.append(gabarito_junto.split(';'))
        # print('A matriz do gabarito é: ', matriz_gab)
        return matriz_gab


def lista_gabarito(matriz_gab):
    lista_gabarito = []
    for questao in matriz_gab:
        lista_gabarito.append(questao[1])
    # print('As respostas corretas são: ', lista_gabarito)
    return lista_gabarito


def coleta_matriz_respostas():
    matriz_resp = []
    with open("respostas.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            respostas_junto = ''.join(row)
            matriz_resp.append(respostas_junto.split('; '))
        # print('A matriz das respostas dos alunos é:', matriz_resp)
        return matriz_resp


def lista_respostas(matriz_resp):
    lista_respostas_alunos = []
    for lin in range(len(matriz_resp)):
        for col in range(5,25,2):
            respostas = matriz_resp[lin][col]
            lista_respostas_alunos.append(respostas)
    # print('As respostas foram: ', lista_respostas_alunos)
    return lista_respostas_alunos
