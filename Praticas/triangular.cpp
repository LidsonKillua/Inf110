#include <bits/stdc++.h>
using namespace std;

bool triang(int a[][1000], int n);

int main(){
  int n;

  cin >> n;

  int v[n][1000];

  for(int i=0; i<n; i++)
    for(int j=0; j<n; j++){
    cin >> v[i][j]; 
  }

  if(triang(v, n)){
    cout << "SIM" << endl;
  }
  else{
    cout << "NAO" << endl;
  }
}

bool triang(int a[][1000], int n) {
  for(int j=0; j<n; j++){
    for(int i=j+1; i<n; i++){
      if(a[i][j] != 0){
        return false;
      }
    }  
  }

  return true;
}
