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
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome :").upper())
    while True:
        pessoa['sexo'] = str(input("Sexo [M/F]: ").upper())[0]
        if pessoa['sexo'] in 'FM':
            break
        print(f'ERROR!,por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]: ').upper())
        if resp in 'SN':
             break
        print("ERROR! Responda S ou N.")
    if resp in 'N':
        break
print('=-'*30)
#  print(galera)
print('=-'*30)

# A - Quantas pessoas foram cadastradas
print(f'A) Total de pessoas cadastradas: {len(galera)} pessoas')
media = soma / len(galera)

# B - A média de idade do grupo
print(f'B) A média de idade: {media:5.1f} anos')

# C - Uma lista com todas as mulheres
print(f'C) As mulheres cadastradas foram ', end=" ")
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=", ")
print()

# D - Uma lista com todas as pessoas com idade acima da média.
print(f'D) pessoas acima da media', end=" ")
for p in galera:
    if p['idade'] >= media:
        print(f'{p["nome"]};sexo {p["sexo"]}; idade {p["idade"]}', end=" ")
print('<<<<ENCERRADO>>>>')


