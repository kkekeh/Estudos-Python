# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai
# se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_atual = date.today().year

nasc = int(input('Ano de Nascimento: '))

idade = ano_atual - nasc

print()
print(f'Você tem {idade} anos de idade.')

if idade < 18:
    print(f'Ainda não pode se alistar!')
    print(f'Poderá se alistar daqui a {18 - idade} ano(s).')
elif idade == 18:
    print('Já pode se alistar!')
elif idade > 18:
    print('Não pode mais se alistar!')
    print(f'O prazo de alistamento venceu há {idade - 18} ano(s).')
