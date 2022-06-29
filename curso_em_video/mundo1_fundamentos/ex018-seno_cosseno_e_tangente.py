# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

ang = float(input('Infome o valor de um ângulo qualquer: '))

seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print(f'Seno: {seno:.2f}\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}')
