# Nome do aluno: Lídson Oliveira    
# Matrícula: 102961
# Data: 24/09/2020


def q1():
    # Escreva aqui um breve comentário dizendo o que o programa 1 faz
    # Este programa lê três números inteiros e os retorna em ordem crescente(do menor para o maior)
    # Escreva o código para a resolução da questão 1 abaixo
    print('solução da questão 1')
    a = int(input('Entre com o primeiro valor: '))
    b = int(input('Entre com o segundo valor: '))
    c = int(input('Entre com o terceiro valor: '))
    print('')   #print para manter a formatação pedida
    
    if a <= b <= c:
        print('A sequência ordenada é: {} {} {}'.format(a, b, c))
    else:
        if a <= c <= b:
            print('A sequência ordenada é: {} {} {}'.format(a, c, b))
        else:
            if b <= a <= c:
                print('A sequência ordenada é: {} {} {}'.format(b, a, c))
            else:
                if b <= c <= a:
                    print('A sequência ordenada é: {} {} {}'.format(b, c, a))
                else:
                    if c <= b <= a:
                        print('A sequência ordenada é: {} {} {}'.format(c, b, a))
                    else:
                        if c <= a <= b:
                            print('A sequência ordenada é: {} {} {}'.format(c, a, b))

def q2():
    # Escreva aqui um breve comentário dizendo o que o programa 2 faz
    # Este programa lê dois valores, um inteiro e um qualquer, caso o segundo valor seja inteiro exibe uma lista de
    # operações com números inteiros e caso seja real exibe uma lista de operações com inteiros e reais. 
    # Escreva o código para a resolução da questão 2 abaixo
    print('solução da questão 2')

    a = int(input('Forneça um valor INTEIRO. A = '))
    b = float(input('Forneça um valor QUALQUER. B = '))
    print('')

    if b == int(b):
        b = int(b)
        soma = a+b
        sub = a-b 
        mult = a*b
        div = a/b 
        exp = a**b
        divint = a//b 
        mod = a%b

        print('As operações aritméticas com inteiros são: ')
        print('')
        print('Matemática      Python         Resultado')
        print('  A + B   =  {}    +    {}  = %7.i'.format(a, b)%soma)
        print('  A - B   =  {}    -    {}  = %7.i'.format(a, b)%sub)
        print('  A * B   =  {}    *    {}  = %7.i'.format(a, b)%mult)
        print('  A ÷ B   =  {}    /    {}  = %7.i'.format(a, b)%div)
        print(' A exp B  =  {}    **   {}  = %7.i'.format(a, b)%exp)
        print(' A div B  =  {}    //   {}  = %7.i'.format(a, b)%divint)
        print(' A mod B  =  {}    %    {}  = '.format(a, b),end='')
        print('{0:7}'.format(mod))
    else:
        soma = a+b
        sub = a-b 
        mult = a*b
        div = a/b 
        exp = a**b
        
        print('As operações aritméticas com inteiro e real são: ')
        print('')
        print('Matemática      Python          Resultado')
        print('  A + B   =  {}    +    %.2f  =  %7.2f'.format(a)%(b, soma))
        print('  A - B   =  {}    -    %.2f  =  %7.2f'.format(a)%(b, sub))
        print('  A * B   =  {}    *    %.2f  =  %7.2f'.format(a)%(b, mult))
        print('  A ÷ B   =  {}    /    %.2f  =  %7.2f'.format(a)%(b, div))
        print(' A exp B  =  {}    **   %.2f  =  %7.2f'.format(a)%(b, exp))
        
    # ÷ 
