#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  int qtd, tA = 0, tR = 0, tF = 0;
  double n;
  
  cin >> qtd;

  for(int i = 1; i <= qtd; i++){
    cin >> n;

    if(n < 40)
      tR++;
    else if(n < 60)
      tF++;
    else 
      tA++;
  }

  printf("Aprovados: %.1f%\n", 100.0*tA/qtd);
  printf("Reprovados: %.1f%\n", 100.0*tR/qtd);
  printf("De exame final: %.1f%\n", 100.0*tF/qtd);
}