# p07.py
# Autor: Lidson Oliveira
# Matrícula: 102961
# Data: 18/03/2021
# Este programa utiliza pilha e regra LIFO para ler expressões e classificá-las de acordo
# com os parênteses.


# Nos casos onde os parênteses for aberto em ordem errada ')(' ele vai acusar
# errado por causa da pilha(como o roteiro não pede o contrário fica assim mesmo)

def main():

    while True:

        expr = input('Digite uma expressão com parênteses (ENTER para terminar): ')
        if expr == '':
            break
        ok = analise_parenteses(expr)

        if ok == True:
            print('{} está OK'.format(expr))
        elif ok == False:
            print('{} está ERRADO'.format(expr))

def analise_parenteses(expr):
    
    pilha = []

    for i in expr:
        if i == '(':
            pilha.append(i)
        elif i == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                return False

    if len(pilha) == 0:
        return True
    else:
        return False
main()
