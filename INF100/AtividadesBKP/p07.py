import numpy as np
# preencha os valores das variáveis linf e lsup conforme o roteiro da
# sua turma prática
linf = 
lsup = 

print('Criando um arranjo com 60.000 posições')
print('Valores no intervalo %d a %d. '%(linf, lsup))
# definição do tamanho do arranjo
N = 60000
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
    

    # teste para verificar se a posição i do arranjo é o
    # maior valor e/ou atualização do número de vezes
    # que o maior valor aparece
    if numeros[i] > maior :
        maior = numeros[i]
        nv = 1
    elif numeros[i] == maior:
        nv = nv + 1 
    
# cálculo da média


# impressão dos resultados (média, maior valor, número de vezes que o maio
# valor aparece



while True :
    # leitura do valor
    # teste do valor lido e definição das 3 tarefas:
    # 1) terminar o programa
    # 2) informar quantas vezes o valor aparece no arranjo
    # 3) informar que o valor não pertence à faixa


