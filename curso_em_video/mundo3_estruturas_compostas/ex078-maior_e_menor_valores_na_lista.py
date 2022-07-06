# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual 
# foi o maior e o menor valor digitado, e as suas respectivas posições na lista.

lista = []
maior = menor = 0

print()

for c in range(0, 5):
    lista.append(int(input(f'Digite um valor na posição {c}: ')))

    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        elif lista[c] < menor:
            menor = lista[c]

print()
print(f'Você digitou os valores {lista}')
print(f'O maior valor da lista é o {maior} nas posições ', end='')

for i, v in enumerate(lista):
    if v == maior:
        print(f'{i + 1} ', end='')

print(f'\nO menor valor da lista é o {menor} nas posições ', end='')

for i, v in enumerate(lista):
    if v == menor:
        print(f'{i + 1} ', end='')
