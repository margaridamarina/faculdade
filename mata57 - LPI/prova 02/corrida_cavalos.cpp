#include <iostream>
#include <vector>

int main() {
    int qtd_corridas;
    std::cin >> qtd_corridas;  // quantidade de corridas

    for (int i = 0; i < qtd_corridas; ++i) {
        int qtd_cavalos;
        std::cin >> qtd_cavalos;  // quantidade de cavalos

        std::vector<int> cavalos(qtd_cavalos);
        for (int j = 0; j < qtd_cavalos; ++j) {
            std::cin >> cavalos[j];  // lista de cavalos
        }

        int cavalo_procurado;
        std::cin >> cavalo_procurado;  // cavalo que deve ser encontrado

        int posicao = 0;
        for (int j = 0; j < qtd_cavalos; ++j) {
            if (cavalos[j] == cavalo_procurado) {
                posicao = j;
                break;
            }
        }

        std::cout << posicao << std::endl;
    }

    return 0;
}
