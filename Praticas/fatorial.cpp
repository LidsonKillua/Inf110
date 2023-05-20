#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  int n;
  long long fat = 1;
  cin >> n;
  
  for(int i = 1; i <= n; i++)
    fat *= i;
  
  cout << fat << endl;
}