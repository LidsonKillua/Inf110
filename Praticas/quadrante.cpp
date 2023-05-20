#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  //cin.tie(0);
  //ios_base::sync_with_stdio(0);

  int x, y;
  cin >> x >> y;

  if(x == 0 && y == 0)
    cout << "ORIGEM";
  else if(x == 0)
    cout << "EIXO Y";
  else if(y == 0)
    cout << "EIXO X";
  else 
    cout << "QUADRANTE " << ((x > 0 && y > 0) ? 1 : 
                            ((x < 0 && y > 0) ? 2 : 
                            ((x < 0 && y < 0) ? 3 : 4)));   

  cout << endl;

  return 0;
}