# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
# cada palavra, quais são as suas vogais.

palavras = ('teste',
            'testando')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais ', end='')

    for l in p:
        if l in 'aeiou':
            print(l, end=' ')
