mapa = []
for ponto_mapa in range(10):
    ponto = [x for x in input().split()]
    mapa.append(ponto)
for lin in range(10):
    for col in range(10):
        if mapa[lin][col] == 't':
            if 0 < lin:
                if mapa[lin-1][col] == '*':
                    mapa[lin][col] = 'p'
            if lin < 9:
                if mapa[lin+1][col] == '*':
                    mapa[lin][col] = 'p'
            if 0 < col:
                if mapa[lin][col-1] == '*':
                    mapa[lin][col] = 'p'
            if col < 9:
                if mapa[lin][col+1] == '*':
                    mapa[lin][col] = 'p'
        print(mapa[lin][col], end=' ')
    print('')