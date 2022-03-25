# Faça um programa de cadastro de clientes que mostre um menu de opções e permita com que a pessoa escolha umas das opções, exibindo qual foi a opção escolhida.
print("-"*20)
print("Cadastro de Clientes".center(20))
print("-"*20)
print("""[1] Novo
[2] Alterar
[3] Excluir
[4] Sair""")
opcao = (input("Digite sua opção: "))
while opcao not in '1234':
    print("Opção INVALIDA!")
    opcao = (input("Digite sua opção: "))
if opcao == '1':
    print("Opção escolhida -> Novo")
elif opcao == '2':
    print("Opção escolhida -> Alterar")
elif opcao == '3':
    print("Opção escolhida -> Excluir")
else:
    print("Opção escolhida -> Sair")

