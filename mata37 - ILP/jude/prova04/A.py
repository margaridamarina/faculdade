import collections

numero_acoes = int(input())
lista_acoes = []
lista_precos = []
for _ in range(numero_acoes):
    acao, preco = input().split()
    lista_acoes.append(acao)
    lista_precos.append(preco)
# print(lista_precos)

lista_precos_inteiros = []
for preco in lista_precos:
    preco_int = int(preco)
    lista_precos_inteiros.append(preco_int)

qtd_compras = int(input())
lista_acoes_compradas = []
lista_qtd = []
for _ in range(qtd_compras):
    acao_comprada, qtd = input().split()
    lista_acoes_compradas.append(acao_comprada)
    lista_qtd.append(qtd)
# print(lista_qtd)

lista_qtd_inteiras = []
for qtd in lista_qtd:
    qtd_int = int(qtd)
    lista_qtd_inteiras.append(qtd_int)

# print(lista_acoes)
# print(lista_precos_inteiros)
# print(lista_acoes_compradas)
# print(lista_qtd_inteiras)

lista_junto_preco = []
for acao, preco in zip(lista_acoes, lista_precos_inteiros):
    items = acao, preco
    lista_junto_preco.append(items)
# print(lista_junto_preco)

lista_junto_qtd = []
for acao_comprada, qtd in zip(lista_acoes_compradas, lista_qtd_inteiras):
    items = acao_comprada, qtd
    lista_junto_qtd.append(items)
# print(lista_junto_qtd)

data_qtd = collections.defaultdict(list)
for k, v in (lista_junto_qtd):
    data_qtd[k].append(v)
dicionario_qtd = dict(data_qtd)
# print(dicionario_qtd)
for k, v in dicionario_qtd.items():
    dicionario_qtd[k] = sum(v)
# print(dicionario_qtd)

data_preco = collections.defaultdict(list)
for k, v in (lista_junto_preco):
    data_preco[k].append(v)
dicionario_preco = dict(data_preco)
# print(dicionario_preco)
for k, v in dicionario_preco.items():
    dicionario_preco[k] = sum(v)
# print(dicionario_preco)

result = {key: dicionario_preco[key] * dicionario_qtd[key] for key in dicionario_preco}
# print(result)

values = result.values() 
total = sum(values) 
print(total)