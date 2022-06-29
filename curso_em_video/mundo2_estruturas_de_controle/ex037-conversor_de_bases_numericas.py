# Escreva um programa que leia um número inteiro qualquer e peça
# para o usuário escolher qual será a base de conversão:
# 1 Para binário
# 2 Para octal
# 3 Para hexadecimal.

n = int(input('Digite um número (inteiro): '))

print('TIPOS DE CONVERSÃO')
print('[1] - Binário')
print('[2] - Octal')
print('[3] - Hexadecimal')

c = int(input('-> '))

if c == 1:
    print(bin(n)[2:])
elif c == 2:
    print(oct(n)[2:])
elif c == 3:
    print(hex(n)[2:])
else:
    print('Tipo Inválido!')
