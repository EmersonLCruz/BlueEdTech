'''E os 10% do garçom?
Defina uma variável para o valor de uma refeição que custou R$ 42,54;
Defina uma variável para o valor da taxa de serviço que é de 10%;
Defina uma variável que calcula o valor total da conta e exiba-o no console com essa formatação: R$ 9999.99.'''
refeicao = 42.54
taxaServico = 0.1
valorTotal = refeicao + (refeicao * taxaServico)
print(f"Valor total da refeição R${valorTotal:.2f}")