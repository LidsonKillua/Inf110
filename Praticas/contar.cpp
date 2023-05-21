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

  cin >> x;
  
  for(int i = 0; i < n ;i++){
    if(l[i] >= x)
      cont++;
  } 

  cout << cont << endl;
}