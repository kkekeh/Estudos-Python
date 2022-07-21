# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só
# que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')


def leiaInt(msg):
    valor = 0
    ok = False

    while True:
        num = str(input(msg))

        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido (não literal).\033[m')
        
        if ok:
            break
    return valor

print()

num = leiaInt('Digite um número: ')
print(f'Você digitou o número {num}.')

print()
