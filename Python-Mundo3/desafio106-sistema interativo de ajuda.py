'''
    Faça um mini sistema, que utilize o interactive help do Python.
    O usuario vai digitar o comando eo manual vai aparecer.
    Quando o usuario digitar fim, o prgrama se encerrará.
    OBS: use cores.
'''
from time import sleep
# criar variavel global de cores
c = ('\033[m',  # 0 = sem cor
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[0;30;47m',   # 6 - cinza
     '\033[7;30m'  # 7 - branco  # background 40-branco;41-vermelho;43-amarelo;44-azul; 45-roxo; 46-ciano; 47-cinza
     );


def ajuda(com):
    #invocando uma função dentro de outra
    titulo(f'Acessando o manual do comando: \'{com}\'', 6)
    print(c[7], end= '')
    help(com)
    print(c[0], end="")
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('*' * tam)
    print(f'  {msg}')
    print('*' * tam)
    print(c[0], end='')
    sleep(1)

# programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 4)
    comando = str(input("Função ou Biblioteca >"))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)
