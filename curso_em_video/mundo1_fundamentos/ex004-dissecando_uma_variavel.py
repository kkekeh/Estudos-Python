# Faça um programa que leia algo pelo teclado e mostre na tela o seu
# tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo: ')
print('Tipo Primitivo', type(algo))
print('É alfabético:', algo.isalpha())
print('É numérico:', algo.isnumeric())
print('É alfanumérico:', algo.isalnum())
print('Está capitalizado:', algo.istitle())
print('Está em maiúsculo:', algo.isupper())
print('Está em minúsculo:', algo.islower())
