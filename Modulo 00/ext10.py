# A turma do colégio vai fazer uma excursão na serra e todos os alunos e monitores vão tomar um bondinho para subir até o pico de uma montanha. A cabine do bondinho pode levar 50 pessoas no máximo, contando alunos e monitores, durante uma viagem até o pico. Neste problema, dado como entrada o número de alunos A e o número de monitores M, você deve escrever um programa que diga se é possível ou não levar todos os alunos e monitores em apenas uma viagem!

a = int(input("Digite número de alunos: "))
m = int(input("Digite número de monitores: "))
pessoas = a + m
lotacao = "S" if pessoas <= 50 else "N"
print(lotacao)