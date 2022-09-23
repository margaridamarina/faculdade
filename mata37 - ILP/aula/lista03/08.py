candidato_ciro = 0
candidato_lula = 0
candidato_lixo = 0
numero_eleitores = int(input("Digite o número de eleitores: "))

for i in range(0,numero_eleitores):
  voto = input("Escolha entre o candidato_ciro(12), candidato_lula(13), candidato_lixo(22): ")
  if voto == "12":
    candidato_ciro = candidato_ciro + 1
  elif voto == "13":
    candidato_lula = candidato_lula + 1
  elif voto == "22":
    candidato_lixo = candidato_lixo + 1
  else:
    print("voto nulo.")

print("Numero de votos do candidato_ciro:", candidato_ciro)
print("Numero de votos do candidato_lula:", candidato_lula)
print("Numero de votos do candidato_lixo:", candidato_lixo)
