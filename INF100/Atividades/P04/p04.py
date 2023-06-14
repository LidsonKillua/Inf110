# Nome: Lidson Oliveira 
# Matrícula: 102961
# Data: 08/10/2020
 
def q1(): 		   
# Escreva aqui um breve comentário sobre o programa solução da questão 1 
# Esse programa lê o nome e temperaturas mínima e máxima de uma cidade e retorna 
# sua amplitude térmica e média em °C e Fahrenheit, além disso faz a verificação 
# da temperatura mínima e dá um aviso caso seja maior que a máxima
#
# Escreva o código para a resolução da questão 1 abaixo
# Os comandos devem estar alinhados (mesma coluna) do comando print()
    #print('solução da questão 1') # apague/comente este comando antes de entregar ! 

    c = input('Informe o nome da cidade: ')   
    tmax = float(input('Informe o valor da temperatura máxima (°C): '))
    tmin = float(input('Informe o valor da temperatura mínima (°C): '))

    while tmin > tmax :
        print('A temperatura mínima não pode ser maior que a máxima')
        tmin = float(input('Informe o valor da temperatura mínima (°C): '))

    ampli = tmax-tmin
    tmed = (tmax+tmin)/2
    ftmin = (9*(tmin)/5)+32    
    ftmax = (9*(tmax)/5)+32   
    ftmed = (ftmax+ftmin)/2   
    fampli = ftmax-ftmin

    print('')
    print('Em {} as condições de temperatura foram: '.format(c))
    print('')
    print('                  Mínima  Máxima  Média  Amplitude')
    print('Graus Celsius %10.1f %7.1f %6.1f %10.1f'%(tmin, tmax, tmed, ampli))
    print('Graus Fahrenheit %7.1f %7.1f %6.1f %10.1f'%(ftmin, ftmax, ftmed, fampli))

def q2():
# Escreva aqui um breve comentário sobre o programa solução da questão 2
# Este programa calcula o valor do elemento da posição N e a soma dos N
# primeiros números de uma Progressão Aritmética, além de mostrar essa PA.
#
# Escreva o código para a resolução da questão 1 abaixo
# Os comandos devem estar alinhados (mesma coluna) do comando print()q1
    #print('solução da questão 2') # apague/comente este comando antes de entregar ! 

    print('Este programa calcula o valor do elemento da posição N e a soma')
    print('dos N primeiros números de uma Progressão Aritmética (PA)')
    print()
    
    a1 = float(input('Informe o valor do primeiro elemento da PA: '))
    r = float(input('Informe o valor da razão da PA: '))
    n = int(input('Informe o valor de N: '))
    c = 1
    sn = 0
    pa = ''
    
    while c < n:
        an = a1 + (c-1)*r
        pa = pa+('%.3f'%(an))+', '
        sn = sn+an                  # Soma não vai ser feita pela fórmula pois
        c += 1                      # o roteiro pediu pra fazer a soma a medida     
                                    # que os valores são gerados.
    an = a1 + (n-1)*r
    pa = pa+('%.3f'%an)
    sn = sn+an
    
    print()
    print('PA = {'+pa+'}')
    print()
    print('O {}° elemento da PA é = %.3f'.format(n)%an)
    print('A soma dos {} primeiros elementos é = %.3f'.format(n)%sn)













