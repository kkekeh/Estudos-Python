# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

viagem = float(input('Distância da viagem: '))

if viagem <= 200:
    print(f'O preço da passagem é de R$ {viagem * 0.50:.2f}')
else:
    print(f'O preço da passagem é de R$ {viagem * 0.45:.2f}')
