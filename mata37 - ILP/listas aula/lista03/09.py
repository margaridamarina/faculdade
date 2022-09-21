comeco = 0
final = 0
tabuada = 0

tabuada = int(input("Digite a tabuada que deseja: "))
comeco = int(input("Digite por qual número deseja começar: "))
final = int(input("Digite por qual número deseja finalizar: "))

while (comeco > final):
		print("O valor inicial não pode ser maior que o final!\n")

while (comeco < (final + 1)):
	print(tabuada, "X", comeco, "=", tabuada * comeco)
	comeco = comeco + 1