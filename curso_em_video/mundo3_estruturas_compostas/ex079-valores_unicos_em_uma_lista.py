# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

valores = []

while True:
    val = int(input('Digite um valor: '))

    if val not in valores:
        valores.append(val)
        print('Valor adcionado com sucesso!')
    else:
        print('Valor duplicado. Não foi adicionado!')

    resp = str(input('Quer continuar? [S/N] '))

    if resp in 'Nn':
        break

valores.sort()
print(f'Você digitou os valores {valores}')
