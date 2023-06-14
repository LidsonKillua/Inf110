# p04.py
# Autor: Lidson Oliveira
# Matrícula: 102961
# Data: 25/02/2021
# Este programa adiciona notas a um arranjo com tamanho pré definido e mostra no fim
# essas notas filtradas em um período específico(a<x<b)

import numpy as np

def leiaNotas(vmin, vmax, tam_max):

    notas = np.zeros(tam_max, dtype = int)
    i = 0 #índice, já que não vou usar for
    
    print('Entre com uma amostra de notas de 0 a 100 (-1 para terminar): ')

    notatemp = 0
    
    while True:

        notatemp = int(input())
        if notatemp == -1:
            break
        
        while notatemp < vmin or notatemp > vmax:
            print('*** Os valores devem estar entre {} e {}.'.format(vmin, vmax))
            notatemp = int(input())
            if notatemp == -1:
                break
        if notatemp == -1:
                break
            
        notas[i] = notatemp
        i += 1

    return notas

def filtra(notas):

    filtro = ''
    for i in range(0, len(notas)):
        if notas[i] >= 40 and notas[i] <= 70:
            filtro += ('%.d '%notas[i])

    print()
    print('As notas entre 40 e 70 são: ')
    print(filtro)

def main():

    vmin = 0
    vmax = 100
    tammax = 150          #Tamanho do arranjo(quantidade máxima de notas)
    
    notas = leiaNotas(vmin, vmax, tammax)
    filtra(notas)

main()








