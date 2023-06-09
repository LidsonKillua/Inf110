#include <iostream>
#include <iomanip> 
#include <math.h>
using namespace std;

int main() {
  double a, b, c, delta, x1, x2;
  
  cin >> a >> b >> c;

  delta = pow(b, 2) - 4 * a * c;
  
  if (delta < 0) {
    cout << "Nao ha raiz real" << endl;
  } 
  else if (delta == 0) {
    x1 = -b / (2 * a);
    cout << setprecision(2) << fixed << x1 << endl;
  }
  else {
    x1 = (-b - sqrt(delta))/ (2 * a);
    x2 = (-b + sqrt(delta))/ (2 * a);

    cout << setprecision(2) << fixed << x1 << " " << x2 << endl;
  }

  return 0;
}