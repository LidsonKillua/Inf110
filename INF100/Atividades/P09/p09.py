# Nome: Lidson Oliveira
# Matrícula: 102961
# Data: 19/11/2020

import numpy as np


def q1(): 		   
# Escreva aqui um breve comentário sobre o programa solução da questão 1 
# Este programa cria duas matrizes com os tamanhos definidos pelo usuário no conjunto (2-10),
# e atribui a elas valores pseudo aleatórios, após isso mostra essas duas matrizes e realiza
# duas operações, add and cut e add and keep, e mostra as matrizes resultantes dessas operações também
#
# Escreva o código para a resolução da questão 1 abaixo
# Os comandos devem estar alinhados (mesma coluna) do comando print()


    # leitura dos valores de número de linhas e de colunas de A e B
    mA = int(input('Número de linhas da matriz A (2-10): '))  # mA =  # numero de linhas de A

    while mA < 2 or mA > 10:
        print('Valor inválido!!!')
        mA = int(input('Número de linhas da matriz A (2-10): '))
        
    nA = int(input('Número de colunas da matriz A (2-10): '))  # nA =  # numero de colunas de A

    while nA < 2 or nA > 10:
        print('Valor inválido!!!')
        nA = int(input('Número de colunas da matriz A (2-10): '))
        
    mB = int(input('Número de linhas da matriz B (2-10): '))  # mB =  # numero de linhas de B

    while mB < 2 or mB > 10:
        print('Valor inválido!!!')
        mB = int(input('Número de linhas da matriz B (2-10): '))
        
    nB = int(input('Número de colunas da matriz B (2-10): '))  # nB =  # numero de colunas de B

    while nB < 2 or nB > 10:
        print('Valor inválido!!!')
        nB = int(input('Número de colunas da matriz B (2-10): '))

    # iniciar gerador de números aleatórios para que os valores sejam
    # OS MESMOS sempre que o programa for executado.
    np.random.seed( 0 )

    # gerar as matrizes A e B: m x n de valores inteiros aleatórios 0 - 10
    A = np.random.randint( 0, 11, (mA, nA) )
    B = np.random.randint( 0, 11, (mB, nB) )

    print('Matriz A:')
    cont = 0
    for i in range(0, mA):
        for j in range(0, nA):
            if i != cont:
                print('')
                print('%3.f'%A[i][j], end = '')
                cont = i
            else:
                print('%3.f'%A[i][j], end = '')
                cont = i

    print()
    print()
    print('Matriz B:')
    cont = 0
    for i in range(0, mB):
        for j in range(0, nB):
            if i != cont:
                print('')
                print('%3.f'%B[i][j], end = '')
                cont = i
            else:
                print('%3.f'%B[i][j], end = '')
                cont = i

    mC = min(mA, mB)
    nC = min(nA, nB)
    C = np.zeros((mC,nC), dtype=int)

    for i in range(0, mC):       
        for j in range(0, nC): 
            C[i][j] = A[i][j]+B[i][j]

    print()
    print()
    print('A add and cut B:')
    cont = 0
    for i in range(0, mC):       
        for j in range(0, nC):   
            if i != cont:
                print('')
                print('%3.f'%(C[i][j]), end = '')
                cont = i
            else:
                print('%3.f'%(C[i][j]), end = '')
                cont = i
                
    mD = max(mA, mB)
    nD = max(nA, nB)
    D = np.zeros((mD,nD), dtype=int)

    for i in range(0, mA):       
        for j in range(0, nA): 
            D[i][j] += A[i][j]
            
    for i in range(0, mB):       
        for j in range(0, nB): 
            D[i][j] += B[i][j]

    print()
    print()
    print('A add and keep B:')
    cont = 0
    for i in range(0, mD):       
        for j in range(0, nD):   
            if i != cont:
                print('')
                print('%3.f'%(D[i][j]), end = '')
                cont = i
            else:
                print('%3.f'%(D[i][j]), end = '')
                cont = i

    
def q2():
# Escreva aqui um breve comentário sobre o programa solução da questão 2
# Este programa cria uma matriz quadrada com o tamanho definido pelo usuário no conjunto(1-8)
# depois atribui valores pseudo aleatórios a ela, depois cria outras 3 com operações comuns 
# em matrizes e as exibe na tela
# 
# Escreva o código para a resolução da questão 1 abaixo
# Os comandos devem estar alinhados (mesma coluna) do comando import

    import random

    dim = int(input('Entre com a dimensão da matriz quadrada (3-8): ')) # leitura da dimensão da matriz

    while dim < 3 or dim > 8:
        print('Valor inválido!!!')
        dim = int(input('Entre com a dimensão da matriz quadrada (3-8): '))

    m = dim         # m =  # numero de linhas
    n = dim         # n =  # numero de colunas

    # inicializa semente aleatória
    np.random.seed( 0 )
    # gerar uma matriz A de valores inteiros aleatórios 0.0 - 10.0
    A = np.empty((m, n))

    for i in range (0, m):
        for j in range (0, n) :
            A[i][j] = 10*random.random() # gera um valor entre 0.0 e 10.0
            
    B = np.empty((m, n))    # Matriz Diagonal Superior

    for i in range (0, m):
        for j in range (0, n):
            B[i][j] = A[i][j]

    C = np.empty((m, n))    # Matriz Diagonal Inferior

    for i in range (0, m):
        for j in range (0, n):
            C[i][j] = A[i][j]

    D = np.empty((m, n))    # Matriz Diagonal

    for i in range (0, m):
        for j in range (0, n):
            D[i][j] = A[i][j]

    #Manitpulação das matrizes

    for i in range (0, m):
        for j in range (0, n):
            if i > j:
                B[i][j] = 0

    for i in range (0, m):
        for j in range (0, n):
            if i < j:
                C[i][j] = 0

    for i in range (0, m):
        for j in range (0, n):
            if i != j: 
                D[i][j] = 0

    # Área dos prints

    print()
    print('Matriz A:',41*' ','Matriz Diagonal Superior:')

    cont = 1
    esp = ' '

    for i in range (0, m):
        for j in range (0, n):
            if cont < n:
                if j == 0:
                    print('  %3.1f '%(A[i][j]), end = '')
                    cont += 1
                else:
                    print(' %2.1f '%(A[i][j]), end = '')
                    cont += 1
            else:
                print(' %2.1f'%(A[i][j]), (51-(n*5))*esp, end='')
                cont = 1
                for k in range (0, n):
                    
                    if cont < n:
                        print(' %2.1f '%(B[i][k]), end = '')
                        cont += 1
                    else:
                        print(' %2.1f '%(B[i][k]))
                        cont = 1
                cont = 1

    print()
    print('Matriz Diagonal Inferior:',25*' ','Matriz Diagonal:')

    cont = 1
    esp = ' '

    for i in range (0, m):
        for j in range (0, n):
            if cont < n:
                if j == 0:
                    print('  %3.1f '%(C[i][j]), end = '')
                    cont += 1
                else:
                    print(' %2.1f '%(C[i][j]), end = '')
                    cont += 1
            else:
                print(' %2.1f'%(C[i][j]), (51-(n*5))*esp, end='')
                cont = 1
                for k in range (0, n):
                    
                    if cont < n:
                        print(' %2.1f '%(D[i][k]), end = '')
                        cont += 1
                    else:
                        print(' %2.1f '%(D[i][k]))
                        cont = 1
                cont = 1



