# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Valor do produto: R$'))

novo = preco - (preco * 0.05)

print(f'O produto de R${preco:.2f} com 5% de desconto fica R${novo:.2f}')
