'''Um novo game de realidade aumentada tem, dentro dele, um mini-game que aparece em certas situações para aumentar o ganho de pontos do game principal. O mini-game é um joguinho de memória com quatro cartas, formando dois pares de cartas iguais. Quer dizer, duas cartas têm um número inteiro N marcado em uma de suas faces e as outras duas cartas têm um outro número inteiro M, N != M. Neste problema, o jogador já virou três cartas.
Claro que, dadas as condições, a carta que falta virar vai formar par com uma das três que já foram viradas. Implemente um programa que, dados os números de três cartas, imprima o número da carta que ainda falta virar!'''
carta = [int(input()),int(input()),int(input())]
if carta[0] != carta[1] and carta[2]:
    c4 = carta[0]
    #print(c4)
if carta[1] != carta[0] and carta[1] != carta[2]:
    c4 = carta[1]
    #print(c4)
if carta[2] != carta[0] and carta[2] != carta[1]:
    c4 = carta[2]
print(f"proxima carta: {c4}")