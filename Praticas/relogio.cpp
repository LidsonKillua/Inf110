#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  int r, fA, cO;
  
  cin >> r >> fA >> cO;
  
  if((fA > 3 * r) || cO < 95)
    cout << "diminuir" << endl;
  else if ((fA < 2 * r) && cO > 97)
    cout << "aumentar" << endl;
  else 
    cout << "manter" << endl;
}