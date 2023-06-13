#include <bits/stdc++.h>
using namespace std;

void convhoras(int seg, int &h, int &m, int &s){
  int qtdseg[3] = {3600, 60, 1};
  
  h = m = s = 0;
  for(int i = 0; i < 3; i++){
    if(seg >= qtdseg[i]){
      switch(qtdseg[i]){
        case 3600:
          h = seg/qtdseg[i];
          seg -= h*3600;
          break;
        case 60:
          m = seg/qtdseg[i];
          seg -= m*60;
          break;
        case 1:
          s = seg/qtdseg[i];
          seg -= s;
          break;         
      }
    }
  }
}

int main(){
  int seg, h, m, s;
  
  cin >> seg;

  convhoras(seg, h, m, s);

  printf("%0.2d:%0.2d:%0.2d\n", h, m, s);
}
