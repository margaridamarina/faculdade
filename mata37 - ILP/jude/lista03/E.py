#PRINT PEDIDO
# qtd_pessoas = int(input())

# numero_mulheres = 0
# numero_homens = 0

# for i in range(qtd_pessoas):
#     S = int(input())
#     if S == 2:
#         numero_mulheres += 1
#     if S == 1:
#         numero_homens += 1
# print(numero_homens)
# print(numero_mulheres)

#VARIAVEIS RENOMEADAS
N = int(input())

numero_mulheres = 0
numero_homens = 0

for i in range(N):
    S = int(input())
    if S == 2:
        numero_mulheres += 1
    if S == 1:
        numero_homens += 1
print(numero_homens)
print(numero_mulheres)
