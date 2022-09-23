a = int(input('Informe o lado do primeiro triangulo'))
b = int(input('Informe o lado do segundo triangulo'))
c = int(input('Informe o lado do terceiro triangulo'))

if (a < b + c) and (b < a + c) and (c < a + b):
    if (a == b == c):
        print('Triangulo equilatero')
    elif (a == b) or (a == c) or (b == c):
        print('Triangulo isosceles')
    else:
        print('Triangulo escaleno')

else:
    print(f'Os valores informados: {a, b, c} nao formam um triangulo')