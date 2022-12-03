numero_planetas = int(input())
lista_planeta = []
lista_urgencia = []
for planeta in range(numero_planetas):
    identificacao_planeta, grau_urgencia = input().split()
    lista_urgencia.append(int(grau_urgencia))
    lista_planeta.append(int(identificacao_planeta))

lista_junto = []
for planeta, ugencia in zip(lista_planeta, lista_urgencia):
    items = planeta, ugencia
    lista_junto.append(items)
# print(lista_junto)

# n = len(lista_urgencia)
# for inicio in range(1, n, -1):
#     i = inicio
#     while i >= 1 and lista_urgencia[i] < lista_urgencia[i+1]:
#         lista_urgencia[i], lista_urgencia[i+1] = lista_urgencia[i+1], lista_urgencia[i]
#         i += 1
# print(lista_urgencia)

sorted(lista_urgencia, reverse=True)

lista_ordenada = sorted(lista_junto, key=lambda lista_junto: lista_junto[1], reverse=True)
# print(lista_ordenada)

for planeta, urgencia in lista_ordenada:
    print (planeta, urgencia)