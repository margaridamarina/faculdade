A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)
if A < 500:
  print('Chegou a parada 1')
if (B+A) < 500:
  print('Chegou a parada 2')
if (C+B+A) < 500:
  print('Chegou a parada 3')
  print('Conseguiu com {} litros de sobra!'.format(500-(A+B+C)))
else: 
  print('Nao foi possivel chegar ao seu destino :(')