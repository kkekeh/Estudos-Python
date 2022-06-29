# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Digite um número para ver o seu fatorial: '))
c = n
f = 1

while c > 0:
    print(c, end='')

    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')

    f *= c
    c -= 1

print(f)
