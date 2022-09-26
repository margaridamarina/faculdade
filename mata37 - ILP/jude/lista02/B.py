N = float(input())
if (N >= 1850):
  print("Passou o Limite")
elif (N < 1850):
  print('{:.2f} de limite disponivel'.format(1850-N))