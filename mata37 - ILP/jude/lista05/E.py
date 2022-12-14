qtd_bonecas = int(input()) #ignore

tamanho_bonecas = [ int(k) for k in input().split()]

consultas = int(input()) #ignore
maior_boneca = [int(x) for x in input().split()]

def get_maior(boneca):
    prev = boneca
    passaram = 0
    for (i, tamanho) in enumerate(tamanho_bonecas):
        if boneca == tamanho:
            return prev, i, passaram

        passaram =+1

        if boneca > tamanho:
            prev = tamanho

        elif boneca < tamanho:
            return prev, i, passaram

for boneca in maior_boneca:
    maior, i, passaram = get_maior(boneca)
    print(0 if i+passaram == 2 else i+passaram)
