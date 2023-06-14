# p06.py
# Autor: Lidson Oliveira
# Matrícula: 102961
# Data: 11/03/2021
# Este programa gerencia duas filas de banco por meio de quatro operações mais uma operação
# de saída, dadas pelo usuário por meio de uma série de caracteres.

def leiaOperacoes():
    
    print('\nDigite a sequência de operações a ser feitas:',
          '\nF para adicionar um cliente na fila 1',
          '\nG para adicionar um cliente na fila 2',
          '\nA para atender cliente na fila 1',
          '\nB para atender cliente na fila 2',
          '\nS para sair da simulação')
    
    op = input().upper()
    return op
    
def simule(n, opers):

    if n % 2 == 0:
        met = int(n/2)
        fila1 = list(range(1,met+1))
        fila2 = list(range(met+1,n+1))
    else:
        met = int(n//2)
        fila1 = list(range(1,met+1))
        fila2 = list(range(met+1,n+1))

    print('\nExistem %d clientes na fila 1.'%(len(fila1)))
    print('Fila 1 atual: ', fila1)
    print('Existem %d clientes na fila 2.'%(len(fila2)))
    print('Fila 2 atual: ', fila2)
        
    for op in opers:
        if op == 'F':
            print('\n==> Operação: %s'%op)
            n += 1
            fila1.append(n) 

        elif op == 'G':
            print('\n==> Operação: %s'%op)
            n += 1
            fila2.append(n)

        elif op == 'A':
            print('\n==> Operação: %s'%op)
            cli = fila1.pop(0)
            print('Cliente %d atendido.'%cli)

        elif op == 'B':
            print('\n==> Operação: %s'%op)
            cli = fila2.pop(0)
            print('Cliente %.d atendido.'%cli)

        elif op == 'S':
            print('\n==> Operação: %s'%op)
            break

        else:
            print('\n==> Operação: %s'%op)
            print('Operação inválida! Digite apenas F, G, A, B ou S.')
            
        
        print('\nExistem %d clientes na fila 1.'%(len(fila1)))
        print('Fila 1 atual:', fila1)
        print('Existem %d clientes na fila 2.'%(len(fila2)))
        print('Fila 2 atual:', fila2)

    print('\nFim da Simulação.')

def main():

    print('Simulação de duas filas de banco')
    qtdcli = int(input('Quantos clientes serão inicialmente? '))

    operacoes = leiaOperacoes()
    simule(qtdcli, operacoes)
    


main()








