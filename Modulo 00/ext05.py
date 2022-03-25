'''Bruno é um menino que gosta muito de ver televisão. No entanto ele se depara com um problema muito chato. Sempre que começa um novo programa no canal preferido dele, a TV Nlogônia, acontece de o volume do som deste programa estar diferente do anterior, às vezes com volume menor, outras vezes com volume maior. Quando está com volume menor, ele aumenta o volume pressionando uma quantidade de vezes seguidas o botão de aumentar para o volume ficar ideal; a mesma coisa acontece quando está um volume maior, e ele diminui o volume pressionando alguma quantidade de vezes seguidas o botão de diminuir o volume para ficar com o volume que ele goste no momento.
O aparelho de TV dele tem umas peculiaridades: ele possui volume mínimo, com valor 0 (também chamado de mudo), e volume máximo, com valor 100. A TV nunca ultrapassa os volumes máximo e mínimo. Por exemplo, se o volume já estiver no máximo e ele pressionar o botão de aumentar o som, o volume não se altera. Da mesma forma, se o volume estiver no valor mínimo e ele pressionar o botão de diminuir o som, o volume não se altera.
Agora Bruno quer sua ajuda: ele lembra qual era o volume inicial da TV, e quantas vezes ele pressionou cada botão. Mas, como foram várias mudanças de volume, ele não sabe qual é o volume atual da TV. Por isso, pediu que você o ajude a calcular qual é o volume atual, dados o volume inicial e a lista de trocas de volume que ele realizou.'''

v = int(input("Digite valor inicial do Volume: "))
t = int(input("Informe quantidade de troca de volume: "))
for x in range(0,t):
    auteracaoVolume = int(input(f"Digite valor da {x+1}º troca: "))
    soma = auteracaoVolume + v
    if soma > 100:
        v = 100
    elif soma < 0:
        v = 0
    else:
        v = soma

print(f"Volume final: {v}")