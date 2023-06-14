# Nome do aluno: Lídson Oliveira    
# Matrícula: 102961
# Data: 10/09/2020
 
def q1(): 		   
# Escreva aqui um breve comentário sobre o programa solução da questão 1 
# Esse programa lê o nome e temperaturas mínima e máxima de uma cidade e retorna 
# sua amplitude térmica e média em °C e Fahrenheit
#
# Escreva o código para a resolução da questão 1 abaixo
# Os comandos devem estar alinhados (mesma coluna) do comando print()
    print('Solução da questão 1')

    c = input('Informe o nome da cidade: ')   
    tmax = float(input('Informe o valor da temperatura máxima(°C): '))
    tmin = float(input('Informe o valor da temperatura mínima(°C): '))
    ampli = tmax-tmin
    tmed = (tmax+tmin)/2
    ftmin = (9*(tmin)/5)+32    
    ftmax = (9*(tmax)/5)+32   
    ftmed = (ftmax+ftmin)/2   
    fampli = ftmax-ftmin

    print('Em {} as condições de temperatura foram: '.format(c))
    print('')
    print('                  Mínima  Máxima  Média  Amplitude')
    print(' Graus Celsius      %.1f    %.1f   %.1f       %.1f'%(tmin, tmax, tmed, ampli))
    print(' Graus Fahrenheit   %.1f    %.1f   %.1f       %.1f'%(ftmin, ftmax, ftmed, fampli))
 
def q2():
# Escreva aqui um breve comentário sobre o programa solução da questão 2
# O programa abaixo realiza duas operações básicas com uma progreção aritmética gerada a partir do input do usuário
#
# Escreva o código para a resolução da questão 1 abaixo
# Os comandos devem estar alinhados (mesma coluna) do comando print()
    print('Solução da questão 2')
    
    print('Este programa calcula o valor do elemento da posição N e a soma dos N primeiros números de uma Progressão Aritmética (PA)')
    a1 = float(input('Informe o valor do primeiro elemento da PA: '))
    r = float(input('Informe o valor da razão da PA: '))
    n = int(input('Informe o valor de N: '))
    an = a1 + (n-1)*r
    sn = n*(a1+an)/2
    
    print('')
    print('O {}° elemento da PA é = %.3f'.format(n)%an)
    print('A soma dos {} primeiros elementos é = %.3f'.format(n)%sn)
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    

