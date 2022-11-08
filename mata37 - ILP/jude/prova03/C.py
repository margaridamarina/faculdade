lin, col = input().split()
lin = int(lin)
col = int(col)
matriz = []
for i in range(lin):
    lin_matriz = [int(x) for x in input().split()]
    matriz.append(lin_matriz)
lista_pokemons = []
for i in range(lin):
    for j in range(col):
        if matriz[i][j] > 0:
            lista_pokemons.append(matriz[i][j])
pokemon_desejado = int(input())
lista_pokemon_desejado = []
for pokemon in lista_pokemons:
    if pokemon == pokemon_desejado:
        lista_pokemon_desejado.append(pokemon)
print("Ash pegou {} pokemon".format(len(lista_pokemon_desejado)))