qtd_bonecas = int(input())
tamanho_bonecas = list(map(int, input().split()))
consultas = int(input())
maior_boneca = list(map(int, input().split()))

lista_posicao_maior_boneca = []
for i in range(consultas):
    n = len(tamanho_bonecas)
    esq = 0
    dir = n - 1
    posicao_maior_boneca = 0
    while esq <= dir:
        meio = (esq + dir) // 2
        if tamanho_bonecas[meio] == maior_boneca[i]:
            break
        elif maior_boneca[i] < tamanho_bonecas[meio]:
            dir = meio - 1
        else:
            esq = meio + 1
    if tamanho_bonecas[meio] == maior_boneca[i]:
        posicao_maior_boneca = meio
        lista_posicao_maior_boneca.append(posicao_maior_boneca)
    else:
        posicao_maior_boneca = -1
        lista_posicao_maior_boneca.append(posicao_maior_boneca)

print(lista_posicao_maior_boneca)
for i in lista_posicao_maior_boneca:
    if lista_posicao_maior_boneca[i] != -1: 
        quantidade_maioskas = posicao_maior_boneca + 1
        if quantidade_maioskas < 2: 
            quantidade_maioskas = 0
        print(quantidade_maioskas)
    else:
        lista_bonecas_menores = [] 
        for boneca in tamanho_bonecas:
            if boneca <= maior_boneca[i]:
                lista_bonecas_menores.append(boneca)
        quantidade_maioskas = len(lista_bonecas_menores) + 1
        if quantidade_maioskas < 2: 
            quantidade_maioskas = 0
        print(quantidade_maioskas)

