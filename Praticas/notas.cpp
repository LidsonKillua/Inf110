#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  int qtd;
  double n, tn = 0;
  cin >> qtd;

  for(int i = 0; i<qtd; i++){
    cin >> n;
    tn += n;
  }

  cout << fixed << setprecision(2) << tn/qtd << endl;
}