#include <iostream>
#include <iomanip> 
#include <math.h>
using namespace std;

int main() {
  double raio, altura, volume;
  
  cin >> raio >> altura;

  volume = 3.1415 * pow(raio, 2) * altura;

  cout << setprecision(2) << fixed << volume << endl;

  return 0;
}