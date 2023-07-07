#include <iostream>
#include <vector>

int main() {
    int X;
    std::cin >> X; // Quantidade de partes diferentes adquiridas

    std::vector<int> partes(X);
    for (int i = 0; i < X; i++) {
        std::cin >> partes[i]; // Quantidade adquirida de cada parte
    }

    int Y;
    std::cin >> Y; // Número sorteado para a multiplicação

    for (int i = 0; i < X; i++) {
        partes[i] *= Y; // Multiplica a quantidade de cada parte pelo número sorteado
    }

    // Imprime a quantidade recebida de cada parte após a multiplicação
    for (int i = 0; i < X; i++) {
        std::cout << partes[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
