#include <iostream>
#include <iomanip> 
#include <math.h>
using namespace std;

int main() {
  int diam, a, l, p;
  char resposta;
  
  cin >> diam;
  cin >> a >> l >> p;

  if (a >= diam && l >= diam && p >= diam) {
    resposta = 'S';
  }
  else {
    resposta = 'N';
  }

  cout << resposta << endl;

  return 0;
}