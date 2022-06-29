# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)

print('''[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input('Sua jogada: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
print(f'Computador jogou {itens[pc]}.')
print(f'Jogador jogou {itens[jogador]}.')

if pc == 0:  # Computador jogou Pedra.
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('JOGADOR PERDEU')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 1:  # Computador jogou Papel.
    if jogador == 0:
        print('JOGADOR PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 2:  # Computador jogou Tesoura.
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('JOGADOR PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
