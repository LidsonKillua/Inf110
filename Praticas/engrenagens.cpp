#include <iostream>
#include <iomanip> 
#include <math.h>
using namespace std;

int main() {
  int d1, d2;
  bool resposta;
  
  cin >> d1 >> d2;

  if (d1 == 0) {
    resposta = 0;
  } 
  else if (d2 % d1 == 0) {
    resposta = 1;
  } 
  else {
    resposta = 0;
  }

  cout << resposta << endl;

  return 0;
}