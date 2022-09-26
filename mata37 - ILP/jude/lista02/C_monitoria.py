from math import sqrt
X1,Y1,X2,Y2 = input().split()
X1 = float(X1) 
Y1 = float(Y1) 
X2 = float(X2) 
Y2 = float(Y2) 
dist_carro_buraco = sqrt(((X2-0)**2) + ((Y2-0)**2))
dist_carro_pedestre = sqrt(((X1-0)**2) + ((Y1-0)**2))
print(dist_carro_pedestre)
print(dist_carro_buraco)
if (dist_carro_pedestre <= 7 and dist_carro_buraco <= 5):
  print("Aprovado no teste")
elif (dist_carro_pedestre > 7 and dist_carro_buraco < 5):
  print("Pedestre nao identificado")
elif (dist_carro_buraco > 5 and dist_carro_pedestre < 7):
  print("Buraco nao identificado")
elif (dist_carro_buraco > 5 and dist_carro_pedestre > 7):
  print("Nao passou no teste")