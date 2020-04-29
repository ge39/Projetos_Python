'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato
'''
player = []
gols = {}

player.append(str(input('Nome Jogador: ').upper()))
player.append(int(input(f'Nº de Partidas {player[0]}: ')))
for p in range(player[1]):
    gols['gol'] = int(input(f'Quantos gols na {p + 1}ª partida: '))
    player.append(gols.copy())
for e in player:

      print(f'=> {e}', end=" ")

