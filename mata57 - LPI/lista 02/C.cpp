#include <iostream>
#include <vector>
#include <string>

int main() {
    std::vector<int> notas;
    std::string input;

    while (true) {
        std::cin >> input;

        if (input == "FIM") {
            // Fim da turma, calcular média e reiniciar para próxima turma
            int ki = notas.size();
            if (ki == 0) {
                break;  // Fim da entrada dos dados
            }

            int soma = 0;
            int nmaxi = notas[0];
            int nmini = notas[0];

            for (int i = 0; i < ki; i++) {
                soma += notas[i];

                if (notas[i] > nmaxi) {
                    nmaxi = notas[i];
                }

                if (notas[i] < nmini) {
                    nmini = notas[i];
                }
            }

            int media = 0;
            if (ki > 2) {
                media = (soma - nmaxi - nmini) / (ki - 2);
            } else if (ki == 2) {
                media = soma / ki;
            } else if (ki == 1) {
                media = notas[0];
            }

            std::cout << media << std::endl;

            notas.clear();  // Reiniciar para próxima turma
        } else {
            // Adicionar nota à turma atual
            int nota = std::stoi(input);
            notas.push_back(nota);
        }
    }

    return 0;
}
