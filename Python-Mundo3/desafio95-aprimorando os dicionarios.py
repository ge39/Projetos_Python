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
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input("NOME: ").upper())
    tot = int(input(f"Numero de partida do {jogador['nome']}: "))
    partidas.clear()
    for p in range(0, tot):
        partidas.append(int(input(f"QUANTOS GOLS NA {p + 1}ª partida: ")))
    #jogador['partidas'] = tot
    jogador['gols'] = partidas[:] # adiciona no dicionario jogador, os gols de cada partida
    jogador['total'] = sum(partidas) # soma dos gols das partidas
    time.append(jogador.copy())     # feito uma copia todos os dados do dicionario jogador para a  lista time,
    #print(jogador)
    while True:
        resp = str(input("Deseja continuar[S/N] ").upper())[0]
        if resp in 'SN':
            break
        print('ERROR: Utilize S ou N.')
    if resp == 'N':
        break
#cabeçalho
print('cod ', end="")
for i in jogador.keys():
    print(f'{i:<15}', end="")
print()
#fim cabeçalho
print('-' *40)
for k, v in enumerate(time):
    print(f"{k:>2} ", end="")
    for d in v.values():
        print(f'{str(d):<15}', end="")
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERROR! Não existe jogador com o código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}--')
        for i, g in enumerate(time[busca]["gols"]):
            print(f' No jogo {i+1}, fez {g} gols.')
    print('-'*40)
print('<<<VOLTE SEMPRE>>>')


