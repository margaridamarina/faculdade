total_figurinhas = int(input()) # ignore
colecao_figurinhas = [int(valor) for valor in input().split()][:total_figurinhas]
qtd_figurinhas = [int(valor) for valor in input().split()][:total_figurinhas]
consultas = int(input()) #ignore

lista_de_troca_de_figurinha = [int(valor) for valor in input().split()][:consultas]

tamanho_colecao_figurinha = len(colecao_figurinhas)
for figurinha in lista_de_troca_de_figurinha:
    esq = 0
    dir = tamanho_colecao_figurinha - 1
    posicao = -1

    while esq <= dir:
        meio = (esq + dir) // 2

        if figurinha == colecao_figurinhas[meio] :
            posicao = meio
            break
        elif figurinha < colecao_figurinhas[meio]:
            dir = meio - 1
        else:
            esq = meio + 1

    if posicao == -1:
        print('Quero')
    elif qtd_figurinhas[posicao] > 1:
        print('Trocar')
    else:
        print('Apenas uma')
