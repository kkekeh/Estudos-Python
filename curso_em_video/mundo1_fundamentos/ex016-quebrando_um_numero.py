# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

n = float(input('Digite um número Real: '))

print(f'A porção Inteira de {n} é {trunc(n)}')
