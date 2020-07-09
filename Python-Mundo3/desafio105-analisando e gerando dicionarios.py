'''
    Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
     e vai retornar um dicionario com as seguintes informações:

     quantidades de notas
     A maior nota
     a menor nota
     A média da turma
     A situação(opcional)
     Adicione tambem a docstring da função
'''
def notas(*n,sit=False):
    r = dict() #criando um dicionario para receber todas as notas
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)

    return r



#Programa principal
resp = notas(2.5, 4.5, 2.5, 10)
print(resp)