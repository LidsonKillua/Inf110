#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  int xP, yP, n, xM, yM, dM = 0, totD = 0, qtd10 = 0;

  cin >> xP >> yP >> n;

  for(int i = 0; i < n; i++){
    cin >> xM >> yM;
    dM = ((xP < xM) ? xM - xP : xP - xM) +
         ((yP < yM) ? yM - yP : yP - yM);
    
    totD += dM;

    if(dM < 10)
      qtd10++;
  }
    
  cout << fixed << setprecision(1) << 1.0 * totD/n << " " << qtd10 << endl;

}