#include <iostream>
#include <iomanip>
using namespace std;

int main() {
  double d, nota[5], maior = 0, menor, soma, pena;

  // leitura 
  cin >> d;
  
  for(int i = 0; i <= 4; i++)
    cin >> nota[i];  // guardar em uma lista para usar o for 

  // inicia com 60 pois todos recebem 60 e 
  // perdem/ganham dependendo da distancia
  soma = 60; 
  menor = nota[0];  // iniciar o menor como o primeiro valor

  // Percorrer a lista somando tudo e definindo o menor e o maior 
  for (int i = 0; i <= 4; i++){
    maior = max(maior, nota[i]);  // a > b ? a : b
    menor = min(menor, nota[i]); 	
    soma += nota[i];
  }

  // Calculando a penalidade
  pena = 1.8 * (d - 120);
  // soma final
  soma =  soma - menor - maior + pena;

  // saída 
  cout << setprecision(1) << fixed << soma << endl;

  return 0;
}