# Nome: Lidson Oliveira
# Matrícula: 102961
# Data: 12/11/2020
 
def q1(): 		   
# Escreva aqui um breve comentário sobre o programa solução da questão 1 
# Este programa gera uma tabela formatada com 128 símbolos da tabela ASCII
#    
# Escreva o código para a resolução da questão 1 abaixo
# Os comandos devem estar alinhados (mesma coluna) do comando print()
    #print('solução da questão 1') # apague/comente este comando antes de entregar ! 

    import numpy as np
    
    print()
    print('Tabela ASCII - Caracteres Visíveis')
    print()
    for i in range(0,6):
        print('Dec Sinal   ',end='')
    print()

    matriz = np.empty((16,6),dtype=int)
    char = np.empty((16,6),dtype=str)

    a = 32

    for j in range(0,6):
        for i in range(0,16):
            matriz[i][j] = a
            a += 1

    a = 32

    for j in range(0,6):
        for i in range(0,16):
            char[i][j] = chr(a)
            a += 1
        
    cont = 1

    for i in range(0,16):
        for j in range(0,6):
            if cont < 6:
                if i != 0 and j != 0:
                    print('%3.d %3s     '%(matriz[i][j], char[i][j]), end='')
                    cont+=1
                elif i == 0 and j == 0:
                    print('%3.d %s  '%(matriz[i][j], 'espaço'), end='')
                    cont+=1
                else:
                    print('%3.d %3s     '%(matriz[i][j], char[i][j]), end='')
                    cont+=1
            else:
                print('%3.d %3s     '%(matriz[i][j], char[i][j]))
                cont = 1
    
 
def q2():
# Escreva aqui um breve comentário sobre o programa solução da questão 2
# Esse programa criptografa uma frase dada pelo usuario de duas formas e depois
# decifra, além disso motra as três
#
# Escreva o código para a resolução da questão 1 abaixo
# Os comandos devem estar alinhados (mesma coluna) do comando print
 
    #print('solução da questão 2') # apague/comente este comando antes de entregar !
    
    import numpy as np

    while True:
        print()
        frase = input('Digite uma frase: ')
        chave = int(input('Entre com o valor da chave (1-50): '))


        chFix = np.empty((len(frase)), dtype=str)
        cpVar = np.empty((len(frase)), dtype=str)
        texDec = np.empty((len(frase)), dtype=str)

        for i in range(0,len(frase)):
            chFix[i] = (chr(ord(frase[i]) + chave))
            
        chVar = chave
        for i in range(0,len(frase)):
            cpVar[i] = (chr(ord(frase[i]) + chVar))
            chVar += 2

        rang = len(frase)
        frase = ''

        for i in range(0,rang):
            texDec[i] = (chr(ord(cpVar[i]) - chVar + (2*rang))) 
            chVar += 2

        CF = ''
        CV = ''
        TD = ''

        for i in chFix:
            CF += i
            
        for i in cpVar:
            CV += i

        for i in texDec:
            TD += i

        print()
        print('Chave Fixa: %s'%CF)
        print('Chave var.: %s'%CV)
        print('Frase dec.: %s'%TD)

        en = input('Executar novamente (S/N)? : ')

        if en == 'S' or en == 'sim' or en == 's' or en == 'SIM':
            variavelinutilsopraverificacao = 1
        else:
            break



