# Escreva um programa que dê a tabuada dos números de 1 a 10.

for x in range(1,11):
    print(f"\nTabuada de {x}\n")
    for y in range(1,11):
        print(f"{x} x {y} = {x*y}")