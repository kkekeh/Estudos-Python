# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre:
# - Quantas pessoas tem mais de 18 anos.
# - Quantos homens foram cadastrados.
# - Quantas mulheres tem menos de 20 anos.

maior = homens = mulher20 = 0

while True:
    idade = int(input('Informe idade: '))
    sexo = str(input('Informe sexo: [M/F] ')).strip().upper()[0]
    
    while sexo not in 'MF':
        sexo = str(input('Informe sexo: [M/F] ')).strip().upper()[0]

    print('Pessoa cadastrada!')

    if idade > 18:
        maior += 1
    
    if sexo == 'M':
        homens += 1
    
    if sexo == 'F' and idade < 20:
        mulher20 += 1

    continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]

    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'Total de {maior} pessoas maior de idade cadastradas.')
print(f'Total de {homens} homens cadastrados.')
print(f'Total de {mulher20} mulheres com menos de 20 anos de idade cadastradas.')
