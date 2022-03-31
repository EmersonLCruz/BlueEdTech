# Escreva um programa que dado um número de 3 dígitos, a soma do cubo de cada dígito é igual ao próprio número. Por exemplo 1³ + 5³ + 3³ = 153.

numero = input("Digite um número inteiro: ")
soma = 0

for x in numero:
    soma += int(x)**len(numero)
print(soma)

if soma == int(numero):
    print("Número de Armstrong")
else:
    print("Não é um número Armstrong")

'''OBS: O enunciado solicita algo que não é valido para todos os números, são alguns números que atendem essa condição que são chamados
de números Armstrong'''