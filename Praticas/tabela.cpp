#include <bits/stdc++.h>
using namespace std;

int main(){
  int m, n;

  cin >> m >> n;

  int v[m][n];

  for(int i = 0; i < m; i++)
    for(int j = 0; j < n; j++)
      cin >> v[i][j];

  for(int j = 0; j < n; j++)
    for(int i = 0; i < m; i++)
      cout << v[i][j] << (i < m-1 ? " " : "\n");

  return 0;
}
