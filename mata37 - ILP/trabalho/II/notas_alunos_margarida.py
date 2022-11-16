import csv


#EXTRAI DADOS DAS PLANILHAS
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


#MANIPULA DADOS EXTRAÍDOS
def separa_respostas_alunos(lista_respostas_alunos, numero_questoes):
    lista_aluno_separado = []
    for i in range(0, len(lista_respostas_alunos), numero_questoes):
        lista_aluno_separado.append(lista_respostas_alunos[i:i + numero_questoes])
    return lista_aluno_separado


def compara_respostas(respostas_aluno, lista_gab):  
    qtd_acertos = 0
    for i in range(len(respostas_aluno)):
        if respostas_aluno[i] == lista_gab[i]:
            qtd_acertos = qtd_acertos + 1 
    # print('A quantidade de acertos foi:', qtd_acertos)
    return qtd_acertos

def lista_matriculas(matriz_resp):
    lista_matriculas = []  
    for resposta in matriz_resp:
        lista_matriculas.append(resposta[1])
    # print('A lista das matrículas é: ', lista_matriculas)
    return lista_matriculas


def lista_nomes(matriz_resp):
    lista_nomes = []
    for resposta in matriz_resp:
        lista_nomes.append(resposta[3])
    # print('A lista com os nomes dos alunos é: ', lista_nomes)
    return lista_nomes


def coleta_lista_notas(matriz_respostas_sep):
    lista_acertos = []
    for resposta in matriz_respostas_sep:
        # print('As respostas separadas do aluno foi:', resposta)
        lista_acertos.append(compara_respostas(resposta, lista_gabarito(coleta_matriz_gabarito())))
    # print('A lista de acertos foi:', lista_acertos)
    return lista_acertos

def lista_aprovados(lista_ac):
    lista_aprovados = []
    for nota in lista_ac:
        if nota >= 7:
            lista_aprovados.append(nota)
    # print(lista_aprovados)
    return lista_aprovados


def coleta_nome_matricula_nota(lista_nom, lista_mat, lista_not):
    infos_alunos = []
    for nome, matricula, nota in zip(lista_nom, lista_mat, lista_not):
        items = nome, matricula, nota
        infos_alunos.append(items)
    # print('O conjunto de tuplas com coletações de cada aluno é: ', infos_alunos)
    return infos_alunos


#RESPONDE QUESTÃO 1 - LISTA EM ORDEM ALFABÉTICA DOS ALUNOS COM O NÚMERO DE MATRICULA E A SUA NOTA.
def coleta_nome_ordem_alfabetica_matricula_nota(info_alunos):
    lista_ordenada_nomes = sorted(info_alunos, key=lambda info_alunos: info_alunos[0], reverse=False) 
    return lista_ordenada_nomes


#RESPONDE QUESTÃO 2 - LISTA EM ORDEM CRESCENTE DE NOTAS COM O NOME DO ALUNO, O NUMERO DA MATRICULA E A SUA NOTA.
def coleta_lista_ordenada_por_nota(infos_notas): 
    lista_notas_ordenada = sorted(infos_notas, key=lambda infos_notas: infos_notas[2], reverse=False) 
    return lista_notas_ordenada


# RESPONDE QUESTÃO 3 - LISTA EM ORDEM CRESCENTE DE NOTAS COM O NOME DO ALUNO, O NUMERO DA MATRICULA E A SUA NOTA PARA OS ALUNOS APROVADOS (>= 7.0).
def coleta_nota_crescente_matricula_nota_aprovados(lista_notas_cres):
    lista_notas_crescentes_aprovados = list(filter(lambda lista_notas_cres: lista_notas_cres[2] >= 7, lista_notas_cres))
    return lista_notas_crescentes_aprovados


#RESPONDE QUESTÃO 4 - LISTA EM ORDEM DECRESCENTE DE NOTAS COM O NOME DO ALUNO, O NUMERO DA MATRICULA E A SUA NOTA PARA OS ALUNOS REPROVADOS (< 7.0).
def coleta_nota_decrescente_matricula_nota_aprovados(infos_notas, lista_notas_decresc):
    lista_notas_decrescente = sorted(infos_notas, key=lambda infos_notas: infos_notas[2], reverse=True) 
    lista_notas_decrescente_reprovados = list(filter(lambda lista_notas_decrescente: lista_notas_decrescente[2] < 7, lista_notas_decrescente))
    return lista_notas_decrescente_reprovados


#RESPONDE QUESTÃO 5 - O PERCENTUAL DE APROVAÇÃO, SABENDO-SE QUE A NOTA MÍNIMA PARA APROVAÇÃO É >= 7.0.
def coleta_percentual_aprovacao(lista_notas_checar):
    lista_aprovados = []
    for nota in lista_notas_checar:
        if nota >= 7:
            lista_aprovados.append(nota)
    percentual = len(lista_aprovados)/len(lista_notas_checar)
    return percentual


