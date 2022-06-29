# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras têm o nome (sem considerar espaços).
# - Quantas letras têm o primeiro nome.

nome = str(input('Informe seu nome completo: ')).strip()

print(f'Seu nome em maiúsculo: {nome.upper()}')
print(f'Seu nome em minúsculo: {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras.')
#print(f'Seu primeiro nome tem {nome.find(" ")} letras.')
print(f'Seu primeiro nome tem {len(nome.split()[0])} letras.')
