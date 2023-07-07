#include <iostream>
#include <vector>

int main() {
    int N;
    std::cin >> N; // Número de pontos recebidos

    std::vector<int> pontos(N);
    for (int i = 0; i < N; i++) {
        std::cin >> pontos[i]; // Valores dos pontos recebidos
    }

    int somaPares = 0;
    int somaImpares = 0;

    for (int i = 0; i < N; i++) {
        if (i % 2 == 0) {
            somaPares += pontos[i]; // Soma dos valores nas posições pares
        } else {
            somaImpares += pontos[i]; // Soma dos valores nas posições ímpares
        }
    }

    if (somaPares > somaImpares) {
        std::cout << "Vou ajudar" << std::endl;
    } else {
        std::cout << "Modo Hard" << std::endl;
    }

    return 0;
}
