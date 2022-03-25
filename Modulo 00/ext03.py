# Por lei, na Nlogônia todas as barras de chocolate são quadradas. Anamaria tem uma barra quadrada de chocolate de lado L, que ela quer compartilhar com alguns colegas da obi. Mas ela é uma boa cidadã e cumpre a lei. Então, ela divide a barra em quatro pedaços quadrados, de lado L=L/2. Depois, ela repete esse procedimento com cada pedaço gerado, sucessivamente, enquanto o lado for maior do que, ou igual a 2cm. Você deve escrever um programa que, dado o lado L da barra inicial, em centímetros, determina quantos pedaços haverá ao final do processo.

l = int(input("Digite o valor de L: "))
quantidade = 1
while l >= 2:
    quantidade *= 4
    l = int(l / 2)
print(quantidade)