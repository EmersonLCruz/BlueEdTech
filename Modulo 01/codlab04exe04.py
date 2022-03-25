# Pergunte ao usuário quantos números serão digitados, depois exiba a soma deles, a média, o menor, o maior, quantos números pares e quantos números ímpares foram digitados. Utilize o 0 como critério de parada.

qtd_numero = int(input("Quantos números deseja digitar? "))
numero = []
soma = media = 0
pares = []
impares = []
if qtd_numero <= 0:
    print("Fim da execução!")
    exit()
else:
    for x in range(0,qtd_numero):
        numero.append(int(input(f"Digite {x+1}º número: ")))

for valores in numero:
    soma += valores
    media = soma / len(numero)
    if valores % 2 == 0:
        pares.append(valores)
    else:
        impares.append(valores)
print(f"O menor valor digitado é {min(numero)}")
print(f"O maior valor digitado é {max(numero)}")
print(f"O media dos valores digitado é {media}")
print(f"Os números pares digitado foram {pares}")
print(f"Os números ímpares digitado foram {impares}")
