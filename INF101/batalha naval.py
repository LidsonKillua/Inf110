import numpy as np
from termcolor import colored

def imprimeTabuleiro ( tabuleiro ) :
  # Cabeçalho de nome das colunas
  print('    ', end='')
  for j in range( len(tabuleiro[0]) ) :
    print( j+1, end=' ' )
  print() 

  # separador vertical -
  print('    ', end='')
  for j in range( len(tabuleiro[0]) ) :
    print( '-', end=' ' )
  print() 

  # impressão de conteúdo formatado
  for i in range( len(tabuleiro) ) :
    print('{} | '.format(chr(i+65)), end='')
    for j in range( len(tabuleiro[0]) ) :

      if tabuleiro[i][j] == 0 :
        print( colored('█', 'blue'), end=' ' )
      elif tabuleiro[i][j] == 1 :
        print( colored('P', 'grey'), end=' ' )
      elif tabuleiro[i][j] == 2 :
        print( colored('C', 'cyan'), end=' ' )
      elif tabuleiro[i][j] == 3 :
        print( colored('c', 'yellow'), end=' ' )
      elif tabuleiro[i][j] == 4 :
        print( colored('r', 'green'), end=' ' )
      elif tabuleiro[i][j] == 9 :
        print( colored('X', 'red'), end=' ' )
    
    print('|')

  # separador vertical -
  print('    ', end='')
  for j in range( len(tabuleiro[0]) ) :
    print( '-', end=' ' )
  print() 

def definirTabuleiro ( tamanho ) :
  tabuleiro = np.zeros( (tamanho, tamanho), dtype=int )
  return tabuleiro

def converterPosicao ( celula ) :
  linha  = int( ord( celula[0].lower() ) ) - 97
  coluna = int( celula[1] ) - 1
  return linha, coluna

def posicionarNavios ( tabuleiro ) :
  # Insere Porta-avião
  celula_inicial = input( 'Qual a célula inicial do Porta-avião: ')
  celula_final = input( 'Qual a célula final do Porta-avião: ')
  i_inicial,j_inicial = converterPosicao(celula_inicial)
  i_final,j_final = converterPosicao(celula_final)
  for i in range( i_inicial, i_final+1 ) :
    for j in range( j_inicial, j_final+1 ) :
      tabuleiro[i][j] = 1

  # Insere Cruzador
  celula_inicial = input( 'Qual a célula inicial do Cruzador: ')
  celula_final = input( 'Qual a célula final do Cruzador: ')
  i_inicial,j_inicial = converterPosicao(celula_inicial)
  i_final,j_final = converterPosicao(celula_final)
  for i in range( i_inicial, i_final+1 ) :
    for j in range( j_inicial, j_final+1 ) :
      tabuleiro[i][j] = 2

  # Insere Contratorpedeiro
  celula_inicial = input( 'Qual a célula inicial do Contratorpedeiro: ')
  celula_final = input( 'Qual a célula final do Contratorpedeiro: ')
  i_inicial,j_inicial = converterPosicao(celula_inicial)
  i_final,j_final = converterPosicao(celula_final)
  for i in range( i_inicial, i_final+1 ) :
    for j in range( j_inicial, j_final+1 ) :
      tabuleiro[i][j] = 3

  # Insere Rebocador
  celula_inicial = input( 'Qual a célula inicial do Rebocador: ')
  celula_final = input( 'Qual a célula final do Rebocador: ')
  i_inicial,j_inicial = converterPosicao(celula_inicial)
  i_final,j_final = converterPosicao(celula_final)
  for i in range( i_inicial, i_final+1 ) :
    for j in range( j_inicial, j_final+1 ) :
      tabuleiro[i][j] = 4

def disparo( tiro, tabuleiro ) :
  i,j = converterPosicao( tiro )
  
  if tabuleiro[i][j] == 0 :
    print('Água') 
  elif tabuleiro[i][j] == 1 :
    print('Porta-avião') 
  elif tabuleiro[i][j] == 2 :
    print('Cruzador') 
  elif tabuleiro[i][j] == 3 :
    print('Contratorpedeiro') 
  elif tabuleiro[i][j] == 4 :
    print('Rebocador') 
  else :
    print('Erro') 
  tabuleiro[i][j] = 9

def jogar ( tabuleiro ) :
  tiro = input( 'Qual a posição do tiro: ')
  while tiro != 'q' :
    disparo( tiro, tabuleiro )
    imprimeTabuleiro( tabuleiro )
    tiro = input( 'Digite q para sair ou\nQual a posição do tiro: ')  
  
def main ( tamanho=8 ) :
  tabuleiro = definirTabuleiro( tamanho )
  imprimeTabuleiro( tabuleiro )
  posicionarNavios( tabuleiro )
  imprimeTabuleiro( tabuleiro )
  jogar( tabuleiro )
  imprimeTabuleiro( tabuleiro )

main()
