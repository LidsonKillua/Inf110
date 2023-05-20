#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  //ios_base::sync_with_stdio(0);

  int n1, n2, n3;
  cin >> n1 >> n2 >> n3;

  cout << max(n1, max(n2, n3)) << endl;
}