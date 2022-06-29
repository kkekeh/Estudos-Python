# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.

soma_idade = 0
idade_homem_velho = 0
nome_homem_velho = ''
tot_mulher20 = 0

for p in range(1, 5):
    print(f'---- {p}ª PESSOA ----')

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade

    if p == 1 and sexo in 'Mm':
        nome_homem_velho = nome
        idade_homem_velho = idade

    if sexo in 'Mm' and idade > idade_homem_velho:
        nome_homem_velho = nome
        idade_homem_velho = idade

    if sexo in 'Ff' and idade < 20:
        tot_mulher20 += 1

media_idade = soma_idade / 4

print(f'A média de idade do grupo é de {media_idade} anos.')
print(f'{nome_homem_velho} é o homem mais velho e tem {idade_homem_velho} anos de idade.')
print(f'Ao todo são {tot_mulher20} mulheres com menos de 20 anos.')
