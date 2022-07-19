# Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.

print()

largura = float(input('Largura: (m) '))
altura = float(input('Altura: (m) '))


def area(lar, alt):
    a = lar * alt

    print(f'A área do comprimento {lar}x{alt} é de {a:.1f}m².')


area(largura, altura)
print()
