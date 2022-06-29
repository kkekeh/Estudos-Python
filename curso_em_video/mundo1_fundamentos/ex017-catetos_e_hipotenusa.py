# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = hypot(co, ca)
hipo = (co ** 2 + ca ** 2) ** (1/5)  # Fórmula que calcula a hipotenusa.

print(f'Hipotenusa: {hi:.2f}')
