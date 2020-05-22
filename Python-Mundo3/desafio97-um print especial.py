'''
    faça um programa que tenha a função chamada escreva()
    que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel
'''

def escreva(txt,l):
    print('-' * l)
    print(f'  {txt}')
    print('-' * l)


texto = str(input('texto: '))
linha = len(texto) + 4
escreva(texto, linha)
