'''Gabriel inventou um código para representar números naturais, usando uma sequência de zeros e uns. Funciona assim, o número natural é representado pela quantidade de vezes que o padrão 100 aparece na sequência. Por exemplo, na sequência 11101001010011110, o padrão aparece duas vezes; e na sequência 11101010111110111010101 ele não aparece nenhuma vez. Você deve ajudar Gabriel e implementar um programa que, dada a sequência de zeros e uns, calcule quantas vezes o padrão 100 aparece nela.'''
n = []
cont = 0
tamanhoSequencia = int(input("Entre com o tamanho da sequencia: "))
for x in range(0,tamanhoSequencia):
    n.append(int(input(f"Valor {x+1}: ")))
for x in range(0,len(n)-2):
    if n[x] == 1 and n[x+1] == 0 and n[x+2] == 0:
        cont += 1

print(f"Quantidade de vezes que aparece a sequencia 100: {cont}")