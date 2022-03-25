# Peça ao usuário uma palavra e a devolva com as letras ao contrário. Caso a palavra seja a mesma nos dois sentidos, imprima uma mensagem dizendo que é um palíndromo.
palavra = input("Digite uma palavra: ").upper().strip()
palavra_invertida = ""

for letra in range(len(palavra)-1,-1,-1): # Pecorrer todas as letras começando pelo ultimo index e terminando em 0 de forma decrescente
    palavra_invertida += palavra[letra]
print(f"A palavra invertida é {palavra_invertida}")
if palavra == palavra_invertida:
    print("A palavra digitada é uma PALÍNDROMA")