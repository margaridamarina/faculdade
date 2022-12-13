total_figurinhas = int(input())
colecao_figurinhas = list(map(int, input().split()))
qtd_figurinhas = list(map(int, input().split()))
consultas = input()
figurinhas = list(map(int, input().split()))

for figurinha in figurinhas:
    n = len(colecao_figurinhas)
    esq = 0
    dir = n - 1
    posicao = 0
    while esq <= dir:
        meio = (esq + dir) // 2
        if colecao_figurinhas[meio] == figurinha:
            break
        elif figurinha < colecao_figurinhas[meio]:
            dir = meio - 1
        else:
            esq = meio + 1
    if colecao_figurinhas[meio] == figurinha:
        posicao = meio
    else:
        posicao = -1
    # print(posicao)

    if posicao == -1:
        print('Quero')
    else:
        if qtd_figurinhas[posicao] > 1:
            print('Trocar')
        if qtd_figurinhas[posicao] == 1:
            print('Apenas uma')
