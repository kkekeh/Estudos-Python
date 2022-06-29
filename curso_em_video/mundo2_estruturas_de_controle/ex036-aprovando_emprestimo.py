# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode
# exceder 30% do salário ou então o empréstimo será negado.

val = float(input('Valor da casa: R$'))
sal = float(input('Salário do Comprador: R$'))
anos = int(input('Anos de financiamento: '))

prest = val / (anos * 12)

print()
print(f'O valor da prestação é de R${prest:.2f}')

if prest <= sal * 0.30:
    print('Empréstimo Aprovado!')
else:
    print('Empréstimo Negado!')
