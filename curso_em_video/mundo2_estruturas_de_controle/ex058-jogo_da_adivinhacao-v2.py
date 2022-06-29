# Melhore o jogo do "ex028" onde o computador vai "pensar" em um número entre 0 e 10. Só que agora, o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('-=-= JOGO DA ADIVINHAÇÃO v2.0 =-=-')
print('Vou pensar em um número entre 0 e 10. Tente adivinhar!')

computador = randint(0, 10)
jogador = int(input('Em que número eu pensei? '))
palpites = 1

while jogador != computador:

    if jogador > computador:
        print('Menos... Tente mais uma vez.')
    elif jogador < computador:
        print('Mais... Tente mais uma vez.')
    
    jogador = int(input('Em que número eu pensei? '))
    palpites += 1

if jogador == computador:
    print(f'Acertou! Eu pensei no número {computador}. Você fez {palpites} tentativas.')
