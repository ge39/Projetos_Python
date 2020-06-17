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
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM')

contador(2, 10, 2)

help(contador)
print('CONSTRUINDO UMA DOCSTRINGS')
'''
    PARA CONSTRUIR UMA DOCSTRINGS, LOGO ABAIXO DA DEF DA FUNÇÃO, DIGITE ASPAS DUPLAS 3 VEZES
'''
#exemplo
"""
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
ln()
print('PARAMETROS OPCIONAIS')

def somar(a=0, b=0, c=0): # O c=0 é o parametro opcional, se nao haver valor no parametro A,B ou C, ele assume o valor zero
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4)
somar()

ln()
print('ESCOPO DE VARIAVEL')
"""
ESCOPO DE VARIAVEL - É  LOCAL ONDE A VARIAVEL VAI EXISTIR
"""
#Escopo local - definida dentro da area de uma função

#Escopo Global - variavel declarada  dentro da area do programa principal, abaixo a def

"""
 para usar uma variavel global dentro de um escopo local, faça
 
 declare que sua variavel é do tipo global:
 
 def texte(a):
    global a
    a=8
    b+=4
    c = 2


#menu principal
a = 5 
"""




