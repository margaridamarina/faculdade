primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))
escolha = str(input('Deseja ordenar de maneira crescente ou decrescente? C/D: '))

if(terceiro < segundo):
    aux = terceiro
    terceiro = segundo
    segundo = aux

if(segundo < primeiro):
    aux = segundo
    segundo = primeiro
    primeiro = aux

if(terceiro < segundo):
    aux = terceiro
    terceiro = segundo
    segundo = aux

if(escolha in 'Cc'):
  print(primeiro,'-',segundo,'-',terceiro)
else:
  print(terceiro,'-',segundo,'-',primeiro)
