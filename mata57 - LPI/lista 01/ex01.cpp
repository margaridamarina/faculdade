#include <iostream>

using namespace std;

int main() {
  char a = '#';
  char b = '>';
  int j = 1;
  char value;

  int P;
  
  value = ((i*b)+(j*a));
  
  for(int i = P; i >= 1; i--) {
      cout << value;
      j=j+1;
  }
  
  return 0;
}


#include <iostream>

using namespace std;

int main() {
  char a = '#';
  char b = '>';
  int j = 1;
  char value;
  int i;
  int P;
  
  
  cout << "Informe a altura da pirâmide: ";
  cin >> P;
 
  
  for(int i = P - 1; i >= -1; --i) {
      cout << i * b << j * a << endl;
      j=j+1;
  }
  
  return 0;
}
