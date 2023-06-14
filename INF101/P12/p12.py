# p12.py
# Programador: Lidson Oliveira
# Matrícula: 102961
# Criado em: 29/04
# Este programa gerencia um estoque com produtos, quantidades e preços e mostra em
# formato de tabela ao usuário. Além disso calcula seu valor total e mostra ao usuário.

def calculaValorTotal(estoque):

    total = 0
    for lista in estoque.values():
        total += (lista[0]*lista[1])

    return total

def main():
    
    estoque = { 'tomate': [1000, 2.30],
                'alface': [500, 0.45],
                'batata': [2150, 1.20],
                'feijão': [100, 5.50]}

    estoque['cebola'] = [500, 1.15]

    print()
    print('      Estoque da Quitanda')
    print()
    print('Produto      Preço   Quantidade')

    for chave, lista in sorted(estoque.items()):
        print('{}{:12.2f}{:11d}'.format(chave, float(lista[1]), int(lista[0])))
        
    print()
    print('Valor total do estoque: {:11.2f}'.format(calculaValorTotal(estoque)))

main()
