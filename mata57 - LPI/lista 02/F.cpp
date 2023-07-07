#include <iostream>

int main() {
    int N, XP;
    std::cin >> N >> XP; // Quantidade de missões e XP ganho por missão

    int XP_Yoda, XP_Luke, XP_Ahsoka;
    std::cin >> XP_Yoda >> XP_Luke >> XP_Ahsoka; // Níveis iniciais de XP

    XP_Yoda += N * XP;
    XP_Luke += N * XP;
    XP_Ahsoka += N * XP;

    std::cout << "Yoda " << XP_Yoda << std::endl;
    std::cout << "Luke " << XP_Luke << std::endl;
    std::cout << "Ahsoka " << XP_Ahsoka << std::endl;

    return 0;
}
