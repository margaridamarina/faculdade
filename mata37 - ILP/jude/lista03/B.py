#ENTENDIMENTO PROBLEMA
#Saber total amigos viajando
#Saber quantas pessoas cabem em cada tipo de quarto
#Ir somando pessoas já alocadas 

#PRINT PEDIDO
# qtd_amigos_viajando = int(input())

# qtd_hospedes_alocados = 0
# qtd_total_hospedes_alocados = 0
# nomes_quartos = ''

# while True:
#     nomes_quartos = str(input())
#     if nomes_quartos == 'Casal':
#         qtd_total_hospedes_alocados += 2
#     if nomes_quartos == 'Triplo':
#         qtd_total_hospedes_alocados += 3
#     if nomes_quartos == 'Quadruplo':
#         qtd_total_hospedes_alocados += 4
#     if nomes_quartos == 'Familia':
#         qtd_total_hospedes_alocados += 5
#     if nomes_quartos == 'FIM':
#         break
# if qtd_total_hospedes_alocados >= qtd_amigos_viajando:
#     print('Pode reservar! Esses quartos cabem todos.')
# else:
#     print('Procure outra pousada.')

#VARIAVEIS RENOMEADAS
N = int(input())

qtd_hospedes_alocados = 0
qtd_total_hospedes_alocados = 0
nomes_quartos = ''

while True:
    nomes_quartos = str(input())
    if nomes_quartos == 'Casal':
        qtd_total_hospedes_alocados += 2
    if nomes_quartos == 'Triplo':
        qtd_total_hospedes_alocados += 3
    if nomes_quartos == 'Quadruplo':
        qtd_total_hospedes_alocados += 4
    if nomes_quartos == 'Familia':
        qtd_total_hospedes_alocados += 5
    if nomes_quartos == 'FIM':
        break
if qtd_total_hospedes_alocados >= N:
    print('Pode reservar! Esses quartos cabem todos.')
else:
    print('Procure outra pousada.')