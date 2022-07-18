# Aprimore o ex093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.

time = []
gols = []
jogador = {}

print()

while True:
    jogador.clear()
    gols.clear()

    jogador['nome'] = str(input('Nome do Jogador: ')).strip()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    
    for p in range(0, jogador['partidas']):
        gols.append(int(input(f' Quantos gols na {p + 1}º partida? ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)

    time.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        
        if resp in 'SN':
            break
        
        print('ERRO! Informe apenas S ou N...')
    
    if resp == 'N':
        break

print('=' * 54)
print('cod ', end='')

for k in jogador.keys():
    print(f'{k:<15}', end='')

print()

for i, v in enumerate(time):
    print(f'{i:<4}', end='')

    for d in v.values():
        print(f'{str(d):<15}', end='')
    
    print()

print('-' * 54)

while True:
    busca = int(input('Mostrar dados de qual jogador? [999 p/ interromper] '))

    if busca == 999:
        break
    
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}...')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"].upper()}')

        for i, g in enumerate(time[busca]['gols']):
            print(f'Na partida {i + 1} fez {g} gol(s).')
    
    print('-' * 54)
