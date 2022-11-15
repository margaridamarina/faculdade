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
        lista_matriculas.append(resposta[1])
    # print('A lista das matrículas é: ', lista_matriculas)
    return lista_matriculas
list_matriculas = lista_matriculas(informa_matriz_respostas())


def lista_nomes(matriz_resp):
    lista_nomes = []
    for resposta in matriz_resp:
        lista_nomes.append(resposta[3])
    # print('A lista com os nomes dos alunos é: ', lista_nomes)
    return lista_nomes
list_nomes = lista_nomes(informa_matriz_respostas())


def lista_notas(matriz_respostas_sep):
    lista_acertos = []
    for resposta in matriz_respostas_sep:
        # print('As respostas separadas do aluno foi:', resposta)
        lista_acertos.append(compara_respostas(resposta, lista_gabarito(informa_matriz_gabarito())))
    # print('A lista de acertos foi:', lista_acertos)
    return lista_acertos
list_notas = lista_notas(gera_listas_respostas_alunos_separadas(lista_respostas(informa_matriz_respostas()), 10))    


def lista_aprovados(lista_ac):
    lista_aprovados = []
    for nota in lista_ac:
        if nota >= 7:
            lista_aprovados.append(nota)
    # print(lista_aprovados)
    return lista_aprovados
lista_aprovados(list_notas)

def infoma_nome_matricula_nota(lista_nom, lista_mat, lista_not):
    infos_alunos = []
    for i, j, k in zip(lista_nom, lista_mat, lista_not):
        items = i, j, k
        infos_alunos.append(items)
    # print('O conjunto de tuplas com informações de cada aluno é: ', infos_alunos)
    return infos_alunos
inform_nome_matricula_nota = infoma_nome_matricula_nota(list_nomes, list_matriculas, list_notas)


#RESPONDE QUESTÃO 1 - LISTA EM ORDEM ALFABÉTICA DOS ALUNOS COM O NÚMERO DE MATRICULA E A SUA NOTA.
def informa_nomeOrdemAlfabetica_matricula_nota(info_alunos):
    lista_ordenada_nomes = sorted(info_alunos, key=lambda info_alunos: info_alunos[0], reverse=False) 
    print(f"QUESTÃO 1: A lista em ordem alfabética dos alunos com o número de matricula e a sua nota é: " + str(lista_ordenada_nomes))
informa_nomeOrdemAlfabetica_matricula_nota(inform_nome_matricula_nota)


#RESPONDE QUESTÃO 2 - LISTA EM ORDEM CRESCENTE DE NOTAS COM O NOME DO ALUNO, O NUMERO DA MATRICULA E A SUA NOTA.
def informa_notaOrdenada_nome_matricula_nota(infos_notas): 
    lista_notas_ordenada = sorted(infos_notas, key=lambda infos_notas: infos_notas[2], reverse=False) 
    print( f"QUESTÃO 2: A lista em ordem crescente de notas com o nome do aluno, o numero da matricula e a sua nota.: " + str(lista_notas_ordenada))
    return lista_notas_ordenada
inform_notaOrdenada_nome_matricula_nota = informa_notaOrdenada_nome_matricula_nota(inform_nome_matricula_nota)


# RESPONDE QUESTÃO 3 - LISTA EM ORDEM CRESCENTE DE NOTAS COM O NOME DO ALUNO, O NUMERO DA MATRICULA E A SUA NOTA PARA OS ALUNOS APROVADOS (>= 7.0).
def informa_notaCrescente_matricula_nota_aprovados(lista_notas_cres):
    lista_notas_crescentes_aprovados = list(filter(lambda lista_notas_cres: lista_notas_cres[2] >= 7, lista_notas_cres))
    print(f"QUESTÃO 3: A lista em ordem crescente de notas com o nome do aluno, o numero da matricula e a sua nota para os alunos aprovados (>= 7.0). é:" + str(lista_notas_crescentes_aprovados))
    return lista_notas_crescentes_aprovados
