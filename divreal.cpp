#include <iostream>
#include <iomanip> 
using namespace std;

int main() {
  double num1, num2, div;
  
  cin >> num1 >> num2;

  div = num1 / num2;

  cout << setprecision(2) << fixed << div << endl;

  return 0;
}