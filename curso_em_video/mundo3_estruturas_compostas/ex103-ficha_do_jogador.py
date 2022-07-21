# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.

print()

jogador = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))


def ficha(nome='<não informado>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s).')


if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if jogador == '':
    ficha(gol=gols)
else:
    ficha(jogador, gols)

print()
