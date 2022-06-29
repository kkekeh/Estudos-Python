# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0

for n in range(1, 7):
    n = int(input(f'Informe valor {n}: '))

    if n % 2 == 0:
        soma += n

print()
print(f'A soma entre todos os valores pares é igual a {soma}.')
