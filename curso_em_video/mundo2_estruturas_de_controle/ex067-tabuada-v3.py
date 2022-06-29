# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Digite um número para ver a sua tabuada: '))

    if num < 0:
        break

    print('-' * 13)

    for n in range(1, 11):
        print(f'{num} x {n:2} = {num * n}')

    print('-' * 13)
