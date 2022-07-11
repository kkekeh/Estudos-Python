# Crie um programa onde o usuário possa digitar sete valores numéricos, e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valores = [[], []]

print()

for c in range(0, 7):
    valor = int(input(f'Digite o {c + 1}° valor: '))
    
    if valor % 2 == 0: # Par.
        valores[0].append(valor)
    else: # Ímpar.
        valores[1].append(valor)

valores[0].sort()
valores[1].sort()

print(f'\nValores pares: {valores[0]}')
print(f'Valores ímpares: {valores[1]}')
print()
