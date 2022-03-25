# Agora, imprima todas as tabuadas do número 1 ao 10.
for num in range(1,11):
    print("-"*20)
    for valor in range(1,11):
        print(f"{valor} x {num} = {num*valor}")