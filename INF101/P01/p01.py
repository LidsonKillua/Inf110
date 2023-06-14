# Nome do aluno: Lidson Oliveira
# Matrícula: 102961
# Data: 04/02/2021
# Este programa manipula uma imagem para transformá-la em "tons de cinza" e,
# depois de uma forma chamada "image embossing" e mostra para o usuário a
# imagem e a imagem manipulada.

import imagens

def main():
    # Lê o arquivo com a imagem original e a coloca na matriz im.
    im = imagens.Imagem('fruits-700.jpg')
    im.mostrar()

    # Produz a imagem em tons de cinza em im1 a partir de im.
    print("Tons de cinza...")
    im1 = tonal(im)
    
    # Produz o embossing da imagem em im2 a partir de im1.
    print("Embossing...")
    im2 = emboss(im1)
    im2.mostrar()
    
    print("Fim do processamento!")


# Implemente aqui a função tonal() que recebe uma imagem como parâmetro e
# retorna a imagem em tons de cinza.

def tonal(img):
    im1 = img.copia()
    m = im1.altura
    n = im1.largura
    
    for i in range(0, m):          
        for j in range(0, n):
            r, g, b = img[i][j] 
            im1[i][j] = ( int(0.299 * r + 0.587 * g + 0.114 * b),int(0.299 * r + 0.587 * g + 0.114 * b),int(0.299 * r + 0.587 * g + 0.114 * b)) 
    return im1

# Implemente aqui a função emboss() que recebe uma imagem em tons de cinza e
# retorna a imagem embossed.

def emboss(img):

    im2 = img.copia()
    m = im2.altura
    n = im2.largura
    
    filtro = [[-1, -1, 0],
              [-1, 0, 1],
              [ 0, 1, 1]]
    # Percorre todas as coordenadas da matriz original, deixando de fora as bordas.
    for y in range(1, m-1):
        for x in range(1, n-1):
            pix = 0 # inicia somatório
            #Percorre matriz de convolução.
            for i in range(0,3):
                for j in range(0,3):
                    # Pega pixel "embaixo" da coordenada do filtro.
                    r, g, b = img[y-(1-i)][x-(1-j)]
                    #multiplica pelo filtro e soma. Para isso podemos usar apenas
                    # um dos componentes (r, g ou b), já que todos são iguais.
                    pix = pix + r * filtro[i][j]
            #Corrige o brilho e garante que fique entre 0 e 255.
            pix = max(0, min(255, pix+128))
            # Atribui o pixel a im2.
            im2[y][x] = (pix, pix, pix)
            
    return im2

# Chama a função main para iniciar o processo.
main()
