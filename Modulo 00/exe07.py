'''Você está na flor da idade?
Defina uma variável para o valor do ano do nascimento;
Defina uma variável para o valor do ano atual;
Defina uma variável que calcula o valor final da idade da pessoa;
Exiba uma mensagem final dizendo a idade da pessoa e a mensagem "Você está na flor da idade".'''
from datetime import date

nascimento = int(input("Digite o ano do seu nascimento: "))
anoAtua = date.today().year
idade = anoAtua - nascimento
print(f"Você tem {idade} ano(s), você esta na flor da idade.")

