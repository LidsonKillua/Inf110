#include <bits/stdc++.h>
using namespace std;

int main(){
  int n, maior = 0, cmaior = 1;
  cin >> n;
    
  int m[n];

  for(int i=0;i<n;i++)
    cin >> m[i];  
    
  for(int i=0;i<n;i++){
    if(m[i] > maior){
        maior = m[i];
        cmaior = 1;
    }
    else if(m[i] == maior)
        cmaior += 1;
  }

  cout << maior << " " << cmaior << endl; 
}
