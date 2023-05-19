#include <bits/stdc++.h>
using namespace std;

int main(){
  int m, n, valrep;
  bool rep = false;

  cin >> m;

  for(int i = 0; i < m; i++){
    cin >> n;
    int v[n];

    for(int j = 0; j < n; j++)
      cin >> v[j];

    for(int j = 0; j < n; j++){
      valrep = v[j];

      for(int k = j+1; k < n; k++)
        if(v[k] == valrep){
          rep = true;
          break;
        }

        if(rep){
          cout << "SIM: " << valrep << endl;
          break;
        }
    }

    if(!rep)
      cout << "NAO" << endl;
    else
      rep = false;

  }


  return 0;
}
