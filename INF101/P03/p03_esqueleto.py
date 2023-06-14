# p03.py
# Autor: Lidson Oliveira
# Matrícula: 102961
# Data: 18/02/2021
# Atualização: ??
# Esse programa simula um jogo de campo minado, baseado em funções e matrizes

import numpy as np
import random
from termcolor import colored

def imprimeTabuleiroSimples(tabuleiro) :
  # print sem argumentos imprime uma linha vazia
  print()
  
  # Funcao len de um array 2D pega o número de linhas, exemplo len(arr)
  # Funcao len da primeira posição de um array 2D pega o número de colunas,
  # exemplo len(arr[0])
  for i in range(len(tabuleiro)) :
    print('| ', end='')
    for j in range(len(tabuleiro[0])) :
      print('{:2d}'.format(tabuleiro[i][j]), end=' ')
    print('|')

  # print sem argumentos imprime uma linha vazia
  print()


def imprimeTabuleiro ( tabuleiro ) :

  # print sem argumentos imprime uma linha vazia
  print()
  
  # Funcao len de um array 2D pega o número de linhas, exemplo len(arr)
  # Funcao len da primeira posição de um array 2D pega o número de colunas,
  # exemplo len(arr[0])
  for i in range(len(tabuleiro)) :
    for j in range(len(tabuleiro[0])) :
      if tabuleiro[i][j] == -1 :
        print(colored('B','red'), end=' ')
      elif tabuleiro[i][j] == 0 :
        print(colored('█','grey'), end=' ')
      else :
        print(colored(tabuleiro[i][j],'cyan'), end=' ')
    print()

  # print sem argumentos imprime uma linha vazia
  print()


def sorteiaPosicao(tabuleiro, semente=None) :
  if semente is not None:
    random.seed(semente)
  while True :
    i = random.randint(0, len(tabuleiro) - 1)
    j = random.randint(0, len(tabuleiro[0]) - 1)
    if tabuleiro[i][j] != -1 :
      break
  return i, j


# Inicializa com zeros um tabuleiro de tamanho definido.
# Coloque sua implementação aqui.
def inicializaTabuleiro(linhas, colunas=-1) :

    m = np.zeros((linhas, colunas), dtype = int)
    return m

# Coloque sua implementação aqui.
def posicionaBombas(quantidade, tabuleiro, semente=None) :

    t = 0
    while t < quantidade:
        i, j = sorteiaPosicao(tabuleiro, semente)
        tabuleiro[i][j] = -1
        t += 1

# Coloque sua implementação aqui.
def calculaTabuleiro(tabuleiro) :
    tab = tabuleiro #variável local de nome menor com o caminho de memória para facilitar a digitação
    t = len(tab) #como ele é uma matriz quadrada posso usar apenas um tamanho
    for i in range(0, t):
        for j in range(0, t):

            if tab[i][j] != -1:
                
                if i-1 < 0:     #Verificações para não deixar o range dos indices sair da matriz
                    k = 0
                else:
                    k = i-1

                if i+1 >= t:
                    l = t-1
                else:
                    l = i+1

                if j-1 < 0:
                    s = 0
                else:
                    s = j-1

                if j+1 >= t:
                    p = t-1
                else:
                    p = j+1

                cont = 0
                    
                for m in range(k, l+1):
                    for n in range(s, p+1):                
                        if tab[m][n] == -1:
                            cont += 1
                                
                    tab[i][j] = cont
   

def main(numero_linhas, numero_colunas, numero_bombas) :
  tabuleiro = inicializaTabuleiro( numero_linhas, numero_colunas )
  posicionaBombas(numero_bombas, tabuleiro, 111)
  imprimeTabuleiroSimples(tabuleiro)
  calculaTabuleiro(tabuleiro)
  imprimeTabuleiroSimples(tabuleiro)


numero_linhas = 8
numero_colunas = 8
numero_bombas = 10

main(numero_linhas, numero_colunas, numero_bombas)
