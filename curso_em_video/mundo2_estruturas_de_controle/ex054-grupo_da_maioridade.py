# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
# pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

ano = date.today().year
maior = 0
menor = 0

for n in range(1, 8):
    nasc = int(input('Ano de Nascimento: '))

    if ano - nasc >= 18:
        maior += 1
    else:
        menor += 1

print()
print(f'Pessoas de maior: {maior}')
print(f'Pessoas de menor: {menor}')
