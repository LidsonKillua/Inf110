// INF110 - Trabalho pratico 3
//
// programa para ler, modificar e gravar uma imagem no formato PNM
//
// Autores: Andre Gustavo dos Santos			(criado em 16/06/14)
//          Andre Gustavo dos Santos			(modificado em 22/05/18)
//			Andre Gustavo dos Santos			(modificado em 13/09/21)
//			Andre Gustavo dos Santos			(modificado em 30/05/23)
//          Lidson Oliveira                     (modificado em 14/06/23)   

#include <bits/stdc++.h>
#include "TP3Tratamentos.cpp"

bool Fcolorida = false;

using namespace std;

int main() {
	unsigned char imagem[MAXALTURA][MAXLARGURA][3];	//a imagem propriamente dita
	int largura, altura;						//dimensoes da imagem
	char tipo[4];										//tipo da imagem
	ifstream arqentrada;						//arquivo que contem a imagem original
	ofstream arqsaida;							//arquivo que contera a imagem modificada
	char comentario[200], c;				//auxiliares
	int i, j, valor;								//auxiliares
	char nomearq[100];							//nome do arquivo
	string msg = "";

//*** LEITURA DA IMAGEM ***//
//inicialmente nao sera necessario entender nem mudar nada nesta parte

	//*** Abertura do arquivo ***//
	cout << "Nome do arquivo com a imagem PNM: ";
	cin >> nomearq;
	arqentrada.open(nomearq,ios::in); //Abre arquivo para leitura
	if (!arqentrada) {
		cout << "Nao consegui abrir arquivo " << nomearq << endl;
		return 0;
	}
//***************************//


//*** Leitura do cabecalho ***//
	arqentrada >> tipo;	//Le o tipo de arquivo
	arqentrada.get();		//Le e descarta o \n do final da 1a. linha

	if (strcmp(tipo,"P2")==0) {
		cout << "Imagem em tons de cinza\n";
		Fcolorida = false;
	}
	else if (strcmp(tipo,"P3")==0) {
		cout << "Imagem colorida\n";
		Fcolorida = true;
	}
	else if (strcmp(tipo,"P1")==0) {
		cout << "Imagem preto e branco\n";
		cout << "Desculpe, nao trabalho com esse tipo de imagem.\n";
		arqentrada.close();
		return 0;
	}
	else if (strcmp(tipo,"P4")==0 || strcmp(tipo,"P5")==0 || strcmp(tipo,"P6")==0) {
		cout << "Imagem no formato RAW\n";
		cout << "Desculpe, nao trabalho com esse tipo de imagem.\n";
		arqentrada.close();
		return 0;
	}

	while((c = arqentrada.get()) == '#')	//Enquanto for comentario
		arqentrada.getline(comentario,200);	//Le e descarta a linha "inteira"

	arqentrada.putback(c);	//Devolve o caractere lido para a entrada, pois como
													//nao era comentario, era o primeiro digito da largura

	arqentrada >> largura >> altura;	//Le as dimensoes da imagem, numero de pixels da horizontal e da vertical
	definirparametros(Fcolorida, largura, altura);
	cout << "Tamanho: " << largura << " x " << altura << endl;
	if (largura > MAXLARGURA) {
		cout << "Desculpe, ainda nao trabalho com imagens com mais de " << MAXLARGURA << " pixels de largura.\n";
		arqentrada.close();
		return 0;
	}
	if (altura > MAXALTURA) {
		cout << "Desculpe, ainda nao trabalho com imagens com mais de " << MAXALTURA << " pixels de altura.\n";
		arqentrada.close();
		return 0;
	}

	arqentrada >> valor;	//Valor maximo do pixel (temos que ler, mas nao sera usado, assumimos 255)
//****************************//


//*** Leitura dos pixels da imagem ***//
	if(Fcolorida)
	for(i=0;i<altura;i++)
		for(j=0;j<largura;j++) 
			for(int k=0;k<3;k++){
				arqentrada >> valor;
				imagem[i][j][k] = (unsigned char)valor;
			}
	else	
	for(i=0;i<altura;i++)
		for(j=0;j<largura;j++) {
			arqentrada >> valor;
			imagem[i][j][0] = (unsigned char)valor;
		}
//************************************//

	arqentrada.close();  //Fecha arquivo apos a leitura

//*** FIM DA LEITURA DA IMAGEM ***//


//*** TRATAMENTO DA IMAGEM ***//
//inicialmente sera nesta parte do codigo que voce vai trabalhar

while (true){
	int opcao; 
	cout << "O que deseja fazer?\n";
	cout << "0 - Sair\n";
	cout << "1 - Escurecer\n";
	cout << "2 - Clarear\n"; 
	cout << "3 - Negativo\n";
	cout << "4 - Espelhar\n";
	cout << "5 - Realce\n";
	cout << "6 - Filtro de Sobel\n";
	cout << "7 - Embossing\n";
	cout << "8 - Luminancia Vermelha\n";

	if(Fcolorida)
		cout << "9 - Tons de cinza\n";

	cin >> opcao;

	if(opcao == 0)
		break;

	switch(opcao){
		case 1: 
			escurecer(imagem); 
			AddMsg(msg, "Escurecer");
			break;

		case 2: 
			clarear(imagem); 
			AddMsg(msg, "Clarear");
			break;

		case 3: 
			negativo(imagem); 
			AddMsg(msg, "Negativo");
			break;
		
		case 4:
			espelhar(imagem);
			AddMsg(msg, "Espelhar");
			break;

		case 5:
			realce(imagem);
			AddMsg(msg, "Realce");
			break;
		
		case 6:
			cout << "Qual tipo de Sobel?\n";
			cout << "1 - Media aritmetica\n";
			cout << "2 - Maior valor\n"; 
			cout << "3 - Magnitude do gradiente\n";

			cin >> opcao; 
			
			switch(opcao){
				case 1: 
				sobel(imagem, 'M');
				AddMsg(msg, "Sobel por Media"); 
				break;

				case 2: 
				sobel(imagem, 'V');
				AddMsg(msg, "Sobel por Maior Valor"); 
				break;

				case 3: 
				sobel(imagem, 'G'); 
				AddMsg(msg, "Sobel por Magnitude do Gradiente");
				break;
			}  
			break;

		case 7: 
			if(Fcolorida)
				tonsDeCinza(imagem);
				AddMsg(msg, "Tons de Cinza");

			embossing(imagem);
			AddMsg(msg, "Embossing");
			break;

		case 8: 
			LuminanciaVermelha(imagem);
			AddMsg(msg, "Luminancia Vermelha");
			break;

		case 9:
			tonsDeCinza(imagem);
			AddMsg(msg, "Tons de Cinza");
			break;
	}

	cout << "--------------------------------------------------\n" + msg +
		    "--------------------------------------------------\n";
}
  

//*** FIM DO TRATAMENTO DA IMAGEM ***//


//*** GRAVACAO DA IMAGEM ***//
//inicialmente nao sera necessario entender nem mudar nada nesta parte

	//*** Grava a nova imagem ***//
	cout << "Nome do arquivo para gravar a imagem PNM: ";
	cin >> nomearq;
	
	arqsaida.open(nomearq,ios::out);	//Abre arquivo para escrita
	if (!arqsaida) {
		cout << "Nao consegui criar" << nomearq << endl;
		return 0;
	}

	arqsaida << tipo << endl;							//tipo
	arqsaida << "# TP3-INF110, by AGS\n";	//comentario
	arqsaida << largura << " " << altura;	//dimensoes
	arqsaida << " " << 255 << endl;				//maior valor
	
	if(Fcolorida)
		for(i=0;i<altura;i++)
			for(j=0;j<largura;j++)
				for(int c=0;c<3;c++)
					arqsaida << (int)imagem[i][j][c] << endl;	//pixels
	else
		for(i=0;i<altura;i++)
			for(j=0;j<largura;j++)
				arqsaida << (int)imagem[i][j][0] << endl;	//pixels

	arqsaida.close();		//fecha o arquivo
	//***************************//

//*** FIM DA GRAVACAO DA IMAGEM ***//

    // Abrir o novo arquivo
    system(nomearq);

	return 0;
}
