# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
tot = 0

for n in range(1, num + 1):

    if num % n == 0:
        tot += 1

        print(n, end=' ')

print()
print(f'O número {num} foi dividido {tot}x')

if tot == 2:
    print('Número Primo.')
else:
    print('Número não Primo.')
