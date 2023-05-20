#include <iostream>

using namespace std;

int main() {
    float nota1, nota2, nota3, nota4, soma, media;
    
    //print em tela
    cout << "Informe as quatro notas entre 0 e 10:" << endl;
    
    //leitura de dados
    cin >> nota1;
    cin >> nota2;
    cin >> nota3;
    cin >> nota4;
    
    //calcular a soma
    soma = nota1 + nota2 + nota3 + nota4;
    
    //calcular a media
    media = soma / 4;
        
    //print da resposta
    cout << "A média foi " << media << "!" << endl;
    
    if (media >= 7.0) cout << "Aluno aprovado! Parabéns!" << endl;
    else {
        cout << "Aluno reprovado! Estude mais!" << endl;
    }
}
