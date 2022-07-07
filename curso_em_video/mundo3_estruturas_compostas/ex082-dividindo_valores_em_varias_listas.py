# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
# listas geradas.

numeros = []
pares = []
impares = []

print()

while True:
    numeros.append(int(input('Digite um número: ')))

    resp = str(input('Quer continuar? [S/N] '))

    if resp in 'Nn':
        break
    
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'Lista completa {numeros}')
print(f'Pares da lista {pares}')
print(f'Ímpares da lista {impares}')

print()
