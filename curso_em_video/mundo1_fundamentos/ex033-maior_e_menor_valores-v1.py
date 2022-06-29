# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))

# Verificando qual é o maior.
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

# Verificando qual é o menor.
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print(f'O número maior é o {maior} e o menor é o {menor}.')
