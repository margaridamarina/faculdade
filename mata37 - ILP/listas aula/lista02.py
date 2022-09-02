def ex01():
  a = int(input())
  b = int(input())
  c = int(input())
  d = int(input())
  media=((a+b+c+d)/4)
  print(media)
  if media >=7:
    print("Você foi aprovado(a)!")
  else:
    print("Você não foi aprovado(a)!")

# ex01()

def ex02():
  senha = input()
  if senha == "ASDFG":
    print("Acesso permitido!")
  else:
    print("Acesso negado!")

# ex02()

def ex03():
  a = int(input())
  b = int(input())
  c = int(input())
  if (a < b+c) and (b < a+c) and (c < a+b):
    print("É um triângulo!")
  else:
    print("Não é um triângulo!")
  if (a==b) or (b==c):
    print("É um triângulo equilátero!")
  if (a==b) or (a==c) or (b==c):
    print("É um triângulo isósceles!")
  if (a!=b!=c):
    print("É um triângulo escaleno!")

# ex03()

def ex04():
  a = int(input())
  b = int(input())
  c = int(input())
  d = int(input())
  media=((a+b+c+d)/4)
  print(media)
  if media >=7:
    print("Você foi aprovado(a)!")
  if media >=3 and media <7:
    print("Você teve direito a prova final!")
    e = int(input())
    print("Digite aqui a sua nota:", e)
    if (e>=5):   
      print("Você foi aprovado(a) por conceito!")
    else:    
      print("Você foi reprovado(a) por conceito!")
  if media <=3:
    print("Você foi reprovado(a)!")

# ex04()

def ex05():
  a = int(input())
  if 5 <= a <= 7: 
    print("Você está na categoria infantil A")
  if 8 <= a <= 10: 
    print("Você está na categoria infantil B")
  if 11 <= a <= 13: 
    print("Você está na categoria juvenil A")
  if 14 <= a <= 17: 
    print("Você está na categoria juvenil B")
  if a > 18: 
    print("Você está na categoria sênior")

# ex05()

def ex06():
  print("Escolha um animal entre os seguintes: leão, cavalo, homem, macaco, morcego, baleia, avestruz, pinguim, pato, águia, tartaruga,crocodilo e cobra:")
  animal = input()

  print("Ele é mamífero? Responda com S ou N:")
  mamifero = input()
  print("Ele é quadrúpede? Responda com S ou N:")
  quadrupede = input()
  print("Ele é carnívoro? Responda com S ou N:")
  carnivoro = input()
  print("Ele é herbívoro? Responda com S ou N:")
  herbivoro = input()
  print("Ele é bípede? Responda com S ou N:")
  bipede = input()
  print("Ele é onívoro? Responda com S ou N:")
  onivoro = input()
  print("Ele é frutífero? Responda com S ou N:")
  frutifero = input()
  print("Ele é voador? Responda com S ou N:")
  voador = input()
  print("Ele é aquático? Responda com S ou N:")
  aquatico = input()
  print("Ele é ave? Responda com S ou N:")
  ave = input()
  print("Ele é tropical? Responda com S ou N:")
  tropical = input()
  print("Ele é polar? Responda com S ou N:")
  polar = input()
  print("Ele é nadador? Responda com S ou N:")
  nadador = input()
  print("Ele é de rapina? Responda com S ou N:")
  rapina = input()
  print("Ele é um réptil? Responda com S ou N:")
  reptil = input()
  print("Ele tem casco? Responda com S ou N:")
  casco = input()
  print("Ele tem pata? Responda com S ou N:")
  pata = input()

  if mamifero=="S" and quadrupede=="S" and carnivoro=="S":
    print("O animal escolhido foi", animal, " e o computador achou que é um leão!")
  if mamifero=="S" and quadrupede=="S" and herbivoro=="S":
    print("O animal escolhido foi", animal, " e o computador achou que é um cavalo!")
  if mamifero=="S" and bipede=="S" and onivoro=="S":
    print("O animal escolhido foi", animal, " e o computador achou que é um homem!")
  if mamifero=="S" and bipede=="S" and frutifero=="S":
    print("O animal escolhido foi", animal, " e o computador achou que é um macaco!")
  if mamifero=="S" and voador=="S":
    print("O animal escolhido foi", animal, " e o computador achou que é um morcego!")
  if mamifero=="S" and aquatico=="S":
    print("O animal escolhido foi", animal, " e o computador achou que é uma baleia!")
  if ave=="S" and voador=="N" and tropical=="S":
    print("O animal escolhido foi", animal, " e o computador achou que é um avestruz!")
  if ave=="S" and voador=="N" and polar=="S":
    print("O animal escolhido foi", animal, " e o computador achou que é um pinguim!")
  if ave=="S" and nadador=="S":
    print("O animal escolhido foi", animal, " e o computador achou que é um pato!")
  if ave=="S" and rapina=="S":
    print("O animal escolhido foi", animal, " e o computador achou que é uma águia!")
  if reptil=="S" and casco=="S":
    print("O animal escolhido foi", animal, " e o computador achou que é uma tartaruga!")
  if reptil=="S" and carnivoro=="S":
    print("O animal escolhido foi", animal, " e o computador achou que é um crocodilo!")
  if reptil=="S" and pata=="N":
    print("O animal escolhido foi", animal, " e o computador achou que é uma cobra!")

ex06()