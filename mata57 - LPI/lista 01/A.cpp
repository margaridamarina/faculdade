#include <iostream>
#include <string>

int main() {
    std::string a = "#";
    std::string b = ">";

    int P;
    std::cin >> P;

    int j = 1;

    for (int k = P - 1; k >= 0; k--) {
        std::string line = std::string(k, b[0]) + std::string(j, a[0]);
        std::cout << line << std::endl;
        j = j + 1;
    }

    return 0;
}