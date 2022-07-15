# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []

print()

jogador['nome'] = str(input('Nome do Jogador: ')).strip()
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for p in range(0, jogador['partidas']):
    gols.append(int(input(f' Quantos gols na {p + 1}º partida? ')))

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print('-' * 30)

for k, i in jogador.items():
    print(f'{k}: {i}')

print('-' * 30)
