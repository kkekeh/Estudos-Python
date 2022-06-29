sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while sexo not in 'MF':
    print('Dado incorreto!\n')
    sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

print('Dado registrado com sucesso!')
