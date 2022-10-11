    # ENTENDIMENTO PROBLEMA
# F1 = int(input())
# F2 = 2*F1
# F3 = 2*F2
# F4 = 2*F3

    #PRINTS MAIS CLAROS
# qtd_familiares, qtd_bolinhas_primeiro_familiar = input().split()

# qtd_familiares = int(qtd_familiares)
# qtd_bolinhas_primeiro_familiar = int(qtd_bolinhas_primeiro_familiar)

# qtd_total_bolinhas = qtd_bolinhas_primeiro_familiar

# print('----')

# for i in range(1, qtd_familiares+1):
#     print(i, end=' ')
#     print(qtd_total_bolinhas)
#     qtd_total_bolinhas = qtd_total_bolinhas*2

    #PRINT PEDIDO
# qtd_familiares, qtd_bolinhas_primeiro_familiar = input().split()

# qtd_familiares = int(qtd_familiares)
# qtd_bolinhas_primeiro_familiar = int(qtd_bolinhas_primeiro_familiar)

# qtd_total_bolinhas = qtd_bolinhas_primeiro_familiar

# for i in range(1, qtd_familiares+1):
#     qtd_total_bolinhas = qtd_total_bolinhas*2
# print(qtd_total_bolinhas)

    #VARIAVEIS RENOMEADAS E PRINT PEDIDO
N, Q = input().split()

N = int(N)
Q = int(Q)

qtd_total_bolinhas = Q

for i in range(1, N+1):
    qtd_total_bolinhas = qtd_total_bolinhas*2
print(qtd_total_bolinhas-Q)
