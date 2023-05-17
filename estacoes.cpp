#include <iostream>
using namespace std;

int main() {
  int d, m;
  string mes, estacao;
  
  // leitura 
  cin >> d >> m;

  // definindo o mes por extenso
  switch(m){
    case 1: mes = "janeiro";
            break;
    case 2: mes = "fevereiro";
            break;
    case 3: mes = "marco";
            break;
    case 4: mes = "abril";
            break;
    case 5: mes = "maio";
            break;
    case 6: mes = "junho";
            break;
    case 7: mes = "julho";
            break;
    case 8: mes = "agosto";
            break;
    case 9: mes = "setembro";
            break;
    case 10: mes = "outubro";
            break;
    case 11: mes = "novembro";
            break;
    case 12: mes = "dezembro";
            break;
  }

  // definindo estacao
  if ((m < 3 || (m == 3 && d < 20)) || (d >= 22 && m == 12))
    estacao = "Verao";
  else if (m < 6 || (m == 6 && d < 21))
    estacao = "Outono";
  else if (m < 9 || (m == 9 && d < 23))
    estacao = "Inverno";
  else if (m < 12 || (m == 12 && d < 22))
    estacao = "Primavera";

  // saída
  cout << d << " de " << mes << endl;
  cout << estacao << endl;

  return 0;
}