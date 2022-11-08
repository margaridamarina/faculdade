lin, col = input().split()
lin = int(lin)
col = int(col)
mapa = []
for i in range(lin):
    lin_mapa = [int(x) for x in input().split()]
    mapa.append(lin_mapa)
for i in range(lin):
    if i % 2 != 0:
        lista_impar = mapa[i]
        lista_impar_contrario = [num for num in reversed(lista_impar)]
        mapa[i] = lista_impar_contrario
ovos = 0
for i in range(lin):
    for j in range(col):
        ovos += mapa[i][j]
        if ovos < 0:
            ovos = 0 
print(ovos)