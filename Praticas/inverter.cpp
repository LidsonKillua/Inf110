#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  int n, v, x, cont = 0;
  
  cin >> n;
  int l[n];
  
  for(int i = 0; i < n ;i++){
    cin >> v;
    l[i] = v;
  } 

  for(int i = n - 1; i >= 0 ;i--)
    cout << l[i] << ((i != 0) ? " " : "\n");
  
}