'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato
'''
player = dict()

while True:
    player['nome'] = str(input('Nome Jogador: ').upper())
    player['partida'] = int(input(f'Nº de Partidas {player["nome"]}: '))
    for p in range(player['partida']):
        gols = int(input(f'Quantos gols na {p + 1}ª partida: '))
