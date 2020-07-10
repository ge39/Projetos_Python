'''
    Faça um mini sistema, que utilize o interactive help do Python.
    O usuario vai digitar o comando eo manual vai aparecer.
    Quando o usuario digitar fim, o prgrama se encerrará.
    OBS: use cores.
'''
#criar variavel global de cores
c = ('\033[m',           # 0 = sem cor
     '\033[0;30;41m\033[m',    # 1 - vermelho
     '\033[0;30;42m',    # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m'       # 6 - branco
    # background 40-branco;41-vermelho;43-amarelo;44-azul; 45-magenta; 46-ciano; 47-cinza
     )


def ajuda(com):
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('*' * tam)
    print(f'  {msg}')
    print('*' * tam)

#programa principal
comando =''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input("Função ou Biblioteca >"))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)