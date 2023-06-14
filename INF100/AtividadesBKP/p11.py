# Nome:
# Matrícula:
#
# Comentários obrigatórios devem ser feitos NAS FUNÇÕES QUE VOCÊ IMPLEMENTAR
# SEGUINDO O MODELO ABAIXO, NAS FUNÇÕES leiaInt() e exibeMatriz()

# numpy é usada pelo programa principal e outras funções

##################################################################
#     Não altere o programa deste ponto até o PONTO 1            #
##################################################################
import numpy as np

# Nome: leiaInt
# Tarefa: Lê um valor inteiro na faixa [linf, lsup] 
# Parâmetros de entrada:
#   msg: mensagem solicitando o valor (string)
#   linf: limite inferior da faixa (inteiro)
#   lsup: limite superior da faixa (inteiro)
#   msgErro: mensagem de erro quando valor fora da faixa (string)
#   exibir: define a exibição (ou não) da mensagem de erro (boolean)
# Retorna:
#   valor lido na faixa [linf, lsup] (inteiro)
def leiaInt(msg, linf, lsup, msgErro, exibir=True) :
        x = int(input(msg))
        while x < linf or x > lsup :
            if exibir :
                print(msgErro)
            x = int(input(msg))
        return x

# Nome: exibeMatriz
# Tarefa: mostra na tela os elementos de uma matriz, organizando-os em linhas
#         e colunas
# Parâmetros de entrada:
#    matriz: nome da matriz a ser exibida (endereço do arranjo bidimensional)
#    msg: mensagem a ser impressa como cabeçalho da matriz (string)
# Retorna:
#    NÃO retorna valor
def exibeMatriz(matriz, msg) :
    print(msg)
    m, n = np.shape(matriz) # retorna o número de linhas e colunas da matriz
    for i in range (0, m):
        for j in range(0, n):
            print('%5d' %matriz[i][j], end='')
        print()
    return

# Nome: exibeMenu
# Tarefa: Faz a exibição das opções disponíveis para o usuário
# Parâmetros de Entrada:
#    Nenhum
# Retorna:
#    NÃO retorna valor
def exibeMenu() :   
    print('\n(1) - Exibir soma das matrizes: A + B')
    print('(2) - Exibir subtração das matrizes: A - B')
    print('(3) - Exibir subtração das matrizes: B - A')
    print('(4) - Exibir multiplicação das matrizes A x B')
    print('(5) - Exibir multiplicação das matrizes B x A')
    print('(6) - Exibir a Transposta de A')
    print('(7) - Exibir a Transposta de B')
    print('(0) - Encerrar o programa')
    return

# Nome: clear
# Tarefa: limpa a tela do shell
# Parâmetros de Entrada:
#    Nenhum
# Retorna:
#    NÃO retorna valor
def clear():
    lines = 30
    print("\n" * lines)

# inclua os comentários 
def leDimensoesMatriz(nome, lim_inf, lim_sup) :
    str1 = 'Número de linhas da Matriz '+nome+' ('+str(lim_inf)+'-'+str(lim_sup)+'): '
    str2 = 'Número de colunas da Matriz '+nome+' ('+str(lim_inf)+'-'+str(lim_sup)+'): '
    lin = leiaInt(str1, lim_inf, lim_sup, 'Valor inválido!!!')
    col = leiaInt(str2, lim_inf, lim_sup, 'Valor inválido!!!')
    return lin, col

#####################################################################
#   Ponto 1 - não mexa em nenhuma linha de código ACIMA deste ponto #
#####################################################################

# Defina aqui a função para somar duas matrizes #

# Defina aqui a função para subtrair duas matrizes #

# Defina aqui a função para multiplicar duas matrizes #

# Defina aqui a função para imprimir a Transposta de uma matriz #

    
# programa principal
print('Seja bem vindo! Este programa cria 2 matrizes de números inteiros e')
print('permite que o usuário selecione operações a serem realizadas com elas')
# inclua aqui os comandos para a utilização da função leDimensoesMatriz
# para determinar o número de linhas (mA) e número de colunas (nA) da matriz A 


# inclua aqui os comandos para a utilização da função leDimensoesMatriz
# para determinar o número de linhas (mB) e número de colunas (nB) da matriz B 



##################################################################
#       NÃO altere as linhas de código abaixo deste ponto        #
##################################################################
# iniciar gerador de números aleatórios para que os valores sejam
# OS MESMOS sempre que o programa for executado.
np.random.seed( 0 )
# gerar as matrizes A com dimensões mA x nA e
# B com dimensões mB x nB. Cada matriz terá valores inteiros
# aleatórios no intervalo [-5, 5]
A = np.random.randint( -5, 6, (mA, nA) )
B = np.random.randint( -5, 6, (mB, nB) )
while True:
    clear()      # limpa a tela
    exibeMenu()  # exibe o menu para o usuário
    # selecionar opção
    op = leiaInt('Selecione a opção desejada (1-7) ou 0 para terminar: ', 0, 7, 'Opção é inválida')
    if op != 0 : # irá executar um das 7 opções
        if op >=1 and op <= 5 : # opções 1 a 5 tem que exibir A e B
            exibeMatriz(A, '\nMatriz A: ')
            exibeMatriz(B, '\nMatriz B: ')
            if op == 1 :
                soma(A, B, '\nA + B') 
            elif op == 2 :
                subtrai(A, B, '\nA - B')
            elif op == 3 :
                subtrai(B, A, '\nB - A')
            elif op == 4 :
                multiplica(A, B, '\nA x B')
            else :
                multiplica(B, A, '\nB x A')    
        elif op == 6: # opção 6 exibe apenas A (e sua transposta)
            exibeMatriz(A, '\nMatriz A: ')
            transposta(A, '\nTransposta de A')
        else :        # opção 7 exibe apenas B (e sua transposta)
            exibeMatriz(B, '\nMatriz B: ')
            transposta(B, '\nTransposta de B')
    else :
        break
    # pausa para que o usuário possa ver o resultado
    resp = input('Tecle Enter para continuar!')      
print('\nObrigado por usar nosso programa!!!')

      


      
