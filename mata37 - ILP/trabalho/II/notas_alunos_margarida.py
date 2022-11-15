import csv
#EXTRAI DADOS DAS PLANILHAS
def informa_matriz_gabarito():
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


def informa_matriz_respostas():
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


#MANIPULA DADOS EXTRAÍDOS
def gera_listas_respostas_alunos_separadas(lista_respostas_alunos, numero_questoes):
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
        lista_matriculas.append(int(resposta[1]))
    # print('A lista das matrículas é: ', lista_matriculas)
    return lista_matriculas
lista_matriculas = lista_matriculas(informa_matriz_respostas())


def lista_nomes(matriz_resp):
    lista_nomes = []
    for resposta in matriz_resp:
        lista_nomes.append(resposta[3])
    # print('A lista com os nomes dos alunos é: ', lista_nomes)
    return lista_nomes
lista_nomes = lista_nomes(informa_matriz_respostas())


def lista_notas(matriz_respostas_sep):
    lista_acertos = []
    for resposta in matriz_respostas_sep:
        # print('As respostas separadas do aluno foi:', resposta)
        lista_acertos.append(compara_respostas(resposta, lista_gabarito(informa_matriz_gabarito())))
    # print('A lista de acertos foi:', lista_acertos)
    return lista_acertos
lista_notas = lista_notas(gera_listas_respostas_alunos_separadas(lista_respostas(informa_matriz_respostas()), 10))    


#RESPONDE QUESTÃO 1 - LISTA EM ORDEM ALFABÉTICA DOS ALUNOS COM O NÚMERO DE MATRICULA E A SUA NOTA.
def lista_nomes_sorteados(lista_nomes_sortear):
    lista_nomes_sorteados = sorted(lista_nomes_sortear)
    # print('A lista com os nomes dos alunos sorteada é: ', lista_nomes_sorteados)
    return lista_nomes_sorteados
lista_nomes_sorteados = lista_nomes_sorteados(lista_nomes)


def infoma_nome_matricula_nota(lista_nom, lista_mat, lista_not):
    infos_alunos = []
    for i, j, k in zip(lista_nom, lista_mat, lista_not):
        items = i, j, k
        infos_alunos.append(items)
    # print('O conjunto de tuplas com informações de cada aluno é: ', infos_alunos)
    return infos_alunos
infoma_nome_matricula_nota = infoma_nome_matricula_nota(lista_nomes, lista_matriculas, lista_notas)


def informa_lista_matricula_nota(info):
    dict_info_aluno = {}
    for item in info:
        dict_info_aluno[item[0]] = [item[1], item[2]]
    # print('O conjunto de dicts com informações de cada aluno é: ', dict_info_aluno)
    return dict_info_aluno
informa_lista_matricula_nota = informa_lista_matricula_nota(infoma_nome_matricula_nota)


def infoma_nomeOrdemAlfabetica_matricula_nota(info_alun, lista_nom_sort):
    lista_ordenada_nomes = [(key, info_alun[key]) for key in lista_nom_sort] 
    print(f"A lista em ordem alfabética dos alunos seguida pelo número de matricula e a sua nota é: " + str(lista_ordenada_nomes))
infoma_nomeOrdemAlfabetica_matricula_nota(informa_lista_matricula_nota, lista_nomes_sorteados)


#RESPONDE QUESTÃO 2 - LISTA EM ORDEM CRESCENTE DE NOTAS COM O NOME DO ALUNO, O NUMERO DA MATRICULA E A SUA NOTA.
#RESPONDE QUESTÃO 3 - LISTA EM ORDEM CRESCENTE DE NOTAS COM O NOME DO ALUNO, O NUMERO DA MATRICULA E A SUA NOTA PARA OS ALUNOS APROVADOS (>= 7.0).
#RESPONDE QUESTÃO 4 - LISTA EM ORDEM DECRESCENTE DE NOTAS COM O NOME DO ALUNO, O NUMERO DA MATRICULA E A SUA NOTA PARA OS ALUNOS REPROVADOS (< 7.0).
#RESPONDE QUESTÃO 5 - O PERCENTUAL DE APROVAÇÃO, SABENDO-SE QUE A NOTA MÍNIMA PARA APROVAÇÃO É >= 7.0.
#RESPONDE QUESTÃO 6 - A NOTA QUE TEVE A MAIOR FREQUÊNCIA ABSOLUTA.
#RESPONDE QUESTÃO 7 - O ALUNO COM A MAIOR NOTA (NOME, MATRICULA E NOTA).
#RESPONDE QUESTÃO 8 - O ALUNO COM A MENOR NOTA (NOME, MATRICULA E NOTA).
#RESPONDE QUESTÃO 9 - A MÉDIA DA TURMA
