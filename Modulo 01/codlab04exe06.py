# Escreva um programa que liste todos os números de -100 a 100 (com os extremos incluídos) e que todo múltiplo de 3 e 4 seja substituído pela palavra Aqui.

for x in range(-100,101):
    if x % 3 == 0 and x % 4 == 0:
        print("Aqui")
    else:
        print(x)