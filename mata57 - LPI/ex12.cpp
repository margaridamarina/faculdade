#include<iostream>
#include <string>
using namespace std;
int main()
 {
     string frase;
     int esq, dir;

     //print tela 
     cout << "Informe uma frase: " << endl;
     
     //leitura de dados
     getline(cin, frase);
     
     //mostra frase inversa
     for (int i = frase.size(); i >= 0; i--)
        cout << frase[i];
        
     //checa se é palíndromo
     esq = 0;
     dir = frase.size() -1;
     
     while(esq < dir) {
         if (frase[esq] == frase[dir]) {
             cout << "\n É um palíndomo" << endl;
             return 0; //sai do programa
         }
         esq++;
         dir--;
     }
     cout << "Não é um palíndromo!" << endl;
 }