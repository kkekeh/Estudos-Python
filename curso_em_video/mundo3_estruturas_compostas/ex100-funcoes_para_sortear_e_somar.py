# Faça um programa que tenha uma lista chamada "números" e duas funções, chamadas sorteia() e somaPar(). A primeira
# função vai sortear 5 números e vai colocá-los dentro da lista, e a segunda função vai mostrar a soma entre todos os
# valores pares sorteados pela função anterior.

from random import randint
from time import sleep

numeros = []


def sorteia():

    for n in range(0, 5):
        numeros.append(randint(0, 10))
    
    print('Sortenado números...')

    for valor in numeros:
        if valor % 2 == 0:
            print(f'\033[0;34;40m{valor}\033[m ', end='', flush=True)
        else:
            print(f'{valor} ', end='', flush=True)
        
        sleep(0.5)


def somaPar():
    soma = 0

    for valor in numeros:
        if valor % 2 == 0:
            soma += valor

    print(f'\nA soma dos valores pares é igual a \033[0;34;40m{soma}\033[m.')


print()
sorteia()
somaPar()
print()
