# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 30)
print(f'{"BANCO":^30}')
print('=' * 30)

valor = float(input('Que valor deseja sacar? R$'))
tot = valor
ced = 50
tot_ced = 0

while True:

    if tot >= ced:
        tot -= ced
        tot_ced += 1
    else:
        if tot_ced > 0:
            print(f'Total de {tot_ced} cédulas de R${ced}')

        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1

        tot_ced = 0

        if tot == 0:
            break

print('=' * 30)
print('Volte sempre! Tenha um bom dia!')
print('=' * 30)
