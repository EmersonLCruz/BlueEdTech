# A natação foi um dos esportes mais emocionantes das Olimpíadas do Rio. Houve até uma prova na qual três atletas chegaram empatados, cada um recebendo uma medalha de prata! Normalmente, porém, os três primeiros colocados terminam a prova em tempos distintos e, portanto, temos a distribuição mais comum de medalhas: o nadador que terminou no menor tempo recebe medalha de ouro; o nadador que terminou com o segundo menor tempo recebe medalha de prata; e o que terminou com o terceiro menor tempo recebe medalha de bronze. Neste problema, dados os três tempos distintos de finalização da prova, dos três nadadores que ganharam medalhas, seu programa deve dizer quem ganhou medalha de ouro, quem ganhou prata e quem ganhou bronze.
medalha = []
t1 = int(input("Digite tempo: "))
t2 = int(input("Digite tempo: "))
t3 = int(input("Digite tempo: "))

if t2 > t1 < t3:
    medalha.append(1)
elif t2 < t1 > t3:
    medalha.append(3)
else:
    medalha.append(2)
if t1 > t2 < t3:
    medalha.append(1)
elif t1 < t2 > t3:
    medalha.append(3)
else:
    medalha.append(2)
if t1 > t3 < t2:
    medalha.append(1)
elif t1 < t3 > t2:
    medalha.append(3)
else:
    medalha.append(2)
print(medalha)