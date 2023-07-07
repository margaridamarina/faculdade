#include <iostream>

int main() {
    int P;
    std::cin >> P;

    if (P % 42 == 0) {
        std::cout << "Sim" << std::endl;
    } else {
        std::cout << "Nao" << std::endl;
    }

    return 0;
}
