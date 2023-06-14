# Nome do aluno: Lidson Oliveira
# Matrícula: 102961
# Data: 01/10/2020


def q1():
    # Escreva aqui um breve comentário dizendo o que o programa 1 faz
    # O programa utiliza uma tabela como base para calcular a alíquota de
    # contribuição do INSS sobre o salário dado pelo usuário.
    #
    # Escreva o código para a resolução da questão 1 abaixo
    # limite entre faixas com alíquotas do INSS
    lim1 = 1045.00
    lim2 = 2089.60
    lim3 = 3134.40
    lim4 = 6101.06
    # alíquotas por faixa
    al1 = 0.075
    al2 = 0.09
    al3 = 0.12
    al4 = 0.14

    sb = float(input('Informe o valor do salário bruto: '))

    if sb <= lim1:
        c = sb*al1
        
    elif sb <= lim2:
        c = (lim1*al1)+((sb-lim1)*al2)
        
    elif sb <= lim3:
        c = (lim1*al1)+((lim2-lim1)*al2)+((sb-lim2)*al3)
        
    elif sb <= lim4:
        c = (lim1*al1)+((lim2-lim1)*al2)+((lim3-lim2)*al3)+((sb-lim3)*al4)

    else:
        c = (lim1*al1)+((lim2-lim1)*al2)+((lim3-lim2)*al3)+((lim4-lim3)*al4)
        
    sf = sb-c
    alqef = (100-((sf*100)/sb))

    print('')
    print('Salário Bruto: %15.2f'%sb)
    print('Contribuição INSS: %11.2f'%c)
    print('Salário menos INSS: %10.2f'%sf)
    print('Alíquota efetiva (INSS): %4.1f%%'%alqef)
      
def q2():
    # Escreva aqui um breve comentário dizendo o que o programa 2 faz
    # O programa 2 recebe o salário do usuário com o INSS descontado e 
    # calcula o imposto de renda com base em uma tabela e utilizando
    # uma base de cálculo com dedução por quantidade de dependentes,
    # também informado pelo usuário.
    #
    # Escreva o código para a resolução da questão 2 abaixo

    # dedução por dependente
    dpd = 189.59
    # alíquotas do imposto de renda
    alir1 = 0.075
    alir2 = 0.15
    alir3 = 0.225
    alir4 = 0.275
    # limite superior das faixas
    limir1 = 1903.98   # isenção
    limir2 = 2826.65   # 7,5%
    limir3 = 3751.05   # 15.0%
    limir4 = 4664.68   # 22.5
    # a faixa de 27,5% não tem limite superior
    print('Use os valores calculados no programa da questão 1')

    sl = float(input('Informe o valor do salário sem INSS: '))   #saldo líquido(sem INSS)
    dep = int(input('Informe o número de dependentes: '))        #número de dependentes

    ddt = (dep*dpd)    # desconto de dependentes total
    bcir = (sl-ddt)    # base de cálculo do IR

    if bcir < 0:               # tratamento pro caso da base de cálculo menor que 0
        bcir = 0                 
        valir = (bcir*0)    

    else:    
        if bcir <= limir1:
            valir = (bcir*0)
        
        elif bcir <= limir2:
            valir = ((bcir-limir1)*alir1)
        
        elif bcir <= limir3:
            valir = (((limir2-limir1)*alir1)+(bcir-limir2)*alir2)
        
        elif bcir <= limir4:
            valir = (((limir2-limir1)*alir1)+((limir3-limir2)*alir2)+(bcir-limir3)*alir3)

        else:
            valir = (((limir2-limir1)*alir1)+((limir3-limir2)*alir2)+((limir4-limir3)*alir3)+(bcir-limir4)*alir4)
            
    sf = sl-valir
    alqefir = (100-((sf*100)/sl))    

    print('')
    print('Salário sem INSS: %10.2f'%sl)
    print('Desconto dependentes: %6.2f (%1.d dependente(s))'%(ddt, dep))
    print('Base de Cálculo: %11.2f'%bcir)
    print('Valor a pagar IR: %10.2f'%valir)
    print('Alíquota efetiva (IR): %4.1f%%'%alqefir)