inform_notaCrescente_matricula_nota_aprovados = informa_notaCrescente_matricula_nota_aprovados(inform_notaOrdenada_nome_matricula_nota)


#RESPONDE QUESTÃO 4 - LISTA EM ORDEM DECRESCENTE DE NOTAS COM O NOME DO ALUNO, O NUMERO DA MATRICULA E A SUA NOTA PARA OS ALUNOS REPROVADOS (< 7.0).
def informa_notaDecrescente_matricula_nota_aprovados(infos_notas, lista_notas_decresc):
    lista_notas_decrescente = sorted(infos_notas, key=lambda infos_notas: infos_notas[2], reverse=True) 
    lista_notas_decrescente_reprovados = list(filter(lambda lista_notas_decrescente: lista_notas_decrescente[2] < 7, lista_notas_decrescente))
    print(f"QUESTÃO 4: A lista em ordem decrescente de notas com o nome do aluno, o numero da matricula e a sua nota para os alunos reprovados (< 7.0). é:" + str(lista_notas_decrescente_reprovados))
informa_notaDecrescente_matricula_nota_aprovados(inform_nome_matricula_nota, inform_notaOrdenada_nome_matricula_nota)


#RESPONDE QUESTÃO 5 - O PERCENTUAL DE APROVAÇÃO, SABENDO-SE QUE A NOTA MÍNIMA PARA APROVAÇÃO É >= 7.0.
def informa_percentual_aprovacao(lista_notas_checar):
    lista_aprovados = []
    for nota in lista_notas_checar:
        if nota >= 7:
            lista_aprovados.append(nota)
    percentual = len(lista_aprovados)/len(lista_notas_checar)
    print(f'QUESTÃO 5: O percentual de aprovação, sabendo-se que a nota mínima para aprovação é >=7.0, foi {percentual:.2%}', )
informa_percentual_aprovacao(list_notas)


#RESPONDE QUESTÃO 6 - A NOTA QUE TEVE A MAIOR FREQUÊNCIA ABSOLUTA.
def informa_frequencia_absoluta(lista_notas_checar):
    lista_frequencias = []
    for nota in lista_notas_checar:
        frequencia = lista_notas_checar.count(nota)
        lista_frequencias.append(frequencia)
    frequencia_por_nota = dict(zip(lista_notas_checar, lista_frequencias))
    print('QUESTÃO 6: A frequência de cada nota é:', frequencia_por_nota)
informa_frequencia_absoluta(list_notas)


#RESPONDE QUESTÃO 7 - O ALUNO COM A MAIOR NOTA (NOME, MATRICULA E NOTA).
def informa_aluno_maior_nota(infos_alunos_notas, lista_not):
    maior_nota = max(number for number in lista_not)
    lista_maior_nota = list(filter(lambda infos_alunos_notas: infos_alunos_notas[2] == maior_nota, infos_alunos_notas))
    print('QUESTÃO 7: O aluno com a maior nota (nome, matricula e nota).', lista_maior_nota)
informa_aluno_maior_nota(inform_nome_matricula_nota, list_notas)


#RESPONDE QUESTÃO 8 - O ALUNO COM A MENOR NOTA (NOME, MATRICULA E NOTA).
def informa_aluno_menor_nota(infos_alunos_notas, lista_not):
    menor_nota = min(number for number in lista_not)
    lista_menor_nota = list(filter(lambda infos_alunos_notas: infos_alunos_notas[2] == menor_nota, infos_alunos_notas))
    print('QUESTÃO 8: O aluno com a menor nota (nome, matricula e nota).', lista_menor_nota)
informa_aluno_menor_nota(inform_nome_matricula_nota, list_notas)


#RESPONDE QUESTÃO 9 - A MÉDIA DA TURMA
def informa_media_turma(lista_notas_checar):
    somatorio = 0
    for nota in lista_notas_checar:
        somatorio += nota
    media = somatorio/len(lista_notas_checar)
    print(f'QUESTÃO 9: A média da turma é {media:.2f}', )
informa_media_turma(list_notas)