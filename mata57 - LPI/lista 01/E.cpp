#include <iostream>
#include <string>

int main() {
    std::string E, T;
    std::cin >> E >> T;

    int V = std::stoi(E) / std::stoi(T);

    std::cout << V << std::endl;

    return 0;
}