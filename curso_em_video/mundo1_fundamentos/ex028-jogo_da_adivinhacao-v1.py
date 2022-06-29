# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela
# se o usuário venceu ou perdeu.

from random import randint

print('-=-= JOGO DA ADIVINHAÇÃO v1.0 =-=-')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')

computador = randint(0, 5)
jogador = int(input('Em que número eu pensei? '))

if jogador == computador:
    print(f'Acertou! eu pensei no número {computador}.')
else:
    print(f'Errou! eu pensei no número {computador}.')
