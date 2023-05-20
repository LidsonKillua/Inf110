#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  //cin.tie(0);
  //ios_base::sync_with_stdio(0);

  int n, ft, fp;
  cin >> n >> ft >> fp;

  if(n < 40 || ft > 15 || fp > 7)
    cout << "Reprovado";
  else if(n < 60)
    cout << "Final";
  else
    cout << "Aprovado";

  cout << endl;
}