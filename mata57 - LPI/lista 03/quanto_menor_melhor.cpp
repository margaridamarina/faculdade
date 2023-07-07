#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

// Função para verificar o tamanho de uma palavra
int tamanho(const std::string& palavra) {
    return palavra.size();
}

// Função para reorganizar a frase no "Formiguês"
std::string traduzir(const std::string& frase) {
    std::istringstream iss(frase);
    std::vector<std::string> palavras;
    std::string palavra;

    // Quebra a frase em palavras
    while (iss >> palavra) {
        palavras.push_back(palavra);
    }

    // Ordena as palavras de acordo com as regras do "Formiguês"
    std::sort(palavras.begin(), palavras.end(), [](const std::string& a, const std::string& b) {
        if (tamanho(a) == tamanho(b)) {
            return a < b;
        } else {
            return tamanho(a) < tamanho(b);
        }
    });

    // Constrói a frase reorganizada
    std::ostringstream oss;
    for (const std::string& palavra : palavras) {
        oss << palavra << " ";
    }

    return oss.str();
}

int main() {
    std::string frase;
    std::getline(std::cin, frase);

    std::string fraseTraduzida = traduzir(frase);
    std::cout << fraseTraduzida << std::endl;

    return 0;
}
