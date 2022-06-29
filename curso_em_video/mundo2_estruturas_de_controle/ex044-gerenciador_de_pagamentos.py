# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
# preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: Preço normal
# - 3x ou mais no cartão: 20% de juros

val = float(input('Valor do produto: R$'))

print('''[1] À vista dinheiro/cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Em até 2x no cartão: Preço normal
[4] 3x ou mais no cartão: 20% de juros''')

opc = int(input('--> '))

if opc == 1:
    total = val - (val * 0.10)
    print(f'O valor a ser pago é de R${total:.2f}')
elif opc == 2:
    total = val - (val * 0.05)
    print(f'O valor a ser pago é de R${total:.2f}')
elif opc == 3:
    total = val
    prest = val / 2
    print(f'O valor a ser pago é de R${val:.2f} e será parcelado no cartão em 2x de R${prest:.2f}')
elif opc == 4:
    total = val + (val * 0.20)
    parc = int(input('Parcelas: '))
    prest = total / parc
    print(f'O valor a ser pago é de R${total:.2f} e será parcelado no cartão em {parc}x de R${prest:.2f}')
else:
    print('Opção Inválida!')
