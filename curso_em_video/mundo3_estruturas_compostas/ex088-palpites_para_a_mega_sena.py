# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados, e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lista = []
jogos = []
cont = 0
tot = 1

print()

quant = int(input('Quantos jogos você quer fazer? '))

while tot <= quant:
    cont = 0
    
    while True:
        num = randint(1, 60)
        
        if num not in lista:
            lista.append(num)
            
            cont += 1
        
        if cont >= 6:
            break

    jogos.append(lista[:])
    jogos.sort()
    lista.clear()
    
    tot += 1

for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i + 1}: {l}')

print()
