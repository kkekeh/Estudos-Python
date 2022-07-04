# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# - Os 5 primeiros times
# - Os últimos 4 colocados
# - Times em ordem alfabética
# - Em que posição está o time da Chapecoense

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print()
print(f'Os 5 primeiros times são:\n {times[:5]}\n')
print(f'Os últimos 4 colocados são:\n {times[-4:]}\n')
print(f'Times em ordem alfabética:\n {sorted(times)}\n')
print(f'O Chapecoense está na posição {times.index("Chapecoense") +1}.')
