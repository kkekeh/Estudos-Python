# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Km percorridos: '))
dias = int(input('Dias alugados: '))

preco = km * 0.15 + dias * 60

print(f'O carro percorreu {km}km durante {dias} dias. O preço a pagar é de R${preco:.2f}')
