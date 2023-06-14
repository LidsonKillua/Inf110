'''
frase = input('Digite a sentença: ')

aberto = 0
fechado = 0

for i in frase:
    if i == '(':
        aberto += 1
    elif i == ')':
        fechado += 1

if aberto == fechado:
    print('OK')
elif aberto != fechado:
    print('Errado')
'''
####
'''
def distancia(ls, li=0, pas=1):
    ls = int(ls)
    li = int(li)
    pas = int(pas)
    while li < ls:
        return li
        li += pas


for i in distancia(0, 10):
    print(i)
'''
######
'''
a,b = 1,2
c = 1 , 2
print(a)
print(b)
print(c)
'''
#####
x = 1 , 2
y = 3 , 4

x , y = y , x

print(x)
print(y)
