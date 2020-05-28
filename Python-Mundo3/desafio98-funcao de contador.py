'''
    Faça um programa que tenha uma função chamada contador()
    Que receba 3 parametros, inicio, fim e passo e realize a contagem
    Seu programa tem que fazer 3 contagens, através da função criada

    A) de 1 a 10, de 1 em 1
    B) de 10 a -10, de 2 em 2
    C) Uma contagem personalizada

'''
from time import sleep

def contador(i, f, p):
    print(f'contagem de {i} até {f} de {p} em {p}')
    sleep(1.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=" ", flush=True)
            sleep(0.25)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=" ", flush=True)
            sleep(0.25)
            cont -= p
        print('FIM!')


#programa principal
contador(1, 10, 1)
contador(100, 1, 5)

