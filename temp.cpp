#include <iostream>
#include <iomanip> 
#include <math.h>
using namespace std;

int main() {
  double temp, tempconv;
  char escala, escalaconv;
  
  cin >> temp >> escala;

  if (escala == 'F') {
    tempconv = 5.0 / 9.0 * (temp - 32);
    escalaconv = 'C';
  } 
  else {
    tempconv = temp * 1.8 + 32; 
    escalaconv = 'F';
  }
  

  cout << setprecision(1) << fixed << tempconv;
  cout << ' ' << escalaconv << endl;

  return 0;
}