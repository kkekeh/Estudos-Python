# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra "FIM", o programa se encerrará. Importante: use cores.

from time import sleep

cores = {
    'vermelho': '\033[0;30;41m',
    'amarelo': '\033[0;30;43m',
    'azul': '\033[0;30;44m',
    'branco': '\033[7;40m',
    'limpa': '\033[m',
}


def msg(txt, cor='limpa'):
    tam = len(txt) + 6

    print(cores[cor], end='')
    print('~' * tam)
    print(f'   {txt}   ')
    print('~' * tam)
    print(cores['limpa'], end='')
    sleep(1)


def ajuda(cmd):
    msg(f'Acessando o manual do comando "{cmd}"...', 'azul')
    print(cores['branco'])
    help(cmd)
    print(cores['limpa'], end='')
    sleep(2)


while True:
    msg('SISTEMA DE AJUDA PyHELP', 'amarelo')

    cmd = str(input('comando: (FIM p/ encerrar) -> ')).strip()

    if cmd.upper() == 'FIM':
        break
    else:
        ajuda(cmd)

msg('Até logo!', 'vermelho')
