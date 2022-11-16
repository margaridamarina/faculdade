import dados_extracao

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
        lista_acertos.append(compara_respostas(resposta, dados_extracao.lista_gabarito(dados_extracao.coleta_matriz_gabarito())))
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