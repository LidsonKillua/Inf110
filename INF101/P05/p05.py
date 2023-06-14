# p05.py
# Autor: Lidson Oliveira
# Matrícula: 102961
# Data: 04/03/2021
# Esse programa ordena uma lista de forma crescente usando um algorítimo de seleção direta

def ordena(lista):

    for h in range(0,len(lista)):
        j = minimo(lista, h)
        lj = lista[j]
        lista[j] = lista[h]
        lista[h] = lj

def minimo(lista, indice):

    ref = max(lista)+1
    # ref = Valor do usuário
    # ref = 99999999
    '''
    Assim com a função max + 1 eu garanto que funcionará para qualquer valor na lista, Mas
    claro que em outra linguagem em que isso não exista eu poderia implementar o max para
    começar de 0 ou usar uma referência dada pelo usuário para ter um valor alto o suficiente.
    '''
    j = 0
    for i in range(indice,len(lista)):
        if lista[i] < ref:
            ref = lista[i]
            j = i
    return j

def main():

    lista = [36, 18, 43, 9, 18, 25, 14]
    
    ordena(lista)
    
    print(lista)

main()








