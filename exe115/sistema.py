from exe115.lib.interface import *
from exe115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    #print('Arquivo encontrado com sucesso')
#else:
    #print('Arquivo não encontrado')
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoas', 'Sair do Sistema'])
    print('processando.....')

    sleep(1.5)
    if resposta == 1:
        #Opção de listar o conteudo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa!
       cabecalho('NOVO CADASTRO')
       nome = str(input('Nome: ').upper().strip())
       idade = int(input('Idade: '))
       cadastrar(arq,nome,idade)
    elif resposta == 3:
        #opcao de sair do sistema
        #cabecalho(f'Opcao 3')
        print(f'\033[0;30;46mSaindo do Sistema, Até Logo\033[m')
        break
    else:
        cabecalho('\033[31mERROR!! Digite uma opção válida')
        sleep(2)
