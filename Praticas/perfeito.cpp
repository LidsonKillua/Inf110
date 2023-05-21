#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  int n, sdiv = 0;
  
  cin >> n;

  for(int i = 1; i<n; i++){
    if(n % i == 0)
      sdiv += i;
  }
    
  if(n == sdiv)
    cout << "SIM" << endl;
  else
    cout << "NAO" << endl;
}