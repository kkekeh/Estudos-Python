def aumentar(valor, taxa):
    print(f'Aumentando {taxa}%, temos R${valor + (valor * taxa / 100):.2f}')


def diminuir(valor, taxa):
    print(f'Dimuindo {taxa}%, temos R${valor - (valor * taxa / 100):.2f}')


def dobro(valor):
    print(f'O dobro de R${valor:.2f} é R${valor * 2:.2f}')


def metade(valor):
    print(f'A metade de R${valor:.2f} é R${valor / 2:.2f}')
