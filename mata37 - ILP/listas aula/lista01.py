#ex01 - Variáveis não devem começar com números ou símbolos

def ex02():
  notaAluno = 0
  nomeAluno = "João"
  matAluno = "mat37"
  sexo = "F"

  print(notaAluno)
  print(nomeAluno)
  print(matAluno)
  print(sexo)

# ex02()

def ex03():
  if 2*4 == 24/3:
    print(True)
  else:
    print(False)

  if 15%4 < 19//6:
    print(True)
  else:
    print(False)

  if 3*5/4 <= 3**2/3:
    print(True)
  else:
    print(False)

  if 2+8%7 >= 3*6-15:
    print(True)
  else:
    print(False)

# ex03()

def ex04():
  a = int(input())
  b = int(input())
  print(a*b)

# ex04()

def ex05():
  a = int(input())
  b = int(input())
  c = int(input())
  d = int(input())
  print((a+b+c+d)/4)

# ex05()

def ex06():
  print(42*60+42)

# ex06()

def ex07():
  print(10*(1/1.61))

# ex07()


def ex08():
  print(((0.6*20+3)+(0.6*20+(0.75*59))))

ex08()
