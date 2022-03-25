'''Neste projeto iremos fazer um jogo de detetive com tudo oque aprendemos até aqui.
este jogo deve funcionar da seguinte forma:
O programa deve fazer 5 perguntas ao usuario com respostas de sim ou não
Caso o usuario responda sim a 4 perguntas ou mais, devemos retornar que ele é culpado
Caso o usuario responda sim a 3 perguntas, devemos retornar que ele é suspeito
Caso o usuario responda sim a 2 perguntas ou menos, devemos retornar que ele é inocente
Criterios de aceitação:
Precisa retornar resposta para todas as possibilidades de culpado,suspeito ou inocente.
Precisa ter condicionais.'''

interrogatorio = [input("Esteve no local do crime? S/N:").upper().strip()[0],
input("Mora perto da vítima? S/N:").upper().strip()[0],
input("Telefonou para a vítima? S/N:")[0].upper().strip(),
input("Já trabalhou com a vítima? S/N:")[0].upper().strip(),
input("Devia para a vítima? S/N:")[0].upper().strip()
]
respostas = interrogatorio.count('S')
if respostas <= 2:
    print("INOCENTE")
elif respostas == 3:
    print("SUSPEITO")
else:
    print("CULPADO")