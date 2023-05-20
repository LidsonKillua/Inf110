#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  int n, nf;
  double a;

  cin >> n >> nf;
  
  for(int i = n; i <= nf; i++){
    a = (180.0 *(i-2)) / i;
    cout << fixed << setprecision(1) << a << endl;
  }
}