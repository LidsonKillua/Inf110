#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  int qtd = 0;
  char c, oldC = '.';
 
  do
  {
    cin >> c;
    
    if(c == oldC || oldC == '.')
      qtd++;
    else{
        cout << qtd << oldC;
        qtd = 1;
    }
    
    oldC = c;
  } while (c != '.');

  cout << 0 << endl;
}