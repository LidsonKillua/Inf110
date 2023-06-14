# Nome: 
# Matrícula:
# Data:

import numpy as np


def q1(): 		   
# Escreva aqui um breve comentário sobre o programa solução da questão 1 
#
#    
# Escreva o código para a resolução da questão 1 abaixo
# Os comandos devem estar alinhados (mesma coluna) do comando print()


    # leitura dos valores de número de linhas e de colunas de A e B
    # mA =  # numero de linhas de A
    # nA =  # numero de colunas de A
    # mB =  # numero de linhas de B
    # nB =  # numero de colunas de B
   

    
    # iniciar gerador de números aleatórios para que os valores sejam
    # OS MESMOS sempre que o programa for executado.
    np.random.seed( 0 )

    # gerar as matrizes A e B: m x n de valores inteiros aleatórios 0 - 10
    A = np.random.randint( 0, 11, (mA, nA) )
    B = np.random.randint( 0, 11, (mB, nB) )



    
def q2():
# Escreva aqui um breve comentário sobre o programa solução da questão 2
#
#
# Escreva o código para a resolução da questão 1 abaixo
# Os comandos devem estar alinhados (mesma coluna) do comando import
    import random
    # leitura da dimensão da matriz
    # m =  # numero de linhas
    # n =  # numero de colunas




    
    # inicializa semente aleatória
    np.random.seed( 0 )
    # gerar uma matriz A de valores inteiros aleatórios 0.0 - 10.0
    A = np.empty((m, n))
    for i in range (0, m):
        for j in range (0, n) :
            A[i][j] = 10*random.random() # gera um valor entre 0.0 e 10.0
            

    
