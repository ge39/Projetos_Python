from exe115.lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar noca pessoas', 'Sair do Sistema'])
    print('processando.....')
    sleep(1.5)
    if resposta == 1:
        cabecalho(f'opção 1')
    elif resposta == 2:
        cabecalho(f'Opcao 2')
    elif resposta == 3:
        #cabecalho(f'Opcao 3')
        print(f'\033[0;30;46mSaindo do Sistema, Até Logo\033[m')
    else:
        cabecalho('\033[31mERROR!! Digite uma opção válida')
        sleep(2)
