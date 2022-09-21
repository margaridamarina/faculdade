resp = 'S'
maior = menor = quant = média = soma = 0
while resp in 'Ss':
  nota = int(input('Digite a nota de um aluno: '))
  soma += nota
  quant += 1
  if quant == 1:
    maior = menor = nota
  else:
    if nota > maior:
      maior = nota
    if nota < menor:
      menor = nota
  resp = str(input('Quer digitar mais uma nota? S/N '))
  média = soma/quant
print(f'A média das notas foi {média}')
print(f'A maior nota foi {maior}')
print(f'A menor nota foi {menor}')
