# Crie um programa que leia nome, ano de nascimento e carteira de trabalho, e cadastre-o (com idade) em um dicionário. Se
# por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dados = {}
ano_atual = datetime.now().year

print()

dados['nome'] = str(input('Nome: ')).strip()
ano_nasc = int(input('Ano de Nascimento: '))
dados['idade'] = ano_atual - ano_nasc
dados['ctps'] = int(input('Carteira de Trabalho: (0 se não possuir) '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - ano_atual)

print()

for k, i in dados.items():
    print(f'{k}: {i}')

print()
