qtd_doces=int(input())

from collections import OrderedDict

pessoas = OrderedDict()
pessoas["Chapeuzinho Vermelho"] = 0
pessoas["Vovozinha"] = 0
pessoas["Lobo Mau"] = 0

while qtd_doces > 0:
    for (nome, doces) in pessoas.items():
        if qtd_doces > 0:
            qtd_doces = qtd_doces - 1
            pessoas[nome] = pessoas[nome] + 1

for (x, y) in pessoas.items():
    print(x, y)


# print(
#     "Chapeuzinho Vermelho {}\nVovozinha {}\nLobo Mau {}".format(
#         pessoas["Chapeuzinho Vermelho"], pessoas["Vovozinha"], pessoas["Lobo Mau"]
#     )
# )
