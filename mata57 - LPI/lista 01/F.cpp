#include <iostream>
#include <string>

int main() {
    std::string A, B, C;
    std::cin >> A >> B >> C;

    int a = std::stoi(A);
    int b = std::stoi(B);
    int c = std::stoi(C);

    if (a == b && b == c) {
        std::cout << "Empate" << std::endl;
    } else {
        if (a == b) {
            std::cout << "C" << std::endl;
        } else {
            if (a == c) {
                std::cout << "B" << std::endl;
            } else {
                std::cout << "A" << std::endl;
            }
        }
    }

    return 0;
}