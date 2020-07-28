from exe115.lib.interface import *

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar noca pessoas', 'Sair do Sistema'])

    if resposta == 1:
        print(f'opção 1')

    elif resposta == 2:
        print(f'Opcao 2')
    elif resposta == 3:
        print(f'Opcao 3')
        print(f'Saindo do Sistema, Até Logo')
    else:
        print('\033[31mERROR!! Digite uma opção válida')

