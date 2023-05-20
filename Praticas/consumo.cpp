#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  float v, km = 0, l = 0;
  char c;
  
  while(true){
    cin >> c;
    if(c == 'X') 
      break;
    
    cin >> v;

    km += (c == 'R') ? v : 0;
    l += (c == 'A') ? v : 0; 
  }

  printf("%.2f\n", km/l);
}