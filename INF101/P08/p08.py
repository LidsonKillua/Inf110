# p08.py
# Nome: Lidson Oliveira 
# Matrícula: 102961
# Data: 25/03/2021
# Atualização: 25/03/2021
# Este programa recebe uma data e retorna a data acrescida de um dia de acordo com o
# calendário gregoriano

def main():
    while True:
        linha = input('\nEntre com uma data (dd mm aaaa):\n')
        dia, mes, ano = tuple(map(int, linha.split(' ')))
        dia1, mes1, ano1 = adicione_1dia(dia, mes, ano)
        print('O dia seguinte é {:02d}/{:02d}/{:4d}.'.format(dia1, mes1, ano1))
        resp = input('Deseja continuar (s/n)? ')
        if resp == 'n' or resp == 'N': break

# Implemente aqui a função bissexto(a).

def bissexto(a):

    if a % 400 == 0: # Como as datas teóricamente serão maiores que 1582 e
        return True  # 1582 > 400 farei essa divisão direto
    else:
        return False


# Implemente aqui a função num_dias_no_mes(m, a).

def num_dias_no_mes(m, a):

    if bissexto(a):
        numDiasMes = 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 
    else:
        numDiasMes = 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31        

    return numDiasMes[m - 1]

    # Criei duas tuplas pois foi dito que tuplas são executadas mais
    # rapido que lista, e como o if já está na criação da lista acredito que não há
    # impacto retirar dele, o problema é que o programa aumentou em 2 linhas hehe

# Implemente aqui a função adicione_1dia(d, m, a).    

def adicione_1dia(d, m, a):
    
    if 1 <= d <= 31 and 1 <= m <= 12 and a > 1582:

        if d == num_dias_no_mes(m, a):
            d = 1
            if m == 12:
                m = 1
                a += 1
            else:
                m += 1
        else:
            d += 1

    return d, m, a

main()
