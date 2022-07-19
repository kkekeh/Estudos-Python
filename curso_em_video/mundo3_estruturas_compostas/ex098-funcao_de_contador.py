# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# - De 1 até 10, de 1 em 1
# - De 10 até 0, de 2 em 2
# - Uma contagem personalizada

from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    
    if i < f:
        sleep(0.5)

        for n in range(i, f + 1, p):
            print(f'{n} ', end='', flush=True)
            sleep(0.5)
        
        print('FIM!')
    else:
        sleep(0.5)

        for n in range(i, f - 1, -p):
            print(f'{n} ', end='', flush=True)
            sleep(0.5)
        
        print('FIM!')


print()
contador(1, 10, 1)
contador(10, 0, 2)
print('\nAgora é a sua vez de escolher...')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

print()
contador(inicio, fim, passo)
print()
