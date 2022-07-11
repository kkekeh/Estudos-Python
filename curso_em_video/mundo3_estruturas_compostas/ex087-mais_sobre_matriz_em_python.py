# Aprimore o desafio anterior, mostrando no final: 
# - A soma de todos os valores pares digitados
# - A soma dos valores da terceira coluna
# - O maior valor da segunda linha

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

soma_par = soma_val = maior = 0

print()

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l + 1}, {c + 1}]: '))

        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]

print()

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}] ', end='')
    
    print()

for l in range(0, 3):
    soma_val += matriz[l][2]

for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'A soma de todos os valores pares é {soma_par}.')
print(f'A soma dos valores da terceira coluna é {soma_val}.')
print(f'O maior valor da segunda linha é {maior}.')
print()
