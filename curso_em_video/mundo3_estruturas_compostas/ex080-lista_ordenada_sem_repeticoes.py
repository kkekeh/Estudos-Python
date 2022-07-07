# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

valores = []

print()

for c in range(0, 5):
    val = int(input('Digite um valor: '))

    if c == 0 or val > valores[-1]:
        valores.append(val)
    else:
        pos = 0

        while pos < len(valores):
            if val <= valores[pos]:
                valores.insert(pos, val)
                
                break
            
            pos +=1

print(f'\nVocê digitou os valores {valores}')
print()
