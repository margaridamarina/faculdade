# pressao_maxima = int(input())
# pressao_medida = int(input())

# pressao_atual = 0

# while pressao_medida != 0:
#   if pressao_medida <= pressao_maxima:
#     pressao_atual = pressao_atual
#   else:
#     pressao_atual = pressao_medida
#   pressao_medida = int(input())

# if pressao_atual > pressao_maxima:
#   print('ALARME')
# else: 
#   print('O Havai pode dormir tranquilo')

T = int(input())
P = int(input())

PA = 0

while P != 0:
  if P <= T:
    PA = PA
  else:
    PA = P
  P = int(input())

if PA > T:
  print('ALARME')
else: 
  print('O Havai pode dormir tranquilo')