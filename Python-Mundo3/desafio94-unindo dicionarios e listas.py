'''
Crie um programa que leia nome,sexo e idade de várias pessoas, guardadndo os dados de cada pessoa
em um dicionario.
e todos os dicionarios em uma lista.
No final, mostre:
A - Quantas pessoas foram cadastradas
B - A média de idade do grupo
C - Uma lista com todas as mulheres
D - Uma lista com todas as pessoas com idade acima da média.
'''
pessoa = dict()
galera = list()

while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome :").upper())
    while True:
        pessoa['sexo'] = str(input("Sexo [M/F]: ").upper())[0]
        if pessoa['sexo'] in 'FM':
            break
        print(f'ERROR!,por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('idade: '))
    while True:
        resp = str(input('Deseja continuar? [S/N]: ').upper())
        if resp in 'SN':
             break
        print("ERROR! Responda S ou N.")
    if resp in 'SN':
        break
print('=-'*30)
print(pessoa)

