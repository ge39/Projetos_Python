'''
    Faça um programa que tenha uma função chamada Maior(),
    que receba vários parametros com valores inteiros.
    Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
#desempacotar parametros
def maior(*num):
    print('Analisando os valores....')
    for valor in num:
        print(num, end=" ")




#  Programa principal
maior(2, 9, 4, 5, 7, 1)
#maior(4, 7, 0)
#maior(1, 2)
#maior(6)
#maior()

