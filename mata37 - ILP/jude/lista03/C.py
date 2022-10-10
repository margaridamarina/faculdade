#PRINT PEDIDO
# total_instrutores = int(input())
# maior_total_gols = 0
# for i in range(total_instrutores):
#     numero_instrutor, total_gols = input().split()
#     numero_instrutor = int(numero_instrutor)
#     total_gols = int(total_gols)
#     if total_gols > maior_total_gols:
#         maior_total_gols = total_gols
#         instrutor = numero_instrutor
# print('Instrutor {}'.format(instrutor))

#VARIAVEIS RENOMEADAS
N = int(input())
maior_total_gols = 0
for i in range(N):
    I, K = input().split()
    I = int(I)
    K = int(K)
    if K >= maior_total_gols:
        maior_total_gols = K
        instrutor = I
print('Instrutor {}'.format(instrutor))