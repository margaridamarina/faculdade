A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)
if A == B == C:
  print('Empate')
else:
  if(A == B):
    print("C")
  else:
    if(A == C):
      print("B")
    else:
      print("A")