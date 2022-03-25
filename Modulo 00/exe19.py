# Jogo da adivinhação: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 10 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
numero = random.randint(0,10)
print('Pensei em um número entre 0 e 10, você consegue descobrir qual foi?')
valor = int(input('Digite o número que você acha que pensei:'))
if valor == numero:
    print('Parabens! Acertou!')
else:
    print(f'Você errou o número que pensei foi {numero}')