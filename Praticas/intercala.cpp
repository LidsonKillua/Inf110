#include <bits/stdc++.h>
using namespace std;
//using ll = long long;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(0);

  int n, v;
  
  cin >> n;
  int v1[n], v2[n];
  
  for(int i = 0; i < n ;i++){
    cin >> v;
    v1[i] = v;
  } 

  for(int i = 0; i < n ;i++){
    cin >> v;
    v2[i] = v;
  } 

  for(int i = 0; i < n ;i++){
    cout << v1[i] << " " << v2[i] << " ";
  } 
  cout << endl;
}