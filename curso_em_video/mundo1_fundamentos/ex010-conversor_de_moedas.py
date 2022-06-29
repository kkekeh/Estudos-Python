# Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira e mostre quantos dólares ela pode comprar.

real = float(input("Dinheiro na carteira: R$"))

dol = real / 5.58

print(f'Com R${real:.2f} se pode comprar US${dol:.2f}')
