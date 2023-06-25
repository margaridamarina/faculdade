#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> somarMatrizes(const vector<vector<int>>& matriz1, const vector<vector<int>>& matriz2) {
    int linhas = matriz1.size();
    int colunas = matriz1[0].size();
    vector<vector<int>> resultado(linhas, vector<int>(colunas, 0));

    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < colunas; j++) {
            resultado[i][j] = matriz1[i][j] + matriz2[i][j];
        }
    }

    return resultado;
}

int main() {
    int linhas, colunas;

    cin >> linhas;
    cin >> colunas;

    cout << "Matriz A:" << endl;
    vector<vector<int>> matriz1(linhas, vector<int>(colunas, 0));
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < colunas; j++) {
            cin >> matriz1[i][j];
        }
    }

    cout << "Matriz B:" << endl;
    vector<vector<int>> matriz2(linhas, vector<int>(colunas, 0));
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < colunas; j++) {
            cin >> matriz2[i][j];
        }
    }

    vector<vector<int>> resultado = somarMatrizes(matriz1, matriz2);

    cout << "Matriz C:" << endl;
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < colunas; j++) {
            cout << resultado[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
