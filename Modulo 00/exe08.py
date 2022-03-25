'''Conversor de moedas: Crie um programa que solicite um um valor em real ao usuário e converta esse valor, para:
DOLAR
EURO
LIBRA ESTERLINA
DÓLAR CANADENSE
PESO ARGENTINO
PESO CHILENO
Para esse exercício você precisará realizar uma pesquisa para saber a cotação de cada moeda em real. Mostrar o resultado no formato U$9999.99'''

real = float(input("Digite valor para conversão R$ "))
dolar = real / 5.5611012
euro = real / 6.3524007
dolarCanadense = real / 4.4456991
pesoChileno = real / 0.006742
pesoArgentino = real / 0.05366

print(f"Valor convertido em:\nDolar U${dolar:.2f}\nEuro €${euro:.2f}\nDolar Canadense C${dolarCanadense:.2f}\nPeso Chileno CLP${pesoChileno:.2f}\nPeso Argentino ${pesoArgentino:.2f}")