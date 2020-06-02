'''
    Faça um programa que tenha uma função chamada Maior(),
    que receba vários parametros com valores inteiros.
    Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
#desempacotar parametros
from time import sleep
def maior(*num):
    cont = maior = 0
    print('\033[31m\nAnalisando os valores\033[m....')
    for valor in num:
        sleep(0.5)
        print(valor, end=" ", flush=True)
        if cont == 0:  # se for o inicio da contagem
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')



#  Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

