# p08.py
# Nome: 
# Matrícula: 
# Data: 25/03/2021
# Atualização: 25/03/2021
# (Descreva sucintamente o que o programa faz.)

def main():
    while True:
        linha = input('\nEntre com uma data (dd mm aaaa):\n')
        dia, mes, ano = tuple(map(int, linha.split(' ')))
        dia1, mes1, ano1 = adicione_1dia(dia, mes, ano)
        print('O dia seguinte é {:02d}/{:02d}/{:4d}.'.format(dia1, mes1, ano1))
        resp = input('Deseja continuar (s/n)? ')
        if resp == 'n' or resp == 'N': break

# Implemente aqui a função bissexto(a).



# Implemente aqui a função num_dias_no_mes(m, a).



# Implemente aqui a função adicione_1dia(d, m, a).    



main()
