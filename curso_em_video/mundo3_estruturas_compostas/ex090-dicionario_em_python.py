# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
# conteúdo da estrutura na tela.

aluno = {}

print()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))

if aluno['media'] >= 6:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5 or aluno['media'] < 6:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print('-' * 30)

for k, v in aluno.items():
    print(f'{k} é igual a {v}')

print()
