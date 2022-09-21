gabarito = ' '
gabarito2 = ' '
count = total = count2 = maior = menor = 0
for e in range(1,11):
    gabarito = input(f"{e} - Digite o gabarito das notas: ").strip().upper()[0]
    gabarito2 += (gabarito)

print("-="*30)
continuar = ' '
while continuar not in 'N':
    for c in range(1,11):
        resposta = input(f"{c} - Resposta da questao: ").strip().upper()[0]
        if c == 1:
            if resposta == gabarito2[0]:
                count+=1
        if c == 2:
            if resposta == gabarito2[1]:
                count +=1
        if c == 3:
            if resposta == gabarito2[2]:
                count +=1
        if c == 4:
            if resposta == gabarito2[3]:
                count+=1
        if c == 5:
            if resposta == gabarito2[4]:
                count+=1
        if c == 6:
            if resposta == gabarito2[5]:
                count+=1
        if c == 7:
            if resposta == gabarito2[6]:
                count+=1
        if c == 8:
            if resposta == gabarito2[7]:
                count +=1
        if c == 9:
            if resposta == gabarito2[8]:
                count+=1
        if c == 10:
            if resposta == gabarito2[9]:
                count+=1
            print("-="*30)
            continuar = input("Quer continuar [N] para sair ").strip().upper()[0]

            total+=1
        if count > maior:
            maior = count
        if count < menor or count == 1:
            menor = count

print("-="*30)
print("Gabarito das respostas")
for d in gabarito2:
    count2+=1
    print(f"{count2} - {d}")
print("-="*30)

print(f"Total de acertos: {count}")
print(f"Pontos recebidos: {count}")
print(f"Maior acerto {maior}")
print(f"Menor acerto: {menor}")
print(f"Total de alunos a utilizar o sistema: {total}")