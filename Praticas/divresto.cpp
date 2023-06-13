#include <bits/stdc++.h>
using namespace std;

// retorna a divisão e o resto
bool divresto(int, int, int &, int &);

int main(){
  int n, a, b, d, r;
  
  cin >> n;

  for(int i = 0; i < n; i++){
    cin >> a >> b;
    
    if (divresto(a, b, d, r)){
      printf("%d %d\n", d, r);
    }
    else{
      printf("indefinido\n");
    }    
  }
}


bool divresto(int x, int y, int &div, int &rest){
  if(y == 0) 
    return false;
  
  div = x/y;
  rest = x%y;

  return true;
}
