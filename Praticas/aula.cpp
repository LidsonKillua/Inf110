#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  int n, v, aE = 0, eE = 0;
  
  cin >> n;

  for(int i = 0; i<n ; i++){
    cin >> v;
    if(v < 50)
      aE++;
    else if(v < 85)
      eE++;
  }
    
  cout << aE << " " << eE << endl;
}