# Peça um programa que o usuário deve digitar um número par e caso seja digitado um número ímpar, o programa deve repetir o pedido. Quando o número par for digitado, exiba a seguinte mensagem: Tarefa concluída

while True:
    numero = int(input("Digite um número par: "))
    if numero % 2 == 0:
        print("Tarefa Concluída!")
        break
    else:
        print("Número digitado NÃO é PAR")