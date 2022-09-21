codigoCidade = int(input("Digite o código da cidade: "))
quantVeiculos = int(input("Digite o número de veículos na cidade: "))
quantAcidentes = int(input("Digite o número de acidentes com vitimas da cidade: "))

indiceAcidente = float(quantAcidentes) / quantVeiculos
maiorIndice = indiceAcidente
menorIndice = indiceAcidente
maiorIndiceCodigo = codigoCidade
menorIndiceCodigo = codigoCidade
soma = quantVeiculos
somaVeiculos2000 = 0
divisorMedia2000 = 0
a = 0

if (quantVeiculos < 2000):
	somaVeiculos2000 = somaVeiculos2000 + quantAcidentes
	divisorMedia2000 = divisorMedia2000 + 1

while (a < 5):
	indiceAcidente = float(quantAcidentes) / quantVeiculos
	soma = soma + quantVeiculos

	if (indiceAcidente > maiorIndice):
		maiorIndice = indiceAcidente
		maiorIndiceCodigo = codigoCidade

	if (indiceAcidente < menorIndice):
		menorIndice = indiceAcidente
		menorIndiceCodigo = codigoCidade

	if (quantVeiculos < 2000):
		somaVeiculos2000 = somaVeiculos2000 + quantAcidentes
		divisorMedia2000 = divisorMedia2000 + 1

	a = a + 1

print("\nMenor índice: %.2f \nCódigo da cidade: %d" % (menorIndice, menorIndiceCodigo))
print("\nMaior índice: %.2f \nCódigo da cidade: %d" % (maiorIndice, maiorIndiceCodigo))
print("Média de veículos nas %d cidades = %d veículos" % (a,(float(soma)/a)))
print("Média de acidentes em cidades com menos de 2000 veículos: %.1f" % (float(somaVeiculos2000)/divisorMedia2000))