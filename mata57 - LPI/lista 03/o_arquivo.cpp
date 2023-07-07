#include <iostream>
#include <unordered_map>

int main() {
    int L;
    std::cin >> L;  // quantidade de livros no Arquivo

    std::unordered_map<std::string, int> acervo;  // mapa para armazenar o acervo de livros
    for (int i = 0; i < L; ++i) {
        std::string codigo;
        int disponibilidade;
        std::cin >> codigo >> disponibilidade;  // código do livro e disponibilidade
        acervo[codigo] = disponibilidade;  // adiciona o livro ao acervo
    }

    int A;
    std::cin >> A;  // quantidade de livros requisitados pelos arcanistas

    for (int i = 0; i < A; ++i) {
        std::string codigo;
        std::cin >> codigo;  // código do livro requisitado

        if (acervo.find(codigo) != acervo.end()) {
            if (acervo[codigo] == 1) {
                std::cout << "Disponivel" << std::endl;
            } else {
                std::cout << "Emprestado" << std::endl;
            }
        } else {
            std::cout << "Nao encontrado" << std::endl;
        }
    }

    return 0;
}
