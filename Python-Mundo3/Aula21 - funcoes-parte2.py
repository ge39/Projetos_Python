'''
    Interactive help
    help() - função interna do python, um metodo
'''
def ln():
    print('*' * 100)


help(print)
ln()
help(len)
ln()
help(input)
ln()
help(slice)
ln()
print('IMPRIME TODO A INFORMAÇÃO DE UMA FUNÇÃO')
print(print.__doc__)
'''
    DOCSTRINGS - BASICAMENTE É UMA STRING DE DOCUMENTAÇÃO, QUANDO DIGITAMOS help(input), ESTMOS MOSTRANDO A DOCUMENTA
    ÇÃO DA FUNÇÃO INPUT, E TODAS AS FUNCIONALIDADES INTERNAS DO PYTHON TEM SUA PROPRIA DOCSTRINGS
'''

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c =i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM')

contador(2, 10, 2)

help(contador)
print('CONSTRUINDO UMA DOCSTRINGS')
'''
    PARA CONSTRUIR UMA DOCSTRINGS, LOGO ABAIXO DA DEF DA FUNÇÃO, CRIE 2 ASPAS TRIPLAS
'''



