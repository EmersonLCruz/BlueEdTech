# Faça um programa que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições:
from datetime import date
anoAtual = date.today().year
nascimento = int(input("Digite o ano do seu nascimento: "))
idade = anoAtual - nascimento
if idade < 16:
    print("Voto NEGADO")
elif (16 <= idade < 18) or (idade >= 65):
    print("Voto OPCIONAL")
else:
    print("Voto OBRIGATORIO")