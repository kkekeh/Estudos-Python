# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from moeda import aumentar, dobro, metade

print()

valor = float(input('Informe um valor: R$'))

aumentar(valor, 10)
dobro(valor)
metade(valor)
print()
