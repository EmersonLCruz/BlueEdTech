# Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo e implemente a funcionalidade de não aceitar o número 0.
while True:
    numero = int(input("Digite um número diferente de 0: "))
    if numero > 0:
        print("Você digitou um número POSITIVO!")
        break
    elif numero < 0:
        print("Você digitou um número NEGATIVO!")
        break
    else:
        print("Valor INVALIDO!")