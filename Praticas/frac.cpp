#include <bits/stdc++.h>
using namespace std;

//Recebe frações na/da e nb/db e retorna por referência nr/dr = na/da + nb/db
void somafrac(int na, int da, int nb, int db, int &nr, int &dr);

int main(){
  int na, nb, da, db, nr, dr;

  scanf("%d/%d %d/%d", &na, &da, &nb, &db);
  somafrac(na, da, nb, db, nr, dr);
  printf("%d/%d+%d/%d=%d/%d\n", na, da, nb, db, nr, dr);
}

int mmc(int a, int b){  
  for(int i = (a < b) ? b : a; ;i++)
    if((i % a == 0) && (i % b == 0))
      return i;
} 

int mdc(int a, int b){ 
  for(int i = (a < b) ? b : a; i > 0 ;i--)
    if((a % i == 0) && (b % i == 0))
      return i;
  
  return 1;
} 

void somafrac(int na, int da, int nb, int db, int &nr, int &dr){
  int nt, dt;

  if(da == db){
    dt = da;
    nt = na + nb;
  }
  else{
    dt = mmc(da, db);
    nt = (dt/da*na) + (dt/db*nb);
  }

  nr = nt/mdc(dt, nt);
  dr = dt/mdc(dt, nt);
}
