import collections

qtd_competidores, qtd_tentativas = input().split()
qtd_competidores = int(qtd_competidores)
qtd_tentativas = int(qtd_tentativas)
lista_tentativas = []
for _ in range(qtd_competidores):
    tentativas = [float(x) for x in input().split()]
    lista_tentativas.append(tentativas)
print(lista_tentativas)

listas_ordenadas = []
for indice in range(len(lista_tentativas)):
    n = len(lista_tentativas[indice])
    for inicio in range(1, n):
        i = inicio
        while i >= 1 and lista_tentativas[indice][i] < lista_tentativas[indice][i-1]:
            lista_tentativas[indice][i], lista_tentativas[indice][i-1] = lista_tentativas[indice][i-1], lista_tentativas[indice][i]
            i -= 1
    listas_ordenadas.append(lista_tentativas[indice])
print(listas_ordenadas)

lista_maiores = []
for item in listas_ordenadas:
    lista_maiores.append(item[qtd_tentativas-1])
# print(lista_maiores)

lista_menores = []
for item in listas_ordenadas:
    lista_menores.append(item[0])
# print(lista_menores)

lista_diferencas = [elemA - elemB for elemA, elemB in zip(lista_maiores, lista_menores)]
# print(lista_diferencas)

lista_competidores = []
for i in range(1, qtd_competidores+1):
    lista_competidores.append(i)
# print(lista_competidores)

lista_junto = []
for competidor, lista in zip(lista_competidores, listas_ordenadas):
    items = competidor, lista
    lista_junto.append(items)
# print(lista_junto)
data = collections.defaultdict(list)
for k, v in (lista_junto):
    data[k].append(v)
dicionario = dict(data)
# print(dicionario)

for lista in listas_ordenadas:
    if lista_menores[0] in lista:
        for k, v in dicionario.items():
            if lista in v:
                competidor = k
                
print("Competidor {} ganhou! {:.2f}s".format(competidor, lista_menores[0]))