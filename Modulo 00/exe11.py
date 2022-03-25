# Faça um programa que peça dois números, imprima o maior deles ou imprima "Números iguais" se os números forem iguais.
n1 = int(input("Digite 1º número: "))
n2 = int(input("Digite 2º número: "))
if n1 > n2:
    print(f"O maior valor é {n1}")
elif n1 < n2:
    print(f"O maior valor é {n2}")
else:
    print("Números iguais.")