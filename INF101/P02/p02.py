#
# Nome do programador: Lidson Oliveira
# Matrícula: 102961
# Data: 11/02/2021 19:56
# Este programa lê um arquivo .dat com notas, salva as notas em uma lista e
# realiza cálculos a partir dessas notas, a média, desvio padrão, menor e maior
# nota e mostra o resultado ao usuário.
#

import math
import numpy as np

def main():
    nomeArq  = 'notas_inf100.dat'
    arqNotas = open(nomeArq, 'r')
    linhas = arqNotas.read().split('\n')

    notas = np.array(list(map(float, linhas)))

    print('%d notas lidas.' % len(linhas))
    print()
    print('Média das notas:         %5.1f' % media(notas))
    print('Desvio padrão das notas: %5.1f' % desvioPad(notas))
    print('Maior nota:              %5.1f' % maximo(notas))
    print('Menor nota:              %5.1f' % minimo(notas))
    
#
# Insira abaixo a implementação das funções requeridas:
#

def media(notas):
    
    n = len(notas)

    if n > 0:
        
        soma = 0
        
        for i in range(0, n):
            soma = soma + notas[i]
            
        media = (soma)/n
        
        return media

def desvioPad(notas):

    n = len(notas)

    if n > 1:

        m = media(notas)
        soma = 0
        
        for i in range(0, n):
            soma += (notas[i]-m)**2
            
        desvio = math.sqrt(soma/(n-1))

        return desvio

def maximo(notas):
    
    n = len(notas)
    
    if n > 0:        
        maximo = 0
        
        for i in range(0, n):
            if notas[i] > maximo:
                maximo = notas[i]      

    return maximo
    
def minimo(notas):
    
    n = len(notas)
    if n > 0:
        minimo = 100
        
        for i in range(0, n):
            if notas[i] < minimo:
                minimo = notas[i]      

        return minimo

if __name__ == '__main__':
    main()









    
