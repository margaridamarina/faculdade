#include <iostream>
using namespace std;

string calculoPontos(int pontos) {
    if (pontos >= 250)
        return "S+";
    else if (pontos >= 200)
        return "S";
    else if (pontos >= 180)
        return "S-";
    else if (pontos >= 150)
        return "A+";
    else if (pontos >= 100)
        return "A";
    else if (pontos >= 80)
        return "A-";
    else if (pontos >= 60)
        return "B+";
    else if (pontos >= 40)
        return "B";
    else
        return "B-";
}

int main() {
    int N1, N2, N3, N4, N5, N6;
    cin >> N1 >> N2 >> N3 >> N4 >> N5 >> N6;

    int pontos = N1 + N2 + N3 + N4 + N5 + N6;

    string nota = calculoPontos(pontos);

    cout << nota << endl;

    return 0;
}