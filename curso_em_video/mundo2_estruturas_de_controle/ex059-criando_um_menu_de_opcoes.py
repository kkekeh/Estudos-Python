# Crie um programa que leia dois valores e mostre um menu na tela:
# 1 Somar
# 2 Multiplicar
# 3 Maior
# 4 Novos números
# 5 Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print("""[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa""")

opcao = int(input('--> '))

while opcao != 5:

    if opcao == 1:
        print(f'A soma entre os números {n1} e {n2 } é igual a {n1 + n2}.')
    elif opcao == 2:
        print(f'A multiplicação entre os números {n1} e {n2 } é igual a {n1 * n2}.')
    elif opcao == 3:
        maior = n1

        if n2 > maior:
            maior = n2

        print(f'O maior valor entre os números {n1} e {n2 } é {maior}.')

    elif opcao == 4:
        print('Informe novos números.')

        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    else:
        print('Opção inválida! Tente novamente...')
    
    print("""[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa""")

    opcao = int(input('--> '))

print('Fim do programa...')
