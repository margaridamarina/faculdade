#include <iostream>

using namespace std;

float calc_media (float nota1, float nota2, float nota3, float nota4) {
    return (nota1 + nota2 + nota3 + nota4)/4.0;
};

int main()
{
    float nota1, nota2, nota3, nota4;
    cout << "Informe as quatro notas: " << endl;
    cin >> nota1;
    cin >> nota2;
    cin >> nota3;
    cin >> nota4;
    cout << "A média é: " << calc_media(nota1, nota2, nota3, nota4);
    return 0;
}
