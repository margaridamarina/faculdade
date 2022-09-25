T, D = input().split()
T = int(T)
D = int(D)
V, P = input().split()
V = int(V)
P = int(P)
qtd_pedagios = T//D
total_km = T*V
total_pedagios = qtd_pedagios*P
print(total_km + total_pedagios)