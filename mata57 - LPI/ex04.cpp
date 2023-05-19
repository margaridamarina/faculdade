#include <iostream>

using namespace std;

int main() {
    double preco;
    int origem;
    
    //print em tela
    cout << "Informe o preço e o código de origem do produto (1, 2, 3 ou 4):" << endl;
    
    //leitura de dados
    cin >> preco;
    cin >> origem;
    
    //imprime preço
    printf("%.2f", preco); 
    
    //cases
    switch (origem) {
        case 1:
            cout << " Sul!";
            break;
        case 2:
            cout << " Norte!";
            break;
        case 3:
            cout << " Nordeste!";
            break;
        case 4:
            cout << " Centro-Oeste!";
            break;
        default: 
            cout << " Produto importado!";
    }
}
