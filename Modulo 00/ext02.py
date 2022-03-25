# Dois times, Cormengo e Flaminthians, participam de um campeonato de futebol, juntamente com outros times. Cada vitória conta três pontos, cada empate um ponto. Fica melhor classificado no campeonato um time que tenha mais pontos. Em caso de empate no número de pontos, fica melhor classificado o time que tiver maior saldo de gols. Se o número de pontos e o saldo de gols forem os mesmos para os dois times então os dois times estão empatados no campeonato. Dados os números de vitórias e empates, e os saldos de gols dos dois times, sua tarefa é determinar qual dos dois está melhor classificado, ou se eles estão empatados no campeonato.

times = {'Cormengo':[int(input("Cv: "))*3,int(input("Ce: ")),int(input("Cs: "))],'Flaminthias':[int(input("Fv: "))*3,int(input("Fe: ")),int(input("Fs: "))]}

pontosCormengo = times["Cormengo"][0] + times["Cormengo"][1]
pontosFlaminthias = times["Flaminthias"][0] + times["Flaminthias"][1]

if pontosCormengo == pontosFlaminthias:
   if times["Flaminthias"][2] < times["Cormengo"][2]:
       print("C")
   elif times["Flaminthias"][2] > times["Cormengo"][2]:
        print("F")
   else:
        print("=")
elif pontosCormengo < pontosFlaminthias:
    print("F")
else:
    print("C")