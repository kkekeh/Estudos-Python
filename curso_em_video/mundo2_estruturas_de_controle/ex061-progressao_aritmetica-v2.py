# Refaça o "ex051", lendo o primeiro termo e a razão de uma PA, mostrando os
# 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1

while c <= 10:
    print(f'{termo} → ', end='')

    termo += razao
    c += 1

print('FIM')
