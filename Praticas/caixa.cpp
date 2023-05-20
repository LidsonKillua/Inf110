#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  int x;
  cin >> x;

  for(int i = 1; i <= x; i++)
    for(int j = i; j <= x; j++)
      if(i * j == x)
        cout << i << " x " << j << endl;  
}