#include<iostream>
#include <string>
using namespace std;
int main()
 {
     string frase;
     char letra;
     
     //print tela 
     cout << "Informe uma frase: " << endl;
     
     //leitura de dados
     getline(cin, frase);
          
     //print tela 
     cout << "Informe uma letra: " << endl;
     
     //leitura de dados
     cin >> letra;
     
     //conta quantidade da letra
     int count = 0;
     for (int i = 0; i < frase.size(); i++)
        if (frase[i] == letra) count ++;
        
     //imprime contagem
     cout << count;
 }