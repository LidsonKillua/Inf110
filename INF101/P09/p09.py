# p09.py
# Nome do programador: Lidson Oliveira
# Matrícula: 102961
# Data de criação: 08/04/2021
# Data atualização: 08/04/2021
# Este programa cria um banco de dados com arquivos de funcionarios de
# uma empresa, em seguida calcula o salário bruto de cada um desses
# funcionários baseado em outro arquivo e os retorna para o usuário.
# 

def main():
    funcionarios = leiaFunc('funcionarios.csv')
    salariosBrutos = calcSalBruto('horas_trab.dat', funcionarios)

    # Imprime relatório dos salários brutos de todos os funcionários.
    print("\n***     Relatório dos Salários Brutos     ***"
          "\nMatrícula         Nome          Salário Bruto")
    for i in range(len(funcionarios)):
        print("{:7d}    {:20s}    {:8.2f}".format(funcionarios[i][0],
                                                  funcionarios[i][1],
                                                  salariosBrutos[i]))


def leiaFunc(nomeArq):
    # Abre o arquivo no formato csv contendo os dados dos funcionários:
    # matr,nome,cargo,salPorHora
    arqFuncs = open(nomeArq, 'r')

    # Gera o banco de dados dos funcionarios armazenando-o em uma lista
    # de tuplas.
    bd = []
    linha = arqFuncs.readline().rstrip('\n')
    while linha != '':
        dados = linha.split(',')
        #print(dados)
        matr = int(dados[0])
        nome = dados[1]
        cargo = dados[2]
        salPorHora = float(dados[3])
        bd.append((matr, nome, cargo, salPorHora))
        linha = arqFuncs.readline().rstrip('\n')
    arqFuncs.close()

    return bd

#####                                             #####
# Implemente aqui a função calcSalBruto(nomeArq, bd)  #

def calcSalBruto(nomeArq, bd):
    
    arqHoras = open(nomeArq, 'r')

    i = 0
    salario = []
    linha = arqHoras.readline().rstrip('\n')
    while linha != '':
        horas = linha.split(' ')
        horareg = float(horas[0])      #horas regulares
        horaext = float(horas[1])      #horas extra

        salBruto = (horareg * bd[i][3])+(horaext * 1.5 * bd[i][3])
        
        salario.append(salBruto)
        
        linha = arqHoras.readline().rstrip('\n')
        i += 1
        
    arqHoras.close()

    return salario


#####                                             #####

main()
