#include <iostream>

using namespace std;

int main() {
    float peso, altura, imc;
    
    //print em tela
    cout << "Informe seu peso e altura: " << endl;
    
    //leitura de dados
    cin >> peso;
    cin >> altura;
    
    //calcular imc
    imc = peso / (altura * altura);
    
    //print em tela
    cout << "Seu IMC é: " << imc << endl;
    
    //regras
    if (imc < 18.5)
        cout << "Baixo peso e baixo risco de comorbidades";
    else if (18.5 <= imc <= 24.9)
        cout << "Peso normal e médio risco de comorbidades";
    else if (25 <= imc <= 29.9)
        cout << "Pré-obeso e aumentado risco de comorbidades";
    else if (30 <= imc <= 34.9) 
        cout << "Obeso I e moderado risco de comorbidades";
    else if (35 <= imc <= 39.9) 
        cout << "Obeso II e grave risco de comorbidades";
    else cout << "Obeso III e muito grave risco de comorbidades";
}
 