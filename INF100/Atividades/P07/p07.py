# Nome: Lidson Oliveira
# Matrícula: 102961
# Data: 05/11/2020

# Escreva aqui um breve comentário sobre o programa
# Este programa gera uma lista com valores pseudo aleatórios e mostra entre eles
# qual é o maior, quantas vez ele aparece e a média, além disso deixa o usuário escolher um
# valor para ver quantas vezes ele aparece nessa lista.
#

import numpy as np
# preencha os valores das variáveis linf e lsup conforme o roteiro da
# sua turma prática
linf = 75733
lsup = 103124

print('Criando um arranjo com 6.000 posições')
print('Valores no intervalo %d a %d. '%(linf, lsup))
# definição do tamanho do arranjo
N = 6000
# iniciar gerador de números (pseudo)aleatórios para que os valores sejam
# OS MESMOS sempre que o programa for executado.
np.random.seed( 0 )

# gera um arranjo de nome numeros inteiros na faixa de matrículas do horário
numeros = np.random.randint(linf, lsup+1, (N), dtype=int )

# inicialização das variáveis para guardar o menor elemento e o
# somatório de todos os elementos
maior = linf-1
soma = 0

# percorre todo o arranjo, da posição 0 até a posição N
for i in range(0, N) :
    # atualização do somatório
    soma += numeros[i]

    # teste para verificar se a posição i do arranjo é o
    # maior valor e/ou atualização do número de vezes
    # que o maior valor aparece
    if numeros[i] > maior :
        maior = numeros[i]
        nv = 1
    elif numeros[i] == maior:
        nv = nv + 1 
    
# cálculo da média
media = soma/N

# impressão dos resultados (média, maior valor, número de vezes que o maio
# valor aparece

print()
print('A média dos valores é %.0f'%media)
print('O maior valor %.0f aparece %.0f vez(es).'%(maior, nv))
print()

while True : #no input eu coloquei 'entre' ao invés de 'ente' como no exeplo do roteiro por que acho que o roteiro está errado
    v = int(input('Entre com um valor entre %.0f e %.0f ou 0 para terminar: '%(linf,lsup)))  # leitura do valor
    # teste do valor lido e definição das 3 tarefas:
    # 1) terminar o programa
    # 2) informar quantas vezes o valor aparece no arranjo
    # 3) informar que o valor não pertence à faixa
    if v == 0:
        break
    elif v < linf or v > lsup:
        print('Este valor está fora da faixa de valores gerados.')
    else:
        quantidade = 0
        for g in numeros:
            if g == v:
                quantidade += 1
        
        print('O valor %.0f aparece %.0f vez(es).'%(v, quantidade))
    
    
    
   
