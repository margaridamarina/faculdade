tamanho_campo = int(input())
campo = []
ron = 0
harry = 0
for abobora in range(tamanho_campo):
    peso = [int(x) for x in input().split()]
    campo.append(peso)
linha_harry, coluna_ron = input().split()
linha_harry = int(linha_harry)
coluna_ron = int(coluna_ron)
for i in range(tamanho_campo):
    ron += campo[i][coluna_ron]
    campo[i][coluna_ron] = 0
    harry += campo[linha_harry][i]
    campo[linha_harry][i] = 0
print('Harry {}\nRon {}'.format(harry, ron))