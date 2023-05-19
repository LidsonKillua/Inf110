#include <bits/stdc++.h>
using namespace std;

int main(){
  int m, n, b, xB, yB, qtdB;

  cin >> m >> n >> b;

  int v[m][n];

  for(int i = 0; i < m; i++){
    for(int j = 0; j < n; j++)
      v[i][j] = 0;
  }

  for(int i = 0; i < b; i++){
    cin >> xB >> yB;
    v[xB][yB] = 10;
  }

  /* Mostrar a matriz
  for(int i = 0; i < m; i++){
    for(int j = 0; j < n; j++)
      cout << v[i][j] << " ";
   cout << endl;
  } */

  for(int i = 0; i < m; i++){
    for(int j = 0; j < n; j++){
      if(v[i][j] == 10)
        cout << 'B';
      else{
        qtdB = 0;

        for(int k = ((i-1 < 0) ? i : i-1); (k <= i+1) && (k < m); k++)
          for(int l = ((j-1 < 0) ? j : j-1); (l <= j+1) && (l < n); j++)
            if(v[k][l] == 10)
              qtdB++;

        if(qtdB > 0)
          cout << qtdB;
        else
          cout << '-';
      }
    }
    cout << endl;
  }

  return 0;
}

