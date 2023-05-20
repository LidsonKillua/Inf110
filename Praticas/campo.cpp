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
    v[xB-1][yB-1] = 10;
  }

  /* Mostrar a matriz
  for(int i = 0; i < m; i++){
    for(int j = 0; j < n; j++)
      cout << v[i][j] << " ";
   cout << endl;
  } */

  for(int i = 0; i < m; i++){
    for(int j = 0; j < n; j++){
      if(v[i][j] != 10){
        qtdB = 0;

        for(int k = ((i-1 < 0) ? i : i-1); (k <= i+1) && (k < m); k++)
          for(int l = ((j-1 < 0) ? j : j-1); (l <= j+1) && (l < n); l++)
            if(v[k][l] == 10)
              qtdB++;

        v[i][j] = qtdB;
      }
    }
  }
  
  for(int i = 0; i < m; i++){
    for(int j = 0; j < n; j++)
      if(v[i][j] == 10)
        cout << "B";
      else if(v[i][j] == 0)
        cout << "-";
      else
        cout << v[i][j];
        
    cout << endl;
  }

  return 0;
}
