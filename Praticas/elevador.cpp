#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  int qtd, c, sai, ent, nP = 0;
  bool exc = false;
  
  cin >> qtd >> c;

  for(int i = 1; i <= qtd; i++){
    cin >> sai >> ent;
    
    nP += ent - sai;
    if(nP > c)
      exc = true;
  }

  cout << (exc ? 'S' : 'N') << endl;
}