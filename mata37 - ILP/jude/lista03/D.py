#PRINT PEDIDO
# qtd_campeoes = int(input())
# maior_poder = 0
# for i in range(qtd_campeoes):
#     poder = int(input())
#     if poder > maior_poder:
#         maior_poder = poder
# print(maior_poder)

#VARIAVEIS RENOMEADAS
N = int(input())
maior_poder = 0
for i in range(N):
    P = int(input())
    if P >= maior_poder:
        maior_poder = P
print(maior_poder)
