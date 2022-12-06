qtd_contas = int(input())
lista_contas = []
for _ in range(qtd_contas):
    contas = [int(x) for x in input().split()]
    lista_contas.append(contas)
# print(lista_contas)

def ordenacao_vencimento(lista_contas):
    return lista_contas[2]
        
def ordenacao_valores(lista_contas):
    return -lista_contas[1]


def ordenacao_identificadores(lista_contas):
    return lista_contas[0]

lista_organizada = sorted(lista_contas, key=lambda lista_contas: (ordenacao_vencimento(lista_contas), ordenacao_valores(lista_contas), ordenacao_identificadores(lista_contas)))
# print(lista_organizada)

for lista in lista_organizada:
    print(lista[0])