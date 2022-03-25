'''Você está de volta em seu hotel na Tailândia depois de um dia de mergulhos. O seu quarto tem duas lâmpadas. Vou chamá-las de A e B. No hotel há dois interruptores, que chamaremos de I1 e I2. Ao apertar I1, a lâmpada A troca de estado, ou seja, acende se estiver apagada e apaga se estiver acesa. Se apertar I2, ambas as lâmpadas A e B trocam de estado. As lâmpadas inicialmente estão ambas apagadas. Seu amigo resolveu bolar um desafio para você. Ele irá apertar os interruptores em uma certa sequência, e gostaria que você respondesse o estado final das lâmpadas A e B.'''
l1 = l2 = False
opcao = 0
n = int(input("Digite quantidades de apertos no interruptor: "))
for x in range(0,n):
    opcao = int(input(""))
    if opcao == 1 and l1 == False:
        l1 = True
    elif opcao == 1 and l1 == True:
        l1 = False
    elif opcao == 2:
        if l1 == False:
            l1 = True
        else:
            l1 = False
        if l2 == False:
            l2 = True
        else:
            l2 = False

print(f"l1: {l1}, l2: {l2}")
