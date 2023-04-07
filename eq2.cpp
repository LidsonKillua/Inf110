#include <iostream>
#include <iomanip> 
#include <math.h>
using namespace std;

int main() {
  double a, b, c, x1, x2;
  
  cin >> a >> b >> c;

  x1 = (-b + sqrt(pow(b, 2) - 4 * a * c))/ (2 * a);
  x2 = (-b - sqrt(pow(b, 2) - 4 * a * c))/ (2 * a);

  cout << setprecision(4) << fixed << x1 << " " << x2 << endl;

  return 0;
} 