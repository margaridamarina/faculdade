import dados_manipulacao, dados_extracao

num_questoes = 10

def coleta_nome_ordem_alfabetica_matricula_nota(info_alunos):
    lista_ordenada_nomes = sorted(info_alunos, key=lambda info_alunos: info_alunos[0], reverse=False) 
    return lista_ordenada_nomes


def coleta_lista_ordenada_por_nota(infos_notas): 
    lista_notas_ordenada = sorted(infos_notas, key=lambda infos_notas: infos_notas[2], reverse=False) 
    return lista_notas_ordenada


def coleta_nota_crescente_matricula_nota_aprovados(lista_notas_cres):
    lista_notas_crescentes_aprovados = list(filter(lambda lista_notas_cres: lista_notas_cres[2] >= 7, lista_notas_cres))
    return lista_notas_crescentes_aprovados


def coleta_nota_decrescente_matricula_nota_aprovados(infos_notas, lista_notas_decresc):
    lista_notas_decrescente = sorted(infos_notas, key=lambda infos_notas: infos_notas[2], reverse=True) 
    lista_notas_decrescente_reprovados = list(filter(lambda lista_notas_decrescente: lista_notas_decrescente[2] < 7, lista_notas_decrescente))
    return lista_notas_decrescente_reprovados


def coleta_percentual_aprovacao(lista_notas_checar):
    lista_aprovados = []
    for nota in lista_notas_checar:
        if nota >= 7:
            lista_aprovados.append(nota)
    percentual = len(lista_aprovados)/len(lista_notas_checar)
    return percentual


def coleta_frequencia_absoluta(lista_notas_checar):
    lista_frequencias = []
    for nota in lista_notas_checar:
        frequencia = lista_notas_checar.count(nota)
        lista_frequencias.append(frequencia)
    frequencia_por_nota = dict(zip(lista_notas_checar, lista_frequencias))
    return frequencia_por_nota


def coleta_aluno_maior_nota(infos_alunos_notas, lista_not):
    maior_nota = max(number for number in lista_not)
    lista_maior_nota = list(filter(lambda infos_alunos_notas: infos_alunos_notas[2] == maior_nota, infos_alunos_notas))
    return lista_maior_nota


def coleta_aluno_menor_nota(infos_alunos_notas, lista_not):
    menor_nota = min(number for number in lista_not)
    lista_menor_nota = list(filter(lambda infos_alunos_notas: infos_alunos_notas[2] == menor_nota, infos_alunos_notas))
    return lista_menor_nota


def coleta_media_turma(lista_notas_checar):
    somatorio = 0
    for nota in lista_notas_checar:
        somatorio += nota
    media = somatorio/len(lista_notas_checar)
    return media


def menu():
    while True:
        print("""\033[33m
        Digite a opção desejada:
        \033[35m
        1. A lista em ordem alfabética dos alunos com o número de matricula e a sua nota.
        2. A lista em ordem crescente de notas com o nome do aluno, o numero da matricula e a sua nota.
        3. A lista em ordem crescente de notas com o nome do aluno, o numero da matricula e a sua nota para os alunos aprovados (>= 7.0).
        4. A lista em ordem decrescente de notas com o nome do aluno, o numero da matricula e a sua nota para os alunos reprovados (< 7.0).
        5. O percentual de aprovação, sabendo-se que a nota mínima para aprovação é >=7.0.
        6. A nota que teve a maior frequência absoluta.
        7. O aluno com a maior nota (nome, matricula e nota).
        8. O aluno com a menor nota (nome, matricula e nota)
        9. A média da turma.
        
        0. Sair do programa.
        """)
        opcao = int(input('\033[33m'))
        if opcao == 1:
            lista_ordenada_por_nome = coleta_nome_ordem_alfabetica_matricula_nota(nome_matricula_nota)
            print(f"\033[33mQUESTÃO 1: A lista em ordem alfabética dos alunos com o número de matricula e a sua nota é: \n" + str(lista_ordenada_por_nome))
        elif opcao == 2:
            lista_ordenada_por_nota = coleta_lista_ordenada_por_nota(nome_matricula_nota)
            print( f"\033[33mQUESTÃO 2: A lista em ordem crescente de notas com o nome do aluno, o numero da matricula e a sua nota é: \n" + str(lista_ordenada_por_nota))
        elif opcao == 3:
            lista_nota_crescente = coleta_nota_crescente_matricula_nota_aprovados(lista_ordenada_por_nota)
            print(f"\033[33mQUESTÃO 3: A lista em ordem crescente de notas com o nome do aluno, o numero da matricula e a sua nota para os alunos aprovados (>= 7.0). é: \n" + str(lista_nota_crescente))
        elif opcao == 4:
            lista_nota_decrescente = coleta_nota_decrescente_matricula_nota_aprovados(nome_matricula_nota, lista_ordenada_por_nota)
            print(f"\033[33mQUESTÃO 4: A lista em ordem decrescente de notas com o nome do aluno, o numero da matricula e a sua nota para os alunos reprovados (< 7.0). é: \n" + str(lista_nota_decrescente))
        elif opcao == 5:
            percentua_aprovacao = coleta_percentual_aprovacao(list_notas)
            print(f'\033[33mQUESTÃO 5: O percentual de aprovação, sabendo-se que a nota mínima para aprovação é >=7.0, foi {percentua_aprovacao:.2%}', )
        elif opcao == 6:
            frequencia_absoluta = coleta_frequencia_absoluta(list_notas)
            print('\033[33mQUESTÃO 6: A frequência de cada nota é:', frequencia_absoluta)
        elif opcao == 7:
            maior_nota = coleta_aluno_maior_nota(nome_matricula_nota, list_notas)
            print('\033[33mQUESTÃO 7: O aluno com a maior nota (nome, matricula e nota) foi: \n', maior_nota)
        elif opcao == 8:
            menor_nota = coleta_aluno_menor_nota(nome_matricula_nota, list_notas)
            print('\033[33mQUESTÃO 8: O aluno com a menor nota (nome, matricula e nota) foi: \n', menor_nota)
        elif opcao == 9:
            media_turma = coleta_media_turma(list_notas)
            print(f'\033[33mQUESTÃO 9: A média da turma é {media_turma:.2f}')
        elif opcao == 0:
            print(f'\033[33mTchau!')
            break
        else:
            print(f'\033[33mEssa opção não existe!')
            break



#RODA PROGRAMA
if __name__ == "__main__":
    #EXTRAÇÃO DE DADOS
    matriz_resposta = dados_extracao.coleta_matriz_respostas()
    respostas = dados_extracao.lista_respostas(matriz_resposta)
    
    #MANIPULAÇÃO DE DADOS
    separados = dados_manipulacao.separa_respostas_alunos(respostas, num_questoes)
    list_notas = dados_manipulacao.coleta_lista_notas(separados)    
    list_matriculas = dados_manipulacao.lista_matriculas(matriz_resposta)
    list_nomes = dados_manipulacao.lista_nomes(matriz_resposta)
    nome_matricula_nota = dados_manipulacao.coleta_nome_matricula_nota(list_nomes, list_matriculas, list_notas)

    #RESULTADOS
    menu()
    
    
    