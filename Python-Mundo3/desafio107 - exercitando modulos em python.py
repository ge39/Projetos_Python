'''
    crie um mod110 chamado moeda.py
    que tenha as funçoes incorporadas:
    aumentar(), diminuir(), dobro() e metade()
    Faça tambem um programa que importe esse módulo e use algumas dessas funções
    
'''
import moeda

numero = float(input('Digite um Valor: '))

print(f'R$ {numero:.2f} aumentar  10 % =  R$ {moeda.aumentar(numero):.2f}')
print(f'R$ {numero:.2f} diminuiu 10 % =  R$ {moeda.diminuir( - numero):.2f}')
print(f'O dobro de  R$ {numero} é  R$ {moeda.dobro(numero):.2f}')
print(f'A metade de R$ {numero} é R$ {moeda.metade(numero):.2f}')