# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# - Quantas pessoas foram cadastradas
# - Uma listagem com as pessoas mais pesadas
# - Uma listagem com as pessoas mais leves

lista_temp = []
lista_princ = []
maior = menor = 0

print()

while True:
    lista_temp.append(str(input('Nome: ')))
    lista_temp.append(int(input('Peso: ')))

    if len(lista_princ) == 0:
        maior = menor = lista_temp[1]
    else:
        if lista_temp[1] > maior:
            maior = lista_temp[1]
        if lista_temp[1] < menor:
            menor = lista_temp[1]

    lista_princ.append(lista_temp[:])
    lista_temp.clear()

    resp = str(input('Que continuar? [S/N] '))

    if resp in 'Nn':
        break

print(f'\n{len(lista_princ)} pessoa(as) foram cadastradas.')
print(f'{maior}KG é o maior peso. Peso de ', end='')

for p in lista_princ:
    
    if p[1] == maior:
        print(p[0], end=' ')

print(f'\n{menor}KG é o menor peso. Peso de ', end='')

for p in lista_princ:
    
    if p[1] == menor:
        print(p[0], end=' ')
