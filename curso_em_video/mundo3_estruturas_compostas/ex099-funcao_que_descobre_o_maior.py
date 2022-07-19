# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(*num):
    cont = maior = 0

    print('Analisando os valores passados...')

    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)

        if cont == 0:
            maior = valor
        elif valor > maior:
            maior = valor
        
        cont += 1
    
    print(f'\nO maior valor é {maior}.')


print()
maior(1, 2, 3, 4, 5)
print()
