# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
# pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

print()
ano_nasc = int(input('Ano de Nascimento: '))


def voto(ano):
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - ano

    if idade < 16:
        return f'Com idade {idade}: Voto NEGADO'
    elif idade >= 16 and idade < 18 or idade > 65:
        return f'Com idade {idade}: Voto OPCIONAL'
    else:
        return f'Com idade {idade}: Voto OBRIGATÓRIO'


print(voto(ano_nasc))
print()
