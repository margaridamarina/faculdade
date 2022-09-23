nota1 = float(input('Informe a primeira nota: '))
print(nota1)

nota2 = float(input('Informe a segunda nota: '))
print(nota2)

nota3 = float(input('Informe a terceira nota: '))
print(nota3)

nota4 = float(input('Informe a quarta nota: '))
print(nota4)

media = (nota1 + nota2 + nota3 + nota4) / 4

if media > 7.0:
    print('A media do aluno foi: %.2f e o aluno esta aprovado'%(media))
else:
    print('A media do aluno foi: %.2f e o aluno esta reprovado' % (media))