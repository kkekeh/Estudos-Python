# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Largura da parede (m): '))
alt = float(input('Altura da parede (m): '))

area = larg * alt
tinta = area / 2

print(f'Para pintar uma parede de {area:.1f}m² é preciso {tinta:.1f}l de tinta.')
