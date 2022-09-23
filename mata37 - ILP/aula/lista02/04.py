nota1 = float(input('Informe a primeira nota: '))
print(nota1)

nota2 = float(input('Informe a segunda nota: '))
print(nota2)

nota3 = float(input('Informe a terceira nota: '))
print(nota3)

nota4 = float(input('Informe a quarta nota: '))
print(nota4)

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7.0:
    print('Voce foi aprovado por media. A sua media foi: %.2f' %(media))
elif (media >= 3.0) and (media < 7.0):
    print('Voce tem direito a prova final. A sua media foi: %.2f' % (media))
    nota_prova_final = float(input('Informa a nota da prova final: '))
    if nota_prova_final >= 5.0:
        print('Voce foi aprovado por conceito. A sua nota na final foi: %.2f' % (nota_prova_final))
    else:
        print('Voce foi reprovado por conceito. A sua nota na prova final foi: %.2f' % (nota_prova_final))
else:
    print('Voce foi reprovado. A sua media foi: %.2f' %(media))