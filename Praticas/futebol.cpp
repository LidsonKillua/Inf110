#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  int n, iM, l, iJ, qtd = 0;
  cin >> n >> iM >> l;
  
  for(int i = 0; i < n; i++){
    cin >> iJ;

    if(iJ >= iM)
      qtd++;
  }
  
  cout << ((qtd > l) ? "Nao aceito." : "Aceito.") << endl;
}