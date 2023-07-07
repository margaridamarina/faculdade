#include <iostream>

bool numero_primo(int n) {
    if (n < 2) {
        return false;
    }
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int N;
    while (true) {
        std::cin >> N;
        if (N == 0) {
            break;
        }
        if (numero_primo(N)) {
            std::cout << "O numero de cadeiras eh primo!" << std::endl;
        } else {
            std::cout << "O numero de cadeiras nao eh primo!" << std::endl;
        }
    }
    return 0;
}
