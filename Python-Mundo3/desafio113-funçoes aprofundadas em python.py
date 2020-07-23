'''
    Reescreva a função leiaInt()
    que fizemos no desafio104, incluindo agora a possibilidade da digitação
    de um numero de tipo inválido.
    aproveite e crie uma função leiaFloat(), com a mesma funcionalidade
'''
from exe113 import numeros


#programa principal
n1 = numeros.leiaInt("Digite um numero: ")
n2 = numeros.leiaFloat("Digite um valor Real: ")
print(f'O valor inteiro foi \033[33m{n1}\033[m e o valor real foi \033[34m{n2:.2f}\033[m')

