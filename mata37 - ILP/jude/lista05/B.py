qtd_participantes = int(input())
part = list(map(int, input().split()))
part_ordenada = sorted(part)
for i in range(8):
    print(part_ordenada[i], end=' ')

