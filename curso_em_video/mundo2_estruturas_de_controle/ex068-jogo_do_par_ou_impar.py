# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador
# perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

vitorias = 0

while True:
    jogador = int(input('Digite uma valor: '))
    tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    computador = randint(0, 11)
    tot = jogador + computador
    tipo_tot = ''
    
    if tot % 2 == 0:
        tipo_tot = 'PAR'
    else:
        tipo_tot = 'ÍMPAR'
    
    print(f'Você jogou {jogador} e o computador {computador}. Total de {tot}. Deu {tipo_tot}!')

    if tipo == 'P':
        if tipo_tot == 'PAR':
            print('Você ganhou!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if tipo_tot == 'ÍMPAR':
            print('Você ganhou!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break

    print('Vamos jogar novamente...')

print(f'Você venceu {vitorias} vezes.')
