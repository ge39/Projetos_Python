'''
    Adapte o codigo do desafio 107,
    criando uma funçao adicional chamada moeda() que consiga mostrar ps valores como um valor
    monetario formatado

'''
from exe108 import moeda2


numero = float(input('Digite um Valor: R$ '))
print(f'R$ {moeda2.moeda(numero)} aumentar  10 % =  {moeda2.moeda(moeda2.aumentar(numero, 10))}')
print(f'R$ {moeda2.moeda(numero)} diminuiu 10 % =  {moeda2.moeda(moeda2.diminuir( numero, 10))}')
print(f'O dobro de {moeda2.moeda(numero)} é  {moeda2.moeda(moeda2.dobro(numero))}')
print(f'A metade de  {moeda2.moeda(numero)} é  {moeda2.moeda(moeda2.metade(numero))}')