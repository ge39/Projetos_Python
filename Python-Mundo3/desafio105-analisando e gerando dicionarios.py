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
    """
    'doscstring'
    -> Função para analisar notas e situações de vários alunos.()
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre  situação da turma
    """
    r = dict() #criando um dicionario para receber todas as notas
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)

    if sit: #se a situação for verdadeira "sit = True"....
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r



#Programa principal
resp = notas(2.5, 4.5, 2.5, 2.5, 6.5, sit = True)
print(resp)
help(notas) #docstring ou helper()