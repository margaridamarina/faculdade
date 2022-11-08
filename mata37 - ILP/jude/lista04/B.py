tamanho_campo, teleportes = input().split()
tamanho_campo = int(tamanho_campo)
teleportes = int(teleportes)
campo = []
naves_destruidas = 0
for localidades in range(tamanho_campo):
    localidade = [int(x) for x in input().split()]
    campo.append(localidade)
for local in range(teleportes):
    dim_x, dim_y = input().split()
    dim_x, dim_y = int(dim_x), int(dim_y)
    for i in range(dim_x, -1, -1):
        if campo[i][dim_y] == 1:
            naves_destruidas += 1
            campo[i][dim_y] = 0
            break
print(naves_destruidas)