# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com
# as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)


def notas(*notas, sit=False):
    dados = {}
    tam = len(notas)

    dados['notas'] = tam
    dados['maior'] = max(notas)
    dados['menor'] = min(notas)
    dados['media'] = sum(notas) / tam
    
    if sit:
        if dados['media'] < 5:
            dados['situacao'] = 'RUIM'
        elif dados['media'] <= 7:
            dados['situacao'] = 'RAZOÁVEL'
        else:
            dados['situacao'] = 'BOA'
    
    return dados


resp = notas(5, 8, 7, sit=True)

print()
print(resp)
print()

# Refazer esse exercício com mais lógica...
