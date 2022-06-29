# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
# todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
# quer ou não continuar a digitar valores.

quant = soma = media = maior = menor = 0
r = 'S'

while r in 'S':
    n = int(input('Digite um número: '))
    quant += 1
    soma += n
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

media = soma / quant

print(f'Média: {media:.1f}')
print(f'Maior e menor: {maior, menor}')
