# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# - Quantas vezes apareceu o valor 9
# - Em que posição foi digitado o primeiro valor 3
# - Quais foram os números pares

valores = (int(input('Digite um valor: ')),
           int(input('Digite mais um valor: ')),
           int(input('Digite mais outro valor: ')),
           int(input('Digite só mais um valor: ')))

print(f'Você digitou os valores: {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes.')

if 3 in valores:
    print(f'O valor 3 apareceu pela primeira vez na posição {valores.index(3) + 1}.')

print('Os valores pares são: ', end='')

for v in valores:
    if v % 2 == 0:
        print(v, end=' ')
