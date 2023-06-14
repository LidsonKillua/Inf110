# Nome: Lidson Oliveira
# Matrícula: 102961
# Data: 29/10/2020
 
def q1(): 		   
# Escreva aqui um breve comentário sobre o programa solução da questão 1 
# Este programa calcula a soma dos N primeiros termos da série de Fibonacci e,
# se o usuário pedir, mostra estes elementos.
#    
# Escreva o código para a resolução da questão 1 abaixo
# Os comandos devem estar alinhados (mesma coluna) do comando print()
    #print('solução da questão 1') # apague/comente este comando antes de entregar ! 

    print('Este programa calcula a soma dos N primeiros termos da série de Fibonacci.')
    print()

    n = int(input('Informe o número de elementos (N >= 3): '))

    while n < 3:
        print('N deve ser >= 3')
        n = int(input('Informe o número de elementos (N >= 3): '))

    d = input('Deseja ver todos os elementos (S/N): ')
    print()

    s = 1
    fb = '0 1 '
    e1 = 0
    e2 = 1

    for i in range(2,n):
        e = e1+e2
        fb += ('%.d '%e)
        s += e
        e1 = e2
        e2 = e
        
    if d == 's' or d == 'sim' or d == 'S' or d == 'SIM':
        print('Fibonacci: '+fb)
        
    print('A soma dos %.d primeiros elementos da série de Fibonacci é: %.d.'%(n,s))

def q2():
# Escreva aqui um breve comentário sobre o programa solução da questão 2
# Este programa calcula PI utilizando a série de Nilakantha, mostra os valores calculados com cada
# elemento até um valor específicado pelo usuário, além de mostrar o erro para o valor conhecido de PI
# 
# Escreva o código para a resolução da questão 1 abaixo
# Os comandos devem estar alinhados (mesma coluna) do comando PIc8 = 3.14159265
 
    PIc8 = 3.14159265 # valor de PI com 8 casas decimais
    print('Cálculo de PI usando a série de Nilakantha')
    exnov = 's'
    som = 0
    while exnov == 's' or exnov == 'sim' or exnov == 'S' or exnov == 'SIM':
        print()
        
        n = int(input('Informe o número de elementos da série (N >= 1): '))
        
        while n < 1:
            print('N deve ser >= 1')
            print()
            n = int(input('Informe o número de elementos da série (N >= 1): '))
        
        for i in range(1,n+1):
            if i == 1:
                pi = 3
                err = abs(pi-PIc8)
                print()
                print('  N    PI Calculado      Erro')
                print('%3.d     %6.8f     %7.8f'%(i, pi, err))
                
            else:
                som = 0
                for j in range(1, i):
                    som += ((-1)**(j+1))*4/((2*j)*((2*j)+1)*((2*j)+2))
                    
                pi = 3+som
                err = abs(pi-PIc8)
                print('%3.d     %6.8f     %7.8f'%(i, pi, err))
        
        exnov = input('Deseja executar novamente ? (S/N): ')
    

