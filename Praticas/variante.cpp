#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  int p0, tx, semanas = 0;
  long long infec;
  cin >> p0 >> tx;

  infec = p0;

  while(infec < 1000000000){
    infec = infec + (infec * tx);
    semanas += 1;
  }

  cout << semanas << endl;
}