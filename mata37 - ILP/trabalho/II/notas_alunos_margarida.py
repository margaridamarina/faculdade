import csv

def matriz_gabarito():
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


def matriz_respostas():
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


def gerador_listas_respostas_alunos_separadas(lista_respostas_alunos, numero_questoes):
    for i in range(0, len(lista_respostas_alunos), numero_questoes):
        yield lista_respostas_alunos[i:i + numero_questoes]


def compara_respostas(lista_a_ser_conferida, lista_gab):  
    comparacao = [i for i, j in zip(lista_a_ser_conferida, lista_gab) if i == j]
    qtd_acertos = len(comparacao)
    # print('Os matches são: ', comparacao)
    # print('A quantidade de acertos foi:', qtd_acertos)
    return qtd_acertos

def lista_matriculas(matriz_resp):
    lista_matriculas = []
    for resposta in matriz_resp:
        lista_matriculas.append(resposta[1])
    print('A lista das matrículas é: ', lista_matriculas)
    return lista_matriculas
lista_matriculas(matriz_respostas())


def lista_nomes(matriz_resp):
    lista_nomes = []
    for resposta in matriz_resp:
        lista_nomes.append(resposta[3])
    print('A lista com os nomes dos alunos é: ', lista_nomes)
    return lista_nomes
lista_nomes(matriz_respostas())


def lista_acertos(matriz_respostas_sep):
    lista_acertos = []
    for resposta in matriz_respostas_sep:
        # print('As respostas separadas do aluno foi:', resposta)
        lista_acertos.append(compara_respostas(resposta, lista_gabarito(matriz_gabarito())))
    print('A lista de acertos foi:', lista_acertos)
    return lista_acertos
lista_acertos(gerador_listas_respostas_alunos_separadas(lista_respostas(matriz_respostas()), 10))    