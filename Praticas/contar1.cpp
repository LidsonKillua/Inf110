#include <iostream>
#include <iomanip>
using namespace std;

int main() {
  int v, soma = 0;
  char tipo;

  while(true){
    // leitura 
    cin >> tipo >> v;

    // parar se digitar 0
    if(v == 0)
        break;
    
    // teste para somar em centavos
    if(tipo == 'M')
        soma += v;
    else
        soma += v * 100; 
  }

  // saída dividindo por 100 para mostar as moedas em reais
  cout << "R$" << setprecision(2) << fixed << soma/100.0 << endl;

  return 0;
}