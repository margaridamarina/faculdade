X1,Y1,X2,Y2 = map(int,input().split())
dist_carro_pedestre = ((X1**2) + (Y1**2))**0.5
dist_carro_buraco = (((X2 - X1)**2 + (Y2 - Y1 )**2)**0.5)

if (dist_carro_buraco > 5 and dist_carro_pedestre > 7):
  print("Nao passou no teste")
elif (dist_carro_buraco > 5):
  print("Buraco nao identificado")
elif (dist_carro_pedestre > 7):
  print("Pedestre nao identificado")
else:
  print("Aprovado no teste")