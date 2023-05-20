#include <iostream>

using namespace std;

float calc_media (float preco1, float preco2, float preco3, float preco4) {
    return (preco1 + preco2 + preco3 + preco4)/4.0;
};

int main()
{
    float preco1, preco2, preco3, preco4;
    cout << "Informe os quatro precos: " << endl;
    cin >> preco1;
    cin >> preco2;
    cin >> preco3;
    cin >> preco4;
    cout << "A média é R$ " << calc_media(preco1, preco2, preco3, preco4);
    return 0;
}
