def encontra_palavra(linhas, palavra):
	pode_horizontal = True if len(linhas[0]) >= len(palavra) else False
	pode_vertical = True if len(linhas) >= len(palavra) else False

	for direcao, possivel in [('H', pode_horizontal), ('V', pode_vertical)]:
		if possivel:
			linhas_direcionadas = zip(*linhas) if direcao == 'V' else linhas
			for index_linha, linha in enumerate(linhas_direcionadas):
				indices_letra = encontra_horizontal(linha, palavra)
				if indices_letra:
					posicoes = [(index_linha, index_letra) for index_letra in indices_letra]
					posicoes = [posicao[::-1] for posicao in posicoes] if direcao == 'V' else posicoes
					return posicoes

def encontra_horizontal(linha, palavra):
	linha = ''.join(linha)
	invertida = palavra[::-1]
	for estilo_palavra in (palavra, invertida):
		if estilo_palavra in linha:
			return [linha.index(estilo_palavra) + n for n in range(len(estilo_palavra))]
	return False

def encontra_posicoes_na_linha(diagonal_posicao, palavra, sentido):
	linha = ''.join([diagonal[1] for diagonal in diagonal_posicao])
	invertida = palavra[::-1]

	indices_palavra = range(len(palavra)) if sentido == 'D' else range(len(palavra))[::-1]

	for estilo_palavra in (palavra, invertida):
		if estilo_palavra in linha:
			n = linha.index(estilo_palavra)
			return [diagonal_posicao[n + letra_index][0] for letra_index in indices_palavra]

tamanho_caca_palavras = int(input())
linhas = []
for letras in range(tamanho_caca_palavras):
    letra = [x for x in input().split()]
    linhas.append(letra)

palavra = [input()]
posicoes_achou = []
for p in palavra:
	posicoes = encontra_palavra(linhas, p)
	if posicoes:
		posicoes_achou.extend(posicoes)

matriz_final = []
for index_linha, linha in enumerate(linhas):
	print_linha = []
	for index_letra, letra in enumerate(linha):
		if (index_linha, index_letra) in posicoes_achou:
			print_linha += letra
		else:
			print_linha += '.'
	matriz_final.append(print_linha)
# print('A matriz final é: ', matriz_final)
# print('O tamanho da matriz final é: ', len(matriz_final))

lista_letras = []
for l in palavra[0]:
    lista_letras.append(l)
# print('A lista de letras separadas é: ', lista_letras)
tamanho_palavra = len(lista_letras)
# print('O tamanho da palavra é: ', tamanho_palavra)
# print('A primeira letra é: ', lista_letras[0])
# print('A última letra é: ', lista_letras[tamanho_palavra-1])

posicao_primeira_letra = 0, 0
posicao_letra_final = 0, 0
posicao_primeira_letra_limpa=''
posicao_letra_final_limpa=''

for lin in range(len(matriz_final)):
    for col in range(len(matriz_final)):
        if matriz_final[lin][col] == lista_letras[0]:
            posicao_primeira_letra = str(lin),str(col)
            posicao_primeira_letra_limpa = ' '.join(posicao_primeira_letra)
        elif matriz_final[lin][col] == lista_letras[tamanho_palavra-1]:
            posicao_letra_final = str(lin),str(col)
            posicao_letra_final_limpa = ' '.join(posicao_letra_final)
print(posicao_primeira_letra_limpa, posicao_letra_final_limpa)
