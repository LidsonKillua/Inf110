n = int(input())
v = []

for i in range(n):
    v.append(int(input()))

maior = 0
cmaior = 1
for i in v:
  if i > maior:
     maior = i
     cmaior = 1
  elif i == maior:
     cmaior += 1

print(f'{maior} {cmaior}')
