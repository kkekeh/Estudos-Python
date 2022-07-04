# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')

while True:
    num = int(input('Digite um número entre 0 e 5: '))

    if num >= 0 and num <= 20:
        break
    else:
        print('Tente novamente.', end=' ')

print(f'Você digitou o número {tupla[num]}.')
