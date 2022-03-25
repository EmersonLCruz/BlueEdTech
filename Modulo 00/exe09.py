'''Faça um programa que pergunte ao usuário um número e valide se o numero é par ou impar:
Crie uma variável para receber o valor, com conversão para inteiro
Para um número ser par, a divisão dele por 2 tem que dar resto 0'''
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("Você digitou um número PAR!")
else:
    print("Você digitou um número IMPAR!")