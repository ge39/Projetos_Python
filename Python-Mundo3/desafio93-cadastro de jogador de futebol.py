'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato
'''
jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome Jogador: ').upper())
tot = int(input(f'Nº de Partidas {jogador["nome"]}: '))
for p in range(0, tot):
   partidas.append = int(input(f'Quantos gols na {p + 1}ª partida: '))
jogador['gols'] = partidas[:]
print(jogador)
print(partidas)
