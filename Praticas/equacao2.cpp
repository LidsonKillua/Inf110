#include <bits/stdc++.h>
using namespace std;

//Retorna o número de raízes reais de uma eq. do 2◦ grau de coeficientes a b c
//Retorna as raízes por refer^encia em x1 e x2
int eq2grau(double a, double b, double c, double &x1, double &x2);

int main(){
  double a, b, c, x1, x2;
  
  cin >> a >> b >> c;  
    
  switch (eq2grau(a, b, c, x1, x2))
  {
  case 0:
    printf("Nao ha raiz real\n");
    break;

  case 1:
    printf("%.2f\n", x1);
    break;
  
  case 2:
    printf("%.2f %.2f\n", x1, x2);
    break;
  }  
}


int eq2grau(double a, double b, double c, double &x1, double &x2){
  double delta = (b * b - 4 * a * c); 
  
  if(delta < 0) 
    return 0;
  else if(delta == 0){
    x1 = (-b + sqrt(delta))/ (2 * a);
    return 1;
  }
  else{
    x1 = (-b - sqrt(delta))/ (2 * a);
    x2 = (-b + sqrt(delta))/ (2 * a);
    return 2;
  }  
}
