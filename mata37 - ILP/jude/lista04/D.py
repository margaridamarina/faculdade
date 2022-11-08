jogo = []
coord = [0, 0]
lista_coord = []
for ponto_jogo in range(7):
    ponto = [x for x in input().split()]
    jogo.append(ponto)
for lin in range(7):
    for col in range(7):
        if jogo[lin][col] == '1':
            coord = [lin, col]
            lista_coord.append(coord)
# print('As coordenadas das peças são: ', lista_coord)
lista_juntos = []
for item in lista_coord:
    palavra = str(item[0]),str(item[1])
    junto = ''.join(palavra)
    lista_juntos.append(junto)
# print('A lista com as coordenação sem separação é:', lista_juntos)
lista_inversos = []
for item in lista_juntos:
    if item[0] != item[1]:
        inverso = item[::-1] #começar do início, terminar do fim, pegar de traz pra frente
        lista_inversos.append(inverso)
    for inv in lista_inversos:
        if inv in lista_juntos:
            lista_juntos.remove(inv)
# print('Os itens inversos são: ', lista_inversos)
# print('A lista sem os itens inversos é: ', lista_juntos)
# print('A quantidade de peças sem somar os inversos é: ', len(lista_juntos))
print(len(lista_juntos))

