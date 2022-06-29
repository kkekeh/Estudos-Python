# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Salario do funcionário: R$'))

novo = sal + (sal * 0.15)

print(f'O salário de R${sal:.2f} com 15% de aumento fica R${novo:.2f}')
