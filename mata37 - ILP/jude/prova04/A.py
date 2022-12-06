from collections import defaultdict

numero_acoes = int(input())

acao_preco = {}
for _ in range(numero_acoes):
  acao, preco = input().split()
  acao_preco[acao] = int(preco)
  
qtd_compras = int(input())
mapa_acao_quantide_comprada = defaultdict(int)

for _ in range(qtd_compras):
  acao_comprada, qtd = input().split()
  as_int = int(mapa_acao_quantide_comprada[acao_comprada])
  mapa_acao_quantide_comprada[acao_comprada] = as_int + int(qtd)

somada = 0
for k, v in acao_preco.items():
  somada = somada+acao_preco[k] * mapa_acao_quantide_comprada[k]
print(somada)