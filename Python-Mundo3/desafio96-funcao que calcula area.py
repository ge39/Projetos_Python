'''
    Faca um programa que tenha uma funcao chamada area ().
    que receba as dimensoes de um terreno retangular(largura e comprimento) e
    mostre a área do terreno
'''
def area (l, c):
    s = l * c

    print(f'Largura = {l}')
    print(f'Comprimento = {c}')
    print(f'Area = {s}')


lar = float(input('Largura:' ))
com = float(input('Comprimento'))

area(lar, com)



print('CONTROLE DE TERRENO')