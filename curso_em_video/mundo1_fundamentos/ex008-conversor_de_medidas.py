# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Informe um valor em metros: '))

cm = medida * 100
mm = medida * 1000

print(f'{medida}m equivale a {cm:.0f}cm e {mm:.0f}mm')
