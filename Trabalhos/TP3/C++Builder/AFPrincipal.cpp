//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop
#include <iostream>
#include <fstream>
#include <cstring>
#include <stdlib.h>

#include "AFPrincipal.h"
using namespace std;
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TfrmPrincipal *frmPrincipal;

const int MAXALTURA  = 570;				//tamanho maximo aceito (pode ser alterado)
const int MAXLARGURA = 570;
bool Fcolorida = false;
unsigned char imagem[MAXALTURA][MAXLARGURA][3];	//a imagem propriamente dita
int largura, altura, Flargura, Faltura;						//dimensoes da imagem
char tipo[4];										//tipo da imagem
ifstream arqentrada;						//arquivo que contem a imagem original
ofstream arqsaida;							//arquivo que contera a imagem modificada
char comentario[200], c;				//auxiliares
int i, j, valor;								//auxiliares
string nomearq;							//nome do arquivo
string msg = "";
int aux[MAXALTURA][MAXLARGURA][3], auxY[MAXALTURA][MAXLARGURA][3], auxX[MAXALTURA][MAXLARGURA][3];

//---------------------------------------------------------------------------
int ValidatePx(int valor);
void AddMsg(string &msg, string filtro);
void aplicarFiltro(unsigned char imagem[][MAXLARGURA][3], int filtro[3][3], int aux[][MAXLARGURA][3]);
void escurecer(unsigned char imagem[MAXALTURA][MAXLARGURA][3]);
void clarear(unsigned char imagem[MAXALTURA][MAXLARGURA][3]);
void negativo(unsigned char imagem[MAXALTURA][MAXLARGURA][3]);
void espelhar(unsigned char imagem[MAXALTURA][MAXLARGURA][3]);
void realce(unsigned char imagem[MAXALTURA][MAXLARGURA][3]);
void sobel(unsigned char imagem[MAXALTURA][MAXLARGURA][3], char tipo);
void tonsDeCinza(unsigned char imagem[MAXALTURA][MAXLARGURA][3]);
void LuminanciaVermelha(unsigned char imagem[MAXALTURA][MAXLARGURA][3]);
void embossing(unsigned char imagem[MAXALTURA][MAXLARGURA][3]);
//---------------------------------------------------------------------------
__fastcall TfrmPrincipal::TfrmPrincipal(TComponent* Owner)
	: TForm(Owner)
{
	opdPrincipal->Filter = "PNM files (*.pnm)|*.PNM";
	spdPrincipal->Filter = "PNM files (*.pnm)|*.PNM";
}
//---------------------------------------------------------------------------
void __fastcall TfrmPrincipal::btnImgClick(TObject *Sender)
{
	//*** Abertura do arquivo ***//
	if (opdPrincipal->Execute()){
		if (FileExists(opdPrincipal->FileName)){
			nomearq = (AnsiString(opdPrincipal->FileName)).c_str();
			arqentrada.open(nomearq, ios::in);

			if (!arqentrada)
				throw(Exception("Nao consegui abrir arquivo."));
		}
		else{
		  throw(Exception("Nao consegui abrir arquivo."));
		}
	}
	//***************************//

	//*** Leitura do cabecalho ***//
	arqentrada >> tipo;	//Le o tipo de arquivo
	arqentrada.get();	//Le e descarta o \n do final da 1a. linha

	if (strcmp(tipo,"P2")==0) {
		mmoPrincipal->Lines->Append(("Imagem aberta: "+nomearq).c_str());
		mmoPrincipal->Lines->Append("Imagem em tons de cinza\n");
		Fcolorida = false;
	}
	else if (strcmp(tipo,"P3")==0) {
		mmoPrincipal->Lines->Append(("Imagem aberta: "+nomearq).c_str());
		mmoPrincipal->Lines->Append("Imagem colorida\n");
		Fcolorida = true;
	}
	else if (strcmp(tipo,"P1")==0) {
		mmoPrincipal->Text += "Imagem preto e branco\n";
		arqentrada.close();
		throw(Exception("Desculpe, ainda nao trabalho com esse tipo de imagem."));
	}
	else if (strcmp(tipo,"P4")==0 || strcmp(tipo,"P5")==0 || strcmp(tipo,"P6")==0) {
		mmoPrincipal->Text += "Imagem no formato RAW\n";
		arqentrada.close();
		throw(Exception("Desculpe, ainda nao trabalho com esse tipo de imagem."));
	}

	while((c = arqentrada.get()) == '#')	//Enquanto for comentario
		arqentrada.getline(comentario,200);	//Le e descarta a linha "inteira"

	arqentrada.putback(c);	//Devolve o caractere lido para a entrada, pois como
													//nao era comentario, era o primeiro digito da largura

	arqentrada >> largura >> altura;	//Le as dimensoes da imagem, numero de pixels da horizontal e da vertical
	Faltura = altura;
	Flargura = largura;
	mmoPrincipal->Lines->Append(("Tamanho: "+ IntToStr(largura)+" x "+IntToStr(altura)+"\n").c_str());
	if (largura > MAXLARGURA) {
		arqentrada.close();
		throw(Exception("Desculpe, ainda nao trabalho com imagens com muitos pixels de largura."));
	}
	if (altura > MAXALTURA) {
		arqentrada.close();
		throw(Exception("Desculpe, ainda nao trabalho com imagens com muitos pixels de altura."));
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

	/* Se leu a imagem, habilitar botões */
	btnAplicar->Enabled = true;
	btnMostrar->Enabled = true;
    rgrFiltros->Enabled = true;

	//*** FIM DA LEITURA DA IMAGEM ***//
}
//---------------------------------------------------------------------------
void __fastcall TfrmPrincipal::btnAplicarClick(TObject *Sender)
{
	switch(rgrFiltros->ItemIndex){
		case 0:
			escurecer(imagem);
			AddMsg(msg, "Escurecer");
			mmoPrincipal->Lines->Append(msg.c_str());
			break;

		case 1:
			clarear(imagem);
			AddMsg(msg, "Clarear");
			mmoPrincipal->Lines->Append(msg.c_str());
			break;

		case 2:
			negativo(imagem);
			AddMsg(msg, "Negativo");
			mmoPrincipal->Lines->Append(msg.c_str());
			break;

		case 3:
			espelhar(imagem);
			AddMsg(msg, "Espelhar");
			mmoPrincipal->Lines->Append(msg.c_str());
			break;

		case 4:
			realce(imagem);
			AddMsg(msg, "Realce");
			mmoPrincipal->Lines->Append(msg.c_str());
			break;

		case 5:
			switch(StrToInt(InputBox("Qual tipo de Sobel? ", "1 - Media aritmetica\n2 - Maior valor\n3 - Magnitude do gradiente\n", "1"))){
				case 1:
				sobel(imagem, 'M');
				AddMsg(msg, "Sobel por Media");
				mmoPrincipal->Lines->Append(msg.c_str());
				break;

				case 2:
				sobel(imagem, 'V');
				AddMsg(msg, "Sobel por Maior Valor");
				mmoPrincipal->Lines->Append(msg.c_str());
				break;

				case 3:
				sobel(imagem, 'G');
				AddMsg(msg, "Sobel por Magnitude do Gradiente");
				mmoPrincipal->Lines->Append(msg.c_str());
				break;
			}
			break;

		case 7:
			if(Fcolorida){
				tonsDeCinza(imagem);
				AddMsg(msg, "Tons de Cinza");
				mmoPrincipal->Lines->Append(msg.c_str());
			}

			embossing(imagem);
			AddMsg(msg, "Embossing");
			mmoPrincipal->Lines->Append(msg.c_str());
			break;

		case 8:
			LuminanciaVermelha(imagem);
			AddMsg(msg, "Luminancia Vermelha");
			mmoPrincipal->Lines->Append(msg.c_str());
			break;

		case 9:
			tonsDeCinza(imagem);
			AddMsg(msg, "Tons de Cinza");
            mmoPrincipal->Lines->Append(msg.c_str());
			break;
	}
    btnSalvar->Enabled = true;
}
//---------------------------------------------------------------------------
void __fastcall TfrmPrincipal::btnSalvarClick(TObject *Sender)
{
	if (spdPrincipal->Execute()){
		nomearq = (AnsiString(spdPrincipal->FileName)).c_str();
		arqsaida.open(nomearq,ios::out);	//Abre arquivo para escrita

		if (!arqsaida) {
			throw(Exception("Nao consegui abrir arquivo."));
		}

		arqsaida << tipo << endl;				//tipo
		arqsaida << "# TP3-INF110, by AGS\n";	//comentario
		arqsaida << largura << " " << altura;	//dimensoes
		arqsaida << " " << 255 << endl;			//maior valor

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
	}
    //*** FIM DA GRAVACAO DA IMAGEM ***//
}
//---------------------------------------------------------------------------
void __fastcall TfrmPrincipal::btnMostrarClick(TObject *Sender)
{
	system(nomearq.c_str());
}
//---------------------------------------------------------------------------
//*** Manter o pixel entre 0 e 255 ***//
int ValidatePx(int valor){
    if (valor > 255)						//se der > 255
		return 255;							//  deixa branco
    else if (valor < 0)						//se der negativo
		return 0;					        //  deixa preto

    return valor;                           // se não, deixa como está
}
//---------------------------------------------------------------------------
//*** Mensagem mostrada a cada uso ***//
void AddMsg(string &msg, string filtro){
	msg += "filtro "+ filtro + " aplicado\n";
}
//---------------------------------------------------------------------------
//*** Void base que aplica os filtros 3x3(maioria nesse trabalho) ***//
void aplicarFiltro(unsigned char imagem[][MAXLARGURA][3], int filtro[3][3], int aux[][MAXLARGURA][3]){
	for(int i=0;i<Faltura;i++)
		for(int j=0;j<Flargura;j++)
            for(int c=0;c<3;c++){
                int soma = 0;
				// usa k e l para varrer a submatriz 3x3 sem sair dos limites e associa m e n para varrer o filtro.
                for(int k = ((i-1 < 0) ? i : i-1), m = ((i-1 < 0) ? 1 : 0); (k <= i+1) && (k < MAXALTURA); k++, m++)
                    for(int l = ((j-1 < 0) ? j : j-1), n = ((j-1 < 0) ? 1 : 0); (l <= j+1) && (l < MAXLARGURA); l++, n++){
                        soma += ((int)imagem[k][l][c] * filtro[m][n]);
                    }
                aux[i][j][c] = ValidatePx(soma);	//Valida e salva na temporária
		}
}
//---------------------------------------------------------------------------

void escurecer(unsigned char imagem[MAXALTURA][MAXLARGURA][3]){
	int fator, valor;

	fator = StrToInt(InputBox("Qual o fator de escurecimento (1-100)? ", "Fator", "0"));

	//*** Escurece a imagem ***//
	for(int i=0;i<Faltura;i++)
		for(int j=0;j<Flargura;j++)
            for(int c=0;c<3;c++){
                valor = (int)imagem[i][j][c];			//pega o valor do pixel
                valor -= fator;									//escurece o pixel
                imagem[i][j][c] = (unsigned char)ValidatePx(valor);	//modifica o pixel
            }
}
//---------------------------------------------------------------------------
void clarear(unsigned char imagem[MAXALTURA][MAXLARGURA][3]){
	int fator, valor;

	fator = StrToInt(InputBox("Qual o fator de clareamento (1-100)? ", "Fator", "0"));

	//*** Clareia a imagem ***//
	if(!Fcolorida)
        for(int i=0;i<Faltura;i++)
            for(int j=0;j<Flargura;j++){
                valor = (int)imagem[i][j][0];			//pega o valor do pixel
                valor += fator;									//Clareia o pixel
                imagem[i][j][0] = (unsigned char)ValidatePx(valor);	//Valida e modifica o pixel
            }
    else
        for(int i=0;i<Faltura;i++)
            for(int j=0;j<Flargura;j++)
                for(int c=0;c<3;c++){
                    valor = (int)imagem[i][j][c];			//pega o valor do pixel
                    valor += fator;									//Clareia o pixel
                    imagem[i][j][c] = (unsigned char)ValidatePx(valor);	//Valida e modifica o pixel
				}
}
//---------------------------------------------------------------------------
void negativo(unsigned char imagem[MAXALTURA][MAXLARGURA][3]){
    int valor;

	//*** Negativa a imagem ***//
	if(!Fcolorida)
		for(int i=0;i<altura;i++)
			for(int j=0;j<largura;j++){
                valor = (int)imagem[i][j][0];			//pega o valor do pixel
				valor = 255 - valor;				    //negativa o pixel
                imagem[i][j][0] = (unsigned char)valor;	//modifica o pixel
			}
	else
		for(int i=0;i<altura;i++)
			for(int j=0;j<largura;j++)
                for(int c=0;c<3;c++){
                    valor = (int)imagem[i][j][c];			//pega o valor do pixel
                    valor = 255 - valor;				    //negativa o pixel
                    imagem[i][j][c] = (unsigned char)valor;	//modifica o pixel
                }
}
//---------------------------------------------------------------------------
void espelhar(unsigned char imagem[MAXALTURA][MAXLARGURA][3]){
	//*** Espelha a imagem ***//
	if (!Fcolorida)
        for(int i=0;i<Faltura;i++)
            for(int j=0;j<Flargura;j++){
                aux[i][Flargura - j][0] = imagem[i][j][0];	//espelha em uma temporária
            }
    else
        for(int i=0;i<Faltura;i++)
            for(int j=0;j<Flargura;j++)
                for(int c=0;c<3;c++){
                    aux[i][Flargura - j][c] = imagem[i][j][c];	//espelha em uma temporária
                }

    for(int i=0;i<Faltura;i++)
        for(int j=0;j<Flargura;j++)
            for(int c=0;c<3;c++)
                imagem[i][j][c] = aux[i][j][c]; //Salva a imagem
}
//---------------------------------------------------------------------------
void realce(unsigned char imagem[MAXALTURA][MAXLARGURA][3]){
    int filtro[3][3] = {0, -1, 0, -1, 5, -1, 0, -1, 0};

    // Usa a função Genérica para aplicar o filtro na imagem e gravar na aux
    aplicarFiltro(imagem, filtro, aux);

    // Salva a imagem da auxiliar na principal
    for(int i=0;i<Faltura;i++)
		for(int j=0;j<Flargura;j++)
            for(int c=0;c<3;c++)
                imagem[i][j][c] = (unsigned char)aux[i][j][c];
}
//---------------------------------------------------------------------------
void sobel(unsigned char imagem[MAXALTURA][MAXLARGURA][3], char tipo = 'M'){
    float valor;
    int
      gY[3][3] = {1, 2, 1, 0, 0, 0, -1, -2, -1}, // Filtro na vertical
      gX[3][3] = {1, 0, -1, 2, 0, -2, 1, 0, -1}; // Filtro na horizontal

    // Usa a função Genérica para aplicar o filtro na imagem e gravar na aux
    aplicarFiltro(imagem, gY, auxY);
    aplicarFiltro(imagem, gX, auxX);

    // Salva a imagem da auxiliar na principal
    for(int i=0;i<Faltura;i++)
		for(int j=0;j<Flargura;j++)
            for(int c=0;c<3;c++){
                switch (tipo)
                {
                case 'M': //media aritmética
                    valor = (auxY[i][j][c]+auxX[i][j][c])/2;
                    break;
                case 'V': //maior valor
                    valor = max(auxY[i][j][c], auxX[i][j][c]);
                    break;
                case 'G': //magnitude do gradiente
                    valor = sqrt(pow(auxY[i][j][c], 2) + pow(auxX[i][j][c], 2));
                    break;
                default: // tipo vai ser 'M' por padrão
                    break;
                }
                imagem[i][j][c] = (unsigned char) ValidatePx(valor);
            }
}
//---------------------------------------------------------------------------
void tonsDeCinza(unsigned char imagem[MAXALTURA][MAXLARGURA][3]){
	// aplica a formula de luminância = int(0.299 * r + 0.587 * g + 0.114 * b)
    for(int i=0;i<Faltura;i++)
		for(int j=0;j<Flargura;j++){
            imagem[i][j][0] = imagem[i][j][1] = imagem[i][j][2] =
                imagem[i][j][0] * 0.299 +
                imagem[i][j][1] * 0.587 +
                imagem[i][j][2] * 0.114;
        }
}
//---------------------------------------------------------------------------
void LuminanciaVermelha(unsigned char imagem[MAXALTURA][MAXLARGURA][3]){
    // apliquei a formula da luminância = int(0.299 * r + 0.587 * g + 0.114 * b)
    // errada e deu nisso aí kkk
    for(int i=0;i<Faltura;i++)
		for(int j=0;j<Flargura;j++){
            imagem[i][j][0] = ValidatePx(imagem[i][j][0] * 0.299 +
                                         imagem[i][j][1] * 0.587 +
                                         imagem[i][j][2] * 0.114);

            imagem[i][j][1] = imagem[i][j][2] = 0;
        }
}
//---------------------------------------------------------------------------
void embossing(unsigned char imagem[MAXALTURA][MAXLARGURA][3]){
	int filtro[3][3] = {-1, -1, 0, -1, 0, 1, 0, 1, 1};

    int r;

    // Percorre todas as coordenadas da matriz original, deixando de fora as bordas.
    for(int i=1;i<Faltura-1;i++)
		for(int j=1;j<Flargura-1;j++){
            int soma = 0;
            // percorre a matriz de convolução
            for(int k = 0; k < 3; k++)
                for(int l = 0; l < 3; l++){
                    // Pega pixel "embaixo" da coordenada do filtro.
                    r = imagem[i-(1-k)][j-(1-l)][0];
                    // multiplica pelo filtro e soma. Para isso podemos usar apenas
                    // um dos componentes (r, g ou b), já que todos são iguais.
                    soma += (r * filtro[k][l]);
                }

            for(int c=0;c<3;c++)
                //Adiciona 128 para ficar no efeito metálico, valida e atribui o pixel
                imagem[i-1][j-1][c] = (unsigned char) ValidatePx(soma + 128);
		}
}
//---------------------------------------------------------------------------

void __fastcall TfrmPrincipal::FormShow(TObject *Sender)
{
	btnAplicar->Enabled = false;
	btnSalvar->Enabled = false;
	btnMostrar->Enabled = false;
	rgrFiltros->Enabled = false;
}
//---------------------------------------------------------------------------

