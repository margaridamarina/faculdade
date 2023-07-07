#include <iostream>
#include <vector>

using namespace std;

int main() {
    int F, C;
    cin >> F >> C;

    vector<vector<int>> cinema(F, vector<int>(C));

    for (int i = 0; i < F; i++) {
        for (int j = 0; j < C; j++) {
            cin >> cinema[i][j];
        }
    }

    int fila = -1;
    int assento = -1;

    for (int i = 0; i < F; i++) {
        for (int j = 0; j < C - 1; j++) {
            if (cinema[i][j] == 0 && cinema[i][j + 1] == 0) {
                fila = i + 1;
                assento = j + 1;
                break;
            }
        }
        if (fila != -1) {
            break;
        }
    }

    cout << "Fileira: " << fila << endl;
    cout << "Assentos: " << assento << " e " << assento + 1 << endl;

    return 0;
}
