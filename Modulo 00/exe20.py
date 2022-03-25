'''Caixa eletrônico: Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''
valor = int(input('Digite valor do saque: R$ '))
if (valor < 10) or (valor > 600):
    print("Valor Indisponivel para Saque")
else:
    cem = int(valor / 100)
    total = int(valor % 100)
    cinquenta = int(total / 50)
    total = int(total % 50)
    dez = int(total / 10)
    total = int(total % 10)
    cinco = int(total / 5)
    total = int(total % 5)

    print(f"notas de R$ 100,00 = {cem}")
    print(f'notas de R$ 50,00 = {cinquenta}')
    print(f'Notas de R$ 10,00 = {dez}')
    print(f'Notas de R$ 5,00 = {cinco}')
    print(f'Notas de R$ 1,00 = {total}')