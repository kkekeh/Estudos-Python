# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar ou não. No final, mostre:
# - Qual é o total gasto na compra.
# - Quantos produtos custam mais de R$1000.
# - Qual é o nome do produto mais barato.

tot = tot1000 = menor = cont = 0
barato = ''

while True:
    produto = str(input('Nome do produto: ')).strip()
    valor = float(input('Valor: R$ '))
    cont += 1
    tot += valor

    if valor > 1000:
        tot1000 += 1

    if cont == 1:
        barato = produto
        menor = valor
    else:
        if valor < menor:
            barato = produto
            menor = valor

    continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]

    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'Total de R${tot:.2f} gasto.')
print(f'Total de {tot1000} produtos que custam mais que R$1000')
print(f'{barato} é o produto mais barato.')
