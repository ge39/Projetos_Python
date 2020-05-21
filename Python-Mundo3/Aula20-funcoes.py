'''Funçoes python, cria comando personalizados e parametros'''

#  funcoes ou rotinas
def linha():
    print('*-' * 40)

linha()



#  funcoes com parametros , argumentos
def titulo(msg):
    print('-' * 30)
    print(msg)
    print('-'* 30)


#  programa principal
titulo('CURSO EM VIDEO')
titulo('APRENDA PYTHON')
titulo('GUSTAVO GUANABARA')
titulo('Aluno - Jeremias')

print('criando uma funçao soma')
def soma(a, b):
    S = a + b
    print(S)


soma(4, 5)
soma(2, 5)
soma(2, 15)
soma(2, 8)
print('-' * 30)
print('Como empacotar parametros, entao, ')
# o simbolo * define desempacotar parametros, entao, ele entenderá que voce passará varios parametros, e
# nao sabe quantos sao, entao voce vai pegar todos os parametros e jogar dentro de num, isso significa,
# se voce jogar um ou 10 mil parametros, ele vai jogar dentro de num.

def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')

    for valor in num:
        print(f' {valor}', end='')
    print(' - FIM!')

contador(2, 1, 9)
contador(7, 0, 3, 8,)
contador(1)



linha()
print(' Funçoes com listas')
def dobra(lista):

    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)



