candidato_ciro = 0
candidato_lula = 0
candidato_lixo = 0
candidata_loira = 0
voto_nulo = 0
voto_branco = 0
numero_eleitores = int(input("Digite o número de eleitores: "))

for i in range(0,numero_eleitores):
  voto = input("Escolha entre o candidato_ciro(12), candidato_lula(13), candidato_lixo(22), candidata_loira(44), voto_nulo(5), voto_branco(6): ")
  if voto == "12":
    candidato_ciro = candidato_ciro + 1
  elif voto == "13":
    candidato_lula = candidato_lula + 1
  elif voto == "22":
    candidato_lixo = candidato_lixo + 1
  elif voto == "44":
    candidata_loira = candidata_loira + 1
  elif voto == "5":
    voto_nulo = voto_nulo + 1
  elif voto == "6":
    voto_branco = voto_branco + 1

print("Numero de votos do candidato_ciro:", candidato_ciro)
print("Numero de votos do candidato_lula:", candidato_lula)
print("Numero de votos do candidato_lixo:", candidato_lixo)
print("Numero de votos da candidata_loira:", candidata_loira)
print("Numero de votos nulos:", voto_nulo)
print("Numero de votos brancos:", voto_branco)
print("A porcentagem de votos nulos sobre o total de votos:", ((float(voto_nulo)/numero_eleitores)*100),"%")

