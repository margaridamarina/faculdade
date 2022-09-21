resp = 'S'
maior = quant = 0
while resp in 'Ss':
  num = int(input('Digite um número: '))
  quant += 1
  if quant == 1:
    maior = num
  else:
    if num > maior:
      maior = num
  resp = str(input('Quer digitar mais um número? S/N '))
print(f'O maior número foi {num}')