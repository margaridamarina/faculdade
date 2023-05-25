#include <iostream>
#include <string>
#include <iomanip>

int main() {
    std::string B, b, h;
    std::cin >> B >> b >> h;

    float B_val = std::stof(B);
    float b_val = std::stof(b);
    float h_val = std::stof(h);

    float A = ((B_val + b_val) * h_val) / 2.0;

    std::cout << "A=" << std::fixed << std::setprecision(1) << A << std::endl;

    return 0;
}