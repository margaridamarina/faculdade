#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, P;
    cin >> N >> P;

    vector<int> ocupados(P);
    for (int i = 0; i < P; i++) {
        cin >> ocupados[i];
    }

    vector<int> vazios;
    for (int i = 1; i <= N; i++) {
        if (find(ocupados.begin(), ocupados.end(), i) == ocupados.end()) {
            vazios.push_back(i);
        }
    }

    for (int i = 0; i < vazios.size(); i++) {
        cout << vazios[i] << " ";
    }
    cout << endl;

    return 0;
}