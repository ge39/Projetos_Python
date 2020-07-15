'''
    Adapte o codigo do desafio 107,
    criando uma funçao adicional chamada moeda() que consiga mostrar ps valores como um valor
    monetario formatado

'''
from exe108 import moeda2


numero = float(input('Digite um Valor: R$ '))
print(f'R$ {numero:.2f} aumentar  10 % =  R$ {moeda2.aumentar(numero, 10):.2f}')
print(f'R$ {numero:.2f} diminuiu 10 % =  R$ {moeda2.diminuir( numero, 10):.2f}')
print(f'O dobro de  R$ {numero} é  R$ {moeda2.dobro(numero):.2f}')
print(f'A metade de R$ {numero} é R$ {moeda2.metade(numero):.2f}')