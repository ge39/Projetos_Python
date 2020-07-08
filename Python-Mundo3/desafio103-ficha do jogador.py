'''
    Faça um programa que tenha uma funcao chamada ficha(), que receba dois parametros
    opcionais, o nome de um jogador, e quantos gols ele marcou.

    O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não
    tenha sido informado corretamente.
'''

def ficha(jog='<desconhecido>', gol=0):
    print(f'Nome do jogador {jog} e fez {gol} gols ')


#programa principal
n = str(input('Nome jogador :'))
g = str(input('Quantos gols! :'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '': #se tirou todos os espaços e ficou vazio
    ficha(gol=g)
else:
    ficha(n, g)







