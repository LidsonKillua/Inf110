# Nome: Lidson Oliveira
# Matrícula: 102961
# Data: 15/10/2020

 		
# Escreva aqui um breve comentário dizendo o que o programa 1 faz
# Este programa apresenta uma série de números baseada em uma fórmula definida em
# formato de fração e a soma dos números até a quantidade de elementos dada pelo
# usuário.
#
# Escreva o código para a resolução abaixo

n = int(input('N = '))
s = 0
num = 0
den = 0
i = 1
se = ''

while n <= 2:
    print('N deve ser maior que 2!')
    n = int(input('N = '))
    
while i < n:
    s += ((2*i-1)/((-1)**i*3))
    num = (2*i-1)
    den = ((-1)**i*3)
    se = se+('%.d/%.d'%(num,den))+', '
    i += 1

s += ((2*i-1)/((-1)**i*3))
num = (2*i-1)
den = ((-1)**i*3)
se = se+('%.d/%.d'%(num,den))

print()
print('Série = {'+se+'}')    
print('A soma dos %.d elementos da série é: %.4f'%(n,s))

