'''
PARTE 1
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.

Depois vai ler a quantidade de gols feitos em cada partida.

No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato

PARTE 2
Aprimore o desafio 93, para que ele funcione com varios jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento
de cada jogador
'''
jogador = dict()
gols = list()

while True:
    jogador['nome'] = str(input("NOME: ").upper())
    tot = int(input(f"Numero de partida do {jogador['nome']}: "))
    for p in range(0, tot):
        gols.append(int(input(f"QUANTOS GOLS NA {p+1}ª partida: ")))
    jogador['partidas'] = tot
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    #print(jogador)

    while True:
        resp = str(input("Deseja continuar[S/N] ").upper())[0]
        if resp not in 'SN':
            print('ERROR: Utilize S ou N.')
        if resp == 'N':
            break
    for k, v in jogador.items():
        print(f"Valor {k} => {v}")