#RESPONDE QUESTÃO 6 - A NOTA QUE TEVE A MAIOR FREQUÊNCIA ABSOLUTA.
def coleta_frequencia_absoluta(lista_notas_checar):
    lista_frequencias = []
    for nota in lista_notas_checar:
        frequencia = lista_notas_checar.count(nota)
        lista_frequencias.append(frequencia)
    frequencia_por_nota = dict(zip(lista_notas_checar, lista_frequencias))
    return frequencia_por_nota


#RESPONDE QUESTÃO 7 - O ALUNO COM A MAIOR NOTA (NOME, MATRICULA E NOTA).
def coleta_aluno_maior_nota(infos_alunos_notas, lista_not):
    maior_nota = max(number for number in lista_not)
    lista_maior_nota = list(filter(lambda infos_alunos_notas: infos_alunos_notas[2] == maior_nota, infos_alunos_notas))
    return lista_maior_nota


#RESPONDE QUESTÃO 8 - O ALUNO COM A MENOR NOTA (NOME, MATRICULA E NOTA).
def coleta_aluno_menor_nota(infos_alunos_notas, lista_not):
    menor_nota = min(number for number in lista_not)
    lista_menor_nota = list(filter(lambda infos_alunos_notas: infos_alunos_notas[2] == menor_nota, infos_alunos_notas))
    return lista_menor_nota


#RESPONDE QUESTÃO 9 - A MÉDIA DA TURMA
def coleta_media_turma(lista_notas_checar):
    somatorio = 0
    for nota in lista_notas_checar:
        somatorio += nota
    media = somatorio/len(lista_notas_checar)
    return media


#RODA PROGRAMA
if __name__ == "__main__":
    #EXTRAÇÃO DE DADOS
    matriz_resposta = coleta_matriz_respostas()
    respostas = lista_respostas(matriz_resposta)
    separados = separa_respostas_alunos(respostas, 10)
    
    #MANIPULAÇÃO DE DADOS
    list_notas = coleta_lista_notas(separados)    
    list_matriculas = lista_matriculas(coleta_matriz_respostas())
    list_nomes = lista_nomes(coleta_matriz_respostas())
    nome_matricula_nota = coleta_nome_matricula_nota(list_nomes, list_matriculas, list_notas)

    #RESPOSTAS
    lista_ordenada_por_nome = coleta_nome_ordem_alfabetica_matricula_nota(nome_matricula_nota)
    print(f"QUESTÃO 1: A lista em ordem alfabética dos alunos com o número de matricula e a sua nota é: " + str(lista_ordenada_por_nome))
    
    lista_ordenada_por_nota = coleta_lista_ordenada_por_nota(nome_matricula_nota)
    print( f"QUESTÃO 2: A lista em ordem crescente de notas com o nome do aluno, o numero da matricula e a sua nota.: " + str(lista_ordenada_por_nota))
    
    lista_nota_crescente = coleta_nota_crescente_matricula_nota_aprovados(lista_ordenada_por_nota)
    print(f"QUESTÃO 3: A lista em ordem crescente de notas com o nome do aluno, o numero da matricula e a sua nota para os alunos aprovados (>= 7.0). é:" + str(lista_nota_crescente))
    
    lista_nota_decrescente = coleta_nota_decrescente_matricula_nota_aprovados(nome_matricula_nota, lista_ordenada_por_nota)
    print(f"QUESTÃO 4: A lista em ordem decrescente de notas com o nome do aluno, o numero da matricula e a sua nota para os alunos reprovados (< 7.0). é:" + str(lista_nota_decrescente))

    percentua_aprovacao = coleta_percentual_aprovacao(list_notas)
    print(f'QUESTÃO 5: O percentual de aprovação, sabendo-se que a nota mínima para aprovação é >=7.0, foi {percentua_aprovacao:.2%}', )
    
    frequencia_absoluta = coleta_frequencia_absoluta(list_notas)
    print('QUESTÃO 6: A frequência de cada nota é:', frequencia_absoluta)
    
    maior_nota = coleta_aluno_maior_nota(nome_matricula_nota, list_notas)
    print('QUESTÃO 7: O aluno com a maior nota (nome, matricula e nota).', maior_nota)
    
    menor_nota = coleta_aluno_menor_nota(nome_matricula_nota, list_notas)
    print('QUESTÃO 8: O aluno com a menor nota (nome, matricula e nota).', menor_nota)
    
    media_turma = coleta_media_turma(list_notas)
    print(f'QUESTÃO 9: A média da turma é {media_turma:.2f}')