# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# - Quantas pessoas foram cadastradas
# - A média de idade
# - Uma lista com as mulheres
# - Uma lista de pessoas com idade acima da média

pessoas = []
pessoa = {}
soma = media = 0

print()

while True:
    pessoa.clear()
    
    pessoa['nome'] = str(input('Nome: ')).strip()
    
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    
        if pessoa['sexo'] in 'MF':
            break
        
        print('ERRO! Informe apenas M ou F...')
    
    pessoa['idade'] = int(input('Idade: '))    
    soma += pessoa['idade']

    pessoas.append(pessoa.copy())
    
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    
        if resp in 'SN':
            break
        
        print('ERRO! Informe apenas S ou N...')
    
    if resp == 'N':
        break

print(f'\nTotal de {len(pessoas)} pessoas cadastradas.')

media = soma / len(pessoas)

print(f'A média de idade é de {media:.1f}')
print(f'Mulheres cadastradas:')

for p in pessoas:
    
    if p['sexo'] == 'F':
        print(f' {p["nome"]}')

print(f'Pessoas com idade acima da média ({media:.1f}):')

for p in pessoas:
    
    if p['idade'] >= media:
        
        for k, v in p.items():
            print(f' {k} = {v};', end=' ')
        
        print()

print()
