qtd_casais = int(input())
idades_homens = list(map(int, input().split()))
idades_mulheres = list(map(int, input().split()))

idades_homens_decrescente = sorted(idades_homens, reverse=True)
idades_mulheres_crescente = sorted(idades_mulheres)

lista_junto = []
for homem, mulher in zip(idades_homens_decrescente, idades_mulheres_crescente):
    items = homem, mulher
    lista_junto.append(items)
# print(lista_junto)

for homem, mulher in lista_junto:
    print (homem, mulher)