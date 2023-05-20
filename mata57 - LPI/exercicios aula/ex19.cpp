#include <iostream>

using namespace std;

float calc_media_altura (float altura1, float altura2, float altura3, float altura4) {
    return (altura1 + altura2 + altura3 + altura4)/4.0;
};

float calc_media_peso (float peso1, float peso2, float peso3, float peso4) {
    return (peso1 + peso2 + peso3 + peso4)/4.0;
};

int main()
{
    float altura1, altura2, altura3, altura4;
    float peso1, peso2, peso3, peso4;

    cout << "Informe as quatro alturas: " << endl;
    cin >> altura1;
    cin >> altura2;
    cin >> altura3;
    cin >> altura4;

    cout << "Informe os quatro pesos: " << endl;
    cin >> peso1;
    cin >> peso2;
    cin >> peso3;
    cin >> peso4;

    cout << "A média de altura é: " << calc_media_altura(altura1, altura2, altura3, altura4) << endl;
    cout << "A média do peso é: " << calc_media_altura(peso1, peso2, peso3, peso4) << endl;

    return 0;
}
