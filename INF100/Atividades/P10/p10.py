# Nome: Lidson Oliveira
# Matrícula: 102961
# Data: 26/11/2020		
# Escreva aqui um breve comentário dizendo o que o programa 1 faz
#
# Este programa utiliza uma imagem como base, onde há uma placa com um
# boneco e uma seta no tom de preto, a seguir altera os tons do boneco e da seta
# para mais próximo de um tipo de verde escuro e exibe a imagem alterada.
#
# Escreva o código para a resolução abaixo

# o arquivo imagens.py deve estar no mesmo diretório do programa
import imagens
# o arquivo Pedestre.png também deve estar no mesmo diretório 
im = imagens.Imagem('Pedestre.png')
#im.mostrar()  # Mostrar a imagem na tela # comentei esse comando pois o roteiro pede para mostrar apenas a imagem processada(pelo que eu entendi).

m = im.altura
         # Utilizei esses valores para descobrir as dimensões
n = im.largura
        # e depois apaguei o print, dimensões: 440 x 302

for i in range(132, 286):           # Dimensões de pesquisa escolhidas por tentativa e erro com base no roteiro
    for j in range(88, n-70):       
        if im[i][j] == (0, 0, 0):
            im[i][j] = (50, 130, 50)

        if im[i][j] < (150, 200, 200): #Diminui o raio de pesquisa do vermelho pois estava alterando as bordas do círculo(que é vermelho, logo tem R maior)
            im[i][j] = (50, 130, 50) # Testei vários valores e esse me pareceu bom


im.mostrar()

