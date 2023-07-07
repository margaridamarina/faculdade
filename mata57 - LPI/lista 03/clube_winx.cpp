#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int N;
    std::cin >> N;  // quantidade de nomes das alunas

    std::vector<std::string> nomes_alunas(N);
    for (int i = 0; i < N; ++i) {
        std::cin >> nomes_alunas[i];  // lê o nome de cada aluna
    }

    std::sort(nomes_alunas.begin(), nomes_alunas.end());  // ordena os nomes em ordem alfabética

    for (const std::string& nome : nomes_alunas) {
        std::cout << nome << std::endl;  // imprime o nome de cada aluna em ordem alfabética
    }

    return 0;
}
