'''Alice e Bia criaram uma página na Internet com informações sobre o Macaco-prego-de-peito-amarelo, uma espécie em extinção. A página mostra como todos podem ajudar a manter o habitat natural para evitar que a espécie seja extinta.
Uma empresa gostou tanto da iniciativa de Alice e Bia que prometeu doar um prêmio para que as duas amigas possam realizar outras iniciativas semelhantes. A empresa decidiu que o prêmio seria dado quando a soma do número de acessos à página chegasse a 1 milhão.
Dada a lista de acessos diários que ocorreram à página de Alice e Bia, escreva um programa para determinar quantos dias foram necessários para a soma dos acessos chegar a 1 milhão e as amigas ganharem o prêmio.'''
total = 0 
cont = 1
n = int(input("Informe o número de dias da lista: "))
for x in range(0,n):
    a = int(input(f"Quantidade de acesso no {x+1}º dia: "))
    total += a
    if total < 1000000:
        cont += 1
print(f"Quantidade de dias para meta: {cont}")