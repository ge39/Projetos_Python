'''
    crie um programa  que tenha a funcao FATORIAL(), que receba dois parametros:
    O Primeiro parametro que indique o numero a calcular eo outro chamado show,
    que será mostrado um valor LÓGICO   (opcional) indicando se será mostrado
    ou não na tela o processo de cálculo do fatorial
'''

def fatorial(n , show=False):
    """
    -> Calcula o Fatorial de um Numero
    :param nr: O numero a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um Numero n

    """

    f = 1
    for c in range(n, 0, -1):
       f*=c

    return f
#Programa Principal
print(fatorial(5))