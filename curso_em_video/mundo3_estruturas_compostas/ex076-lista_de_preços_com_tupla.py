# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Produto 1', 1.00,
            'Produto 2', 1.00,
            'Produto 3', 1.00,
            'Produto 4', 1.00,
            'Produto 5', 1.00)

print()

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end=' ')
    else:
        print(f'R${produtos[pos]:>8.2f}')
