#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  int a, b;
  cin >> a >> b;
  
  for(int i = (a < b) ? b : a; ;i++)
    if((i % a == 0) && (i % b == 0)){
      cout << i << endl;
      break;
    }
}