'''
    Faça um mini sistema, que utilize o interactive help do Python.
    O usuario vai digitar o comando eo manual vai aparecer.
    Quando o usuario digitar fim, o prgrama se encerrará.
    OBS: use cores.
'''

def ajuda(com):
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('*' * tam)
    print(msg)
    print('*' * tam)

#programa principal
comando=''
while True:
    titulo('  SISTEMA DE AJUDA PyHELP')
    comando = str(input("Função ou Biblioteca >"))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO')