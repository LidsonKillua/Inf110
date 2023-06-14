#include <bits/stdc++.h>
#include "TP3Consts.cpp"
using namespace std;

// Auxiliares 
int
  aux[MAXALTURA][MAXLARGURA][3], auxY[MAXALTURA][MAXLARGURA][3], auxX[MAXALTURA][MAXLARGURA][3];

// Parâmetros
bool 
  Colorida = false;
int
  Flargura = MAXLARGURA,
  Faltura = MAXALTURA;

void definirparametros(bool colorida, int largura, int altura){
  Colorida = colorida;
  Flargura = largura;
  Faltura = altura;
}

int ValidatePx(int valor){
    if (valor > 255)						//se der > 255
		return 255;							//  deixa branco
    else if (valor < 0)						//se der negativo
		return 0;					        //  deixa preto
    
    return valor;                           // se não, deixa como está
}

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

void aplicarFiltro2(unsigned char imagem[][MAXLARGURA][3], int filtro[3][3], int aux[][MAXLARGURA][3]){
    int r;
    for(int i=1;i<Faltura-1;i++)
		for(int j=1;j<Flargura-1;j++){
            int soma = 0;
            // usa k e l para varrer a submatriz 3x3 sem sair dos limites e associa m e n para varrer o filtro.
            for(int k = 0; k < 3; k++)
                for(int l = 0; l < 3; l++){
                    r = imagem[i-(1-k)][j-(1-l)][0];   

                    soma += (r * filtro[k][l]);
                }

            for(int c=0;c<3;c++)
                aux[i][j][c] = ValidatePx(soma);	//Valida e salva na temporária
		}
}

void escurecer(unsigned char imagem[MAXALTURA][MAXLARGURA][3]){
    int fator, valor;
	cout << "Qual o fator de escurecimento (1-100)? ";
	cin >> fator;

	//*** Escurece a imagem ***//
	for(int i=0;i<Faltura;i++)
		for(int j=0;j<Flargura;j++)
            for(int c=0;c<3;c++){
                valor = (int)imagem[i][j][c];			//pega o valor do pixel
                valor -= fator;									//escurece o pixel
                imagem[i][j][c] = (unsigned char)ValidatePx(valor);	//modifica o pixel
            }
}

void clarear(unsigned char imagem[MAXALTURA][MAXLARGURA][3]){
    int fator, valor;
	cout << "Qual o fator de clareamento (1-100)? ";
	cin >> fator;

	//*** Clareia a imagem ***//
    if(!Colorida)
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

void negativo(unsigned char imagem[MAXALTURA][MAXLARGURA][3]){
    int valor;

	//*** Clareia a imagem ***//
    if(!Colorida)
        for(int i=0;i<Faltura;i++)
            for(int j=0;j<Flargura;j++){
                valor = (int)imagem[i][j][0];			//pega o valor do pixel
                valor = 255 - valor;				    //negativa o pixel
                imagem[i][j][0] = (unsigned char)valor;	//modifica o pixel
            }
    else
        for(int i=0;i<Faltura;i++)
            for(int j=0;j<Flargura;j++)
                for(int c=0;c<3;c++){
                    valor = (int)imagem[i][j][c];			//pega o valor do pixel
                    valor = 255 - valor;				    //negativa o pixel
                    imagem[i][j][c] = (unsigned char)valor;	//modifica o pixel
                }
}

void espelhar(unsigned char imagem[MAXALTURA][MAXLARGURA][3]){
	//*** Espelha a imagem ***//
    if (!Colorida)
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

void sobel(unsigned char imagem[MAXALTURA][MAXLARGURA][3], char tipo = 'M'){
    int valor,
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
                    valor = sqrt(auxY[i][j][c]+auxX[i][j][c]);
                    break;
                default: // tipo vai ser 'M' por padrão 
                    break;
                }
                imagem[i][j][c] = (unsigned char)ValidatePx(valor); 
            }            
}

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

void embossing(unsigned char imagem[MAXALTURA][MAXLARGURA][3]){
    int filtro[3][3] = {-1, -1, 0, -1, 0, 1, 0, 1, 1};
    
    // Usa a função Genérica para aplicar o filtro na imagem e gravar na aux
    aplicarFiltro2(imagem, filtro, aux);
    
    // Salva a imagem da auxiliar na principal
    for(int i=0;i<Faltura;i++)
		for(int j=0;j<Flargura;j++){
            for(int c=0;c<3;c++)
                imagem[i][j][c] = (unsigned char) aux[i][j][c];
        }
}
