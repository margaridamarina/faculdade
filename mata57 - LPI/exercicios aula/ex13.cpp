#include<iostream>
#include <string>
#include <vector>
using namespace std;
int main()
 {
     string frase;
     char letras_acentuadas[] = "áéíóúâêôã";
     char letras_nao_acentuadas[] = "aeiouaeoa";

     //print tela 
     cout << "Informe uma frase: " << endl;
     
     //leitura de dados
     getline(cin, frase);
     
     //verifica se tem a letra e substitui
     for (int i = 0; i < frase.size(); i++)
        for (int j = 0; j < frase.size(); j++){
            if (frase[i] == letras_acentuadas[j]) frase[i] == letras_nao_acentuadas[j];
        }
    
     //imprime frase
     cout << frase;
 }