# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# - Quantos números foram digitados
# - A lista de valores, ordenada de forma decrescente
# - Se o valor 5 foi digitado e está ou não na lista

numeros = []

print()

while True:
    numeros.append(int(input('Digite um número: ')))

    resp = str(input('Quer continuar? [S/N] '))

    if resp in 'Nn':
        break

numeros.sort(reverse=True)
print(f'Você digitou {len(numeros)} números.')
print(f'Os valores em ordem decrescente são {numeros}')

if 5 in numeros:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')

print()
