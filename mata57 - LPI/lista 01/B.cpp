#include <iostream>
#include <string>

int main() {
    std::string A, B, C, D, E;
    std::cin >> A >> B >> C >> D >> E;

    int a = std::stoi(A);
    int b = std::stoi(B);
    int c = std::stoi(C);
    int d = std::stoi(D);
    int e = std::stoi(E);

    int result = a - (b + c + d + e);
    std::cout << result << std::endl;

    return 0;
}