#include <iostream>
#include <iomanip> 
#include <math.h>
using namespace std;

int main() {
  int dia, mes;
  string resposta;
  
  cin >> dia >> mes;

  if (dia < 20 && mes <= 3 || mes < 3) {
    resposta = "antes";
  }
  else if (dia == 20 && mes == 3) {
    resposta = "no dia";
  }
  else {
    resposta = "depois";
  }

  cout << resposta << endl;

  return 0;
}