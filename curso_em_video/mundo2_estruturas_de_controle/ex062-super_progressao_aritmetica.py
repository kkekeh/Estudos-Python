# Melhore o "ex061", perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1
tot = 0
mais = 10

while mais != 0:
    tot += mais

    while c <= tot:
        print(f'{termo} → ', end='')

        termo += razao
        c += 1

    print('PAUSA')

    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('FIM')
