#include <iostream>

using namespace std;

int main()
{
    int numero;
    
    cout << "Informe um número: " << endl;
    
    cin >> numero;

    for(int i = 1; i < numero + 1; i++) cout << i;
    
    return 0;
}
