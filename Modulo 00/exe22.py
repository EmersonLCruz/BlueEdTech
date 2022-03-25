'''Jogo de dados: Crie um programa onde jogadores joguem um dado e tenham resultados aleatórios.
O programa tem que:
Perguntar quantas rodadas você quer fazer; ok
Perguntar quantos jogadores vão jogar; ok
Criar um objeto pra cada jogador com nome e número tirado; ok
Guarda todos os objetos em uma lista; ok
Ordenar esses objetos, sabendo que o vencedor tirou o maior número no dado.ok
Mostrar no final qual jogador ganhou mais rodadas e foi o grande campeão.ok'''

from random import randint
igual = maior = 0
aux = []
grupo = []
jogador = {}
jogadas = []
numeroJogador = int(input("Digite quantidade de jogadores: "))
numeroRodada = int(input("Digite quantidade de rodadas: "))

for x in range(0,numeroJogador): # Recebe o nome dos jogadores
    jogador['nome'] = input(f"Digite o nome do {x+1}º jogador: ")
    jogador['v'] = 0
    for y in range(0,numeroRodada): # Inclue o resultado de cada jogador
        jogadas.append(randint(1,6))  
    jogador['Rodadas'] = jogadas[:]
    grupo.append(jogador.copy())
    jogador.clear()
    jogadas.clear()

for x in range(0,len(grupo)): # Imprime as jogadas de Cada jogador
    print(f"Jogador: {grupo[x]['nome']}, Jogadas: {grupo[x]['Rodadas']}")

for x in range(0,numeroRodada): # Verifica quem é o vitorioso em cada rodada
    aux.clear()
    print(f"{x+1}ª Rodada")
    for y in range(0,numeroJogador):
        aux.append(grupo[y]['Rodadas'][x])
    maior = max(aux)
    igual = aux.count(maior)
    vencedor = aux.index(maior)
    if igual > 1:
        print(f"Houve um empate entre {igual} jogadores")
    else:
        print(f"Vitoria de {grupo[vencedor]['nome']}")
        vitorias = grupo[vencedor]['v'] 
        vitorias += 1
        grupo[vencedor]['v'] = vitorias
aux.clear()

for x in range(0,len(grupo)):
    vitorias = grupo[x]['v']
    aux.append(vitorias)
maior = max(aux)
igual = aux.count(maior)
vencedor = aux.index(maior)
if igual > 1:
    print(f"Houve um empate entre {igual} jogadores")
else:
    print(f"O grande campeão é {grupo[vencedor]['nome']}")

