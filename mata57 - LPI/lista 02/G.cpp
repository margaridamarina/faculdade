#include <iostream>
#include <vector>

int main() {
    int N;
    std::cin >> N; 

    std::vector<int> fases(N);
    for (int i = 0; i < N; i++) {
        std::cin >> fases[i]; 
    }

    int M;
    std::cin >> M; 

    int vida = M;
    bool passou = true;

    for (int i = 0; i < N; i++) {
        if (fases[i] >= 2) {
            if (fases[i] > vida) {
                passou = false;
                break;
            }
            vida -= fases[i];
        } else if (fases[i] == 1) {
            vida = M;
        }
    }

    if (passou) {
        std::cout << "Yes, you can" << std::endl;
    } else {
        std::cout << "You Died" << std::endl;
    }

    return 0;
}
