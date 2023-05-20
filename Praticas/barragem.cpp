#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  int p, tM , t = 0, pM, pT = 0;
  cin >> p >> tM;
  
  do
  {
    if(t <= tM)
      pT += pM;
      
    cin >> pM;
    t++;
  } while(pM != -1);
    
  if(p == pT)
    cout << "Todos a salvo" << endl;
  else 
    cout << "Apenas " << pT << " pessoas a salvo" << endl;
}