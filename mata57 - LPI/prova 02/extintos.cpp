#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

bool buscaBinaria(const vector<string>& catalogo, const string& especie) {
    int esq = 0;
    int dir = catalogo.size() - 1;

    while (esq <= dir) {
        int meio = esq + (dir - esq) / 2;

        if (catalogo[meio] == especie) {
            return true;  // Espécie encontrada no catálogo
        } else if (catalogo[meio] < especie) {
            esq = meio + 1;  // A espécie pode estar à direita
        } else {
            dir = meio - 1;  // A espécie pode estar à esquerda
        }
    }

    return false;  // Espécie não encontrada no catálogo
}

int main() {
    int N, Q;
    cin >> N;

    vector<string> catalogo(N);
    for (int i = 0; i < N; i++) {
        cin >> catalogo[i];
    }

    cin >> Q;

    sort(catalogo.begin(), catalogo.end());  // Ordena o catálogo lexicograficamente

    for (int i = 0; i < Q; i++) {
        string especie;
        cin >> especie;

        bool exists = buscaBinaria(catalogo, especie);
        if (exists) {
            cout << especie << " vive!" << endl;
        } else {
            cout << especie << " foi extinto :(" << endl;
        }
    }

    return 0;
}
