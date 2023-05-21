#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  int n1, n2, v;
  
  cin >> n1 >> n2;
  int l1[n1], l2[n2];
  
  for(int i = 0; i < n1 ;i++){
    cin >> v;
    l1[i] = v;
  } 

  for(int i = 0; i < n2 ;i++){
    cin >> v;
    l2[i] = v;
  } 

  cout << "{";   
  
  for(int i = 0; i < n1 ;i++)
    for(int j = 0; j < n2 ;j++)
      if(l1[i] == l2[j])
        cout << l1[i] << " ";

  cout << "}\n";
}