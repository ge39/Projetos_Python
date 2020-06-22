'''
    faça um programa que tenha uma lista chamada numeros e duas funçoes chamaddas sorteia() e somapar().
    A primeira função vai sortear 5 numeros, e vai coloca-los dentro da lista.
    A segunda função vai mostrar a soma entre todos os valores Pares sorteados pela função anterior.
'''

from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores ad Lista: ', end=" ")
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)  # copiando os valores para a função sorteia
        print(f'{n}', end=" ", flush=True)
        sleep(0.3)
    print(' - PRONTO!!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores de {lista}, temos  {soma}')

numeros = list()    # lista
sorteia(numeros)    # invocando a funcao sorteia
somaPar(numeros)    # invocando a função somaPar

