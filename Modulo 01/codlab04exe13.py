''' A seguinte sequência 0, 1, 1, 2, 3, 5, 8, ... , conhecida como sequência de Fibonacci, é formada pela seguinte regra: 
o primeiro termo é 0, o segundo é 1, os próximos serão a soma dos dois anteriores. 
Escreva um programa que peça ao usuário um termo da sequência de Fibonacci e exiba-o na tela.'''

termo = int(input("Digite o termo de Fibonacci: "))
termo_primeiro = 0
termo_segundo = 1
fibonacci = 0

if termo == 1:
    print(f"O valor para o termo {termo} corresponde a {termo_primeiro}")
elif termo == 2:
    print(f"O valor para o termo {termo} corresponde a {termo_segundo}")
else:
    for x in range(2,termo):
        fibonacci = termo_primeiro + termo_segundo
        termo_primeiro,termo_segundo = termo_segundo,fibonacci

    print(f"O valor para o termo {termo} corresponde a {fibonacci}")