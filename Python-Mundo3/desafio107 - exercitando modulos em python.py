'''
    crie um mod110 chamado moeda.py
    que tenha as funçoes incorporadas:
    aumentar(), diminuir(), dobro() e metade()
    Faça tambem um programa que importe esse módulo e use algumas dessas funções
    
'''
def aumentar(n):
    s = n * 0.10 + n
    return (s)

def diminuir(n):
    n - 1
    return(numero)

def dobro():
    n * 2
    return(numero)

def metade():
    n / 2
    return(numero)


numero = float(input('Digite um Valor: '))

print(f'10 % de R$ {numero} é R$ {aumentar(numero)}')