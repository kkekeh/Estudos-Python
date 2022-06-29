# Refaça o "ex009", mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número para ver a sua tabuada: '))

print('-' * 13)

for n in range(1, 11):
    print(f'{num} x {n:2} = {num * n}')

print('-' * 13)
