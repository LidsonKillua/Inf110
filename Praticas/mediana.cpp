#include <bits/stdc++.h>
using namespace std;

double mediana(int a[], int n);

int main(){
  int n, total = 0;
  double media, median;

  cin >> n;

  int v[n];

  for(int i=0; i<n; i++){
    cin >> v[i]; 
    total += v[i];
  }

  media = 1.0 * total/n;

  median = mediana(v, n);
  
  printf("Media: %.1f\n", media);
  printf("Mediana: %.1f\n", median);
}

double mediana(int a[], int n) {
  int temp;
  double m;

  for(int j=0; j<n-1; j++){
    for(int i=0; i<n-1; i++){
      if(a[i] > a[i+1]){
        temp = a[i];
        a[i] = a[i+1];
        a[i+1] = temp;
      }
    }
  }

  if(n%2 != 0){
    m = a[n/2];
  }
  else{
    m = (a[n/2]+a[n/2 - 1])/2.0;
  }
  
  return m;
}
