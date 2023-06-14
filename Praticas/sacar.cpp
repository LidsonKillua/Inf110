#include <iostream>
#include <math.h>
using namespace std;

int main() {
  float v;
  int reais, cent;
  int notas[6] = { 100, 50, 20, 10, 5, 2};
  int moedas[6] = { 100, 50, 25, 10, 5, 1};

  // leitura
  cin >> v;

  // separa a parte inteira das moedas
  reais = int(v);
  cent = round(v * 100 - reais * 100); //bugs e mais bugs

  // percorre as notas e libera o maximo de valor de cada nota
  for(int i = 0; i < 6; i++)
    while(reais >= notas[i]){
        cout << "C " << notas[i] << endl;
        reais -= notas[i];
    }  

  // se sobrar 1 real passar para as moedas
  if(reais == 1)
    cent += 100;

  // percorre as moedas e libera o maximo de valor de cada moeda
  for(int i = 0; i < 6; i++)
    while(cent >= moedas[i]){
        cout << "M " << moedas[i] << endl;
        cent -= moedas[i];
    }  

  return 0;
}
