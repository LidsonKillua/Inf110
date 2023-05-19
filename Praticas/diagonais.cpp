#include <bits/stdc++.h>
using namespace std;

int main(){
  int n;

  cin >> n;

  int v[n][n];

  for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++)
      cin >> v[i][j];

  for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++)
      if(i == j)
        cout << v[i][j] << endl;

  cout << endl;


  for(int i = 0, j = n-1; (i < n) && (j >= 0) ; i++){
    cout << v[i][j] << endl;
    j--;
  }

  return 0;
}
