'''
    Faca um programa que tenha uma funcao chamada area ().
    que receba as dimensoes de um terreno retangular(largura e comprimento) e
    mostre a área do terreno
'''
print('CONTROLE DE TERRENO')

def area (l, c):
    s = l * c

    print(f'Largura = {l} M')
    print(f'Comprimento = {c} M')
    print(f'Area Total = {s:.2f} M')


lar = float(input('Largura(M): '))
com = float(input('Comprimento(M): '))

area(lar, com)



