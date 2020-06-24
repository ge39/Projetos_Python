'''
    Crie um programa que tenha uma função chamada voto() que vai receber como parametro:
    o ano de nascimento de uma pessoa.
    retornando um valor literal, indicando se uma pessoa tem voto NEGADO, OPCIONAL ou ÓBRIGATÓRIO nas eleiçoes.

'''
def voto(ano):

    anoatual = 2020
    if (anoatual - idade < 16):
        print(f'voce tem {anoatual-idade} anos, Não atingiu idade para votar')
    elif(anoatual - idade > 65):
        print(f'Voce tem {anoatual-idade} anos, Voto opcional')
    else:
        print(f'Voce tem {anoatual - idade} anos, Voto Obrigatório')


idade= int(input('Em que ano voce nasceu: '))
votar(idade)