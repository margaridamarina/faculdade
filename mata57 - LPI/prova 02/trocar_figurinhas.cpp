#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int total_figurinhas;
    std::cin >> total_figurinhas; // ignore

    std::vector<int> colecao_figurinhas(total_figurinhas);
    for (int i = 0; i < total_figurinhas; ++i) {
        std::cin >> colecao_figurinhas[i];
    }

    std::vector<int> qtd_figurinhas(total_figurinhas);
    for (int i = 0; i < total_figurinhas; ++i) {
        std::cin >> qtd_figurinhas[i];
    }

    int consultas;
    std::cin >> consultas; // ignore

    std::vector<int> lista_de_troca_de_figurinha(consultas);
    for (int i = 0; i < consultas; ++i) {
        std::cin >> lista_de_troca_de_figurinha[i];
    }

    int tamanho_colecao_figurinha = colecao_figurinhas.size();
    for (int figurinha : lista_de_troca_de_figurinha) {
        int esq = 0;
        int dir = tamanho_colecao_figurinha - 1;
        int posicao = -1;

        while (esq <= dir) {
            int meio = (esq + dir) / 2;

            if (figurinha == colecao_figurinhas[meio]) {
                posicao = meio;
                break;
            } else if (figurinha < colecao_figurinhas[meio]) {
                dir = meio - 1;
            } else {
                esq = meio + 1;
            }
        }

        if (posicao == -1) {
            std::cout << "Quero" << std::endl;
        } else if (qtd_figurinhas[posicao] > 1) {
            std::cout << "Trocar" << std::endl;
        } else {
            std::cout << "Apenas uma" << std::endl;
        }
    }

    return 0;
}
