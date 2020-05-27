'''
    Faça um programa que tenha uma função chamada contador()
    Que receba 3 parametros, inicio, fim e passo e realize a contagem
    Seu programa tem que fazer 3 contagens, através da função criada

    A) de 1 a 10, de 1 em 1
    B) de 10 a -10, de 2 em 2
    C) Uma contagem personalizada

'''

def contador(i, f, p):
    print(contador)

i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))

for contador in range(i, f, p):
    print(contador, end="")
    print(end="")
print(f'contagem de {i} até {f} de {p} em {p}  - FIM', end="")
