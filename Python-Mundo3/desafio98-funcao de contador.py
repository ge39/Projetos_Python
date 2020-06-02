'''
    Faça um programa que tenha uma função chamada contador()
    Que receba 3 parametros, inicio, fim e passo e realize a contagem
    Seu programa tem que fazer 3 contagens, através da função criada

    A) de 1 a 10, de 1 em 1
    B) de 10 a -10, de 2 em 2
    C) Uma contagem personalizada

'''
from time import sleep
def ln():
    print('=' *40)
def contador(i, f, p):
    print(f'inicio {i} fim {f} de {p} até {p}')
    sleep(1.0)
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    if i > f:       # inicio maior que o fim
        cont = i
        while cont >= f:
            sleep(0.25)
            print(f'{cont}', end=" ")
            cont -= p
    if i <= f:      # se inicio for menor ou igual ao fim
        cont = i
        while cont <= f:
            sleep(0.25)
            print(f'{cont}', end=" ", flush=True)
            cont += p
        print('FIM')

#main program
contador(1, 10, 1)
contador(10, -10, 2)
print()
ln()
print('AGORA É SUA VEZ DE CRIAR O CONTADOR')
ini = int(input('Inicio: '))
fin = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fin, pas)

