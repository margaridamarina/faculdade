#include <iostream>
using namespace std;

int main() {
    int X, Y;
    cin >> X >> Y;

    if (X > 0 && X < 100 && Y > 0 && Y < 100) {
        if (X > 70 || Y > 70) {
            cout << "Coordenada valida e o navio esta longe" << endl;
        } else {
            cout << "Coordenada valida e o navio esta perto" << endl;
        }
    } else {
        cout << "Coordenada invalida" << endl;
    }

    return 0;
}