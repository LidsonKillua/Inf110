#include <bits/stdc++.h>
using namespace std;

int main(){
  int m, n, val, qtd = 0;

  cin >> m >> n;

  int v[m][n];

  for(int i = 0; i < m; i++)
    for(int j = 0; j < n; j++)
      cin >> v[i][j];

  cin >> val;

  for(int i = 0; i < m; i++){
    for(int j = 0; j < n; j++)
      if(v[i][j] == val)
        qtd++;

    cout << qtd << endl;
    qtd = 0;
  }

  return 0;
}
