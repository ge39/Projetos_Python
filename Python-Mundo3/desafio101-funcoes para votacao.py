'''
    Crie um programa que tenha uma função chamada voto() que vai receber como parametro:
    o ano de nascimento de uma pessoa.
    retornando um valor literal, indicando se uma pessoa tem voto NEGADO, OPCIONAL ou ÓBRIGATÓRIO nas eleiçoes.

'''



def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano

    if (idade < 16):
          return f'voce tem {idade} anos, Não atingiu idade para votar'
    elif 16 <= idade < 18 or idade > 65:
        return f'Voce tem {idade} anos, Voto opcional'
    else:
        return f'Voce tem {idade} anos, Voto Obrigatório'

#Programa principal
nasc = int(input('Em que ano voce nasceu: '))
print(voto(nasc))