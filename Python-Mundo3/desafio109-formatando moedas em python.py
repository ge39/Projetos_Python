'''
    modifique as funções que foram criadas no desafio 107
    para que elas aceitem um parâmetro a mais, se o valor retornado por elas vai ser ou nao formatado
    pela função moeda().
    desenvolvida no desafio 108.
'''
from exe109 import moeda

numero = float(input('Digite um Valor: R$ '))

print(f'{moeda.moeda(numero)} aumentar  10 % = {moeda.aumentar(numero, 10,True)}')
print(f'{moeda.moeda(numero)} diminuiu 10 % =  {moeda.diminuir(numero, 10,True)}')
print(f'O dobro de  {moeda.moeda(numero)} é  {moeda.dobro(numero, True)}')
print(f'A metade de {moeda.moeda(numero)} é {moeda.metade(numero,True)}')