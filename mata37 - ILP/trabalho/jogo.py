# O usuário informa a quantidade de vidas V
# O usuário informa uma lista de palavras V
# O game seleciona uma palavra randomicamente da lista V
# O game mostra a palavra escolhida de forma criptografada. Ex: AMOR V
# - - -
# O usuário informa uma letra V
# Se a letra estiver na palavra, o game mostra a letra na palavra. a - - - V
# Se a letra não estiver na palavra, o usuário perde uma vida e o game informa que a letra não faz parte da palavra V

# O jogo termina se o usuário não tiver mais vidas ou ele acertou a palavra V
# Nos dois casos, o sistema deve informa-lo. V

import random
from collections import Counter

qtd_palavras = int(input("Quantas palavras você quer acrescentar à lista de palavras? "))
lista_palavras = []
while len(lista_palavras) < qtd_palavras:
    x = str(input("Escreva uma palavra: "))
    if x in lista_palavras:
        print("Essa palavra já foi escolhida: ")
    else:
        lista_palavras.append(x)
print(lista_palavras)
palavra_secreta = random.choice(lista_palavras)
print(palavra_secreta)       
  
def jogo():
    print('Adivinhe a palavra!')
    vidas = int(input("Quantas vidas você quer ter no jogo? "))
      
    for letra in palavra_secreta:
        print('_', end = ' ')        
    print()
  
    letra_escolhida = ''                
    chances = len(palavra_secreta) + vidas - 1
    acertou = 0
    status = 0

    while (chances != 0) and status == 0: 
        print()
        chances -= 1

        chute = str(input('Digite uma letra: '))

        if chute in palavra_secreta:
            k = palavra_secreta.count(chute) 
            for _ in range(k):    
                letra_escolhida += chute 
        else:
            print('A letra não faz parte da palavra!')

        for letra in palavra_secreta:
            if letra in letra_escolhida and (Counter(letra_escolhida) != Counter(palavra_secreta)):
                print(letra, end = ' ')
                acertou += 1
            elif (Counter(letra_escolhida) == Counter(palavra_secreta)): 
                print("A palavra era: ", end=' ')
                print(palavra_secreta)
                flag = 1
                print('Você ganhou!')
                break 
            else:
                print('_', end = ' ')
        
    if chances <= 0 and (Counter(letra_escolhida) != Counter(palavra_secreta)):
        print()
        print('Você perdeu!')
        print('A palavra era {}'.format(palavra_secreta))

jogo()