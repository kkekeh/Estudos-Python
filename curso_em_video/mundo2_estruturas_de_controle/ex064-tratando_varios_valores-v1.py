# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
# foi a soma entre eles (desconsiderando o flag).

n = int(input('Digite um número [999 encerra o programa]: '))
soma = c = 0

while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um número [999 encerra o programa]: '))

print(f'Você digitou {c} números e soma entre eles é de {soma}.')
