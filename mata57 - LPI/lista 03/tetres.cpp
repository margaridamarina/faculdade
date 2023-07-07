#include <iostream>
#include <vector>
#include <algorithm>

// Função para verificar se dois blocos são perfeitos
bool perfeitos(const std::string& bloco1, const std::string& bloco2) {
    int n = bloco1.size();
    for (int i = 0; i < n; ++i) {
        if (bloco1[i] == bloco2[i]) {
            return false;
        }
    }
    return true;
}

int main() {
    int N, M;
    std::cin >> N >> M;  // número de blocos e altura máxima da torre

    std::vector<std::string> blocos(N);
    for (int i = 0; i < N; ++i) {
        std::cin >> blocos[i];  // identificadores dos blocos
    }

    int pontuacao = 0;
    std::vector<std::string> torre;

    for (int i = 0; i < N; ++i) {
        std::string atual = blocos[i];

        bool perfeito = false;
        int h = torre.size();
        if (h > 0) {
            std::string topo = torre[h - 1];
            if (perfeitos(topo, atual)) {
                torre.pop_back();
                pontuacao += 10;
                perfeito = true;
            }
        }

        if (!perfeito) {
            torre.push_back(atual);
        }

        if (torre.size() > M) {
            std::cout << "game over" << std::endl;
            return 0;
        }
    }

    std::cout << pontuacao << std::endl;

    return 0;
}
