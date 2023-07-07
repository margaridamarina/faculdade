#include <iostream>
#include <vector>

int main() {
    int N;
    std::cin >> N;  // quantidade de utilitários

    std::vector<int> utilitarios_usados(N);
    for (int i = 0; i < N; ++i) {
        std::cin >> utilitarios_usados[i];  // lista de utilitários usados
    }

    std::vector<int> utilitarios_acertados(N);
    for (int i = 0; i < N; ++i) {
        std::cin >> utilitarios_acertados[i];  // lista de utilitários acertados
    }

    std::vector<int> porcentagens_acerto(N);
    for (int i = 0; i < N; ++i) {
        if (utilitarios_usados[i] == 0) {
            porcentagens_acerto[i] = 0;
        } else {
            double porcentagem = (static_cast<double>(utilitarios_acertados[i]) / utilitarios_usados[i]) * 100;
            porcentagens_acerto[i] = static_cast<int>(porcentagem);
        }
    }

    for (int i = 0; i < N; ++i) {
        std::cout << porcentagens_acerto[i];
        if (i != N - 1) {
            std::cout << " ";
        }
    }
    std::cout << std::endl;

    return 0;
}
