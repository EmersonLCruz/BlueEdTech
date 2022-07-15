'''Vamos explorar os dados do Titanic, gerando análises mais complexas.
Para as respostas, esperamos que descreva com suas palavras o resultado encontrado. Qual foi a lógica que usou e ao fim mostre o código.
Qual a quantidade de sobreviventes?
Qual a quantidade de sobreviventes por classe?
Qual o preço médio dos tickets?
Qual o maior e o menor ticket?
Entre os sobreviventes, identificou algum padrão que gostaria de compartilhar? Valor do ticket, classe?
Percentual de homens e mulheres sobreviventes?
Idade média geral dos tribulantes?
Idade média dos homens e das mulheres?
Idade média dos sobreviventes.
Faça outras análises e compartilhe.
Plotar um gráfico com o percentual de homens e mulheres.
Pesquise os tipos de gráficos. Você pode, por exemplo, montar um DF com o percentual e plotar num gráfico de pizza.
Plotar um gráfico por classe.
Plota um gráfico de plot.box() nos preços e tentar idenficiar Outliers.
Caso tenha identificado Outliers na atividade 13, alguma sugestão de resolução.
Plotar um gráfico de sobreviventes.'''

import pandas as pd
import matplotlib.pyplot as plt

arquivo = pd.read_csv('train.csv')
df = pd.DataFrame(arquivo)

# Quantidade de sobreviventes
sobreviventes = df[df['Survived'] == 1]
print(f"A quantidade de sobreviventes foram de {sobreviventes['Survived'].count()}")

# Quantidade de sobreviventes por classe
sobrevivente_class01 = sobreviventes[sobreviventes['Pclass'] == 1]
sobrevivente_class02 = sobreviventes[sobreviventes['Pclass'] == 2]
sobreviventes_class03 = sobreviventes[sobreviventes['Pclass'] == 3]

print(f"Sobreviventes Primeira Classe: {sobrevivente_class01['Survived'].count()}")
print(f"Sobreviventes Segunda Classe: {sobrevivente_class02['Survived'].count()}")
print(f"Sobreviventes Terceira Classe: {sobreviventes_class03['Survived'].count()}")

# Qual o preço médio dos tickets?
print(f"O preço médio da tarifa foi de ${df['Fare'].mean():.2f}")

# Qual o maior e o menor ticket?
print(f"O maior valor de Ticket foi de ${df['Fare'].max():.2f} e o menor foi de ${df['Fare'].min():.2f}")
# Entre os sobreviventes, identificou algum padrão que gostaria de compartilhar? Valor do ticket, classe?
print(sobrevivente_class01[['Pclass','Fare','Sex','Age']].sort_values('Fare'))
print(sobrevivente_class02[['Pclass','Fare','Sex','Age']].sort_values('Fare'))
print(sobreviventes_class03[['Pclass','Fare','Sex','Age']].sort_values('Fare'))

'''Entre os sobreviventes está um número maior de mulheres, quanto ao valor do ticket em alguns momentos os valores se chocam entre as
classes Ex: as tarifas compreendidas entre $25.92 à $56.49 foram tarifas pagas pelas três classes'''

# Percentual de homens e mulheres sobreviventes?

sobrevivente_class01_mulheres = sobrevivente_class01[sobrevivente_class01['Sex'] == 'female']
sobrevivente_class01_homens = sobrevivente_class01[sobrevivente_class01['Sex'] == 'male']
sobrevivente_class02_mulheres = sobrevivente_class02[sobrevivente_class02['Sex'] == 'female']
sobrevivente_class02_homens = sobrevivente_class02[sobrevivente_class02['Sex'] == 'male']
sobrevivente_class03_mulheres = sobreviventes_class03[sobreviventes_class03['Sex'] == 'female']
sobrevivente_class03_homens = sobreviventes_class03[sobreviventes_class03['Sex'] == 'male']
quant_sobreviventes = sobreviventes['Survived'].count()
print(f"Dos sobreviventes as mulheres totalizam um percentual: {(sobrevivente_class01_mulheres['Sex'].count() + sobrevivente_class02_mulheres['Sex'].count() + sobrevivente_class03_mulheres['Sex'].count())/quant_sobreviventes * 100:.2f}%")
print(f"Dos sobreviventes os homens totalizam um percentual: {(sobrevivente_class01_homens['Sex'].count() + sobrevivente_class02_homens['Sex'].count() + sobrevivente_class03_homens['Sex'].count())/quant_sobreviventes * 100:.2f}%")

# Idade média geral dos tribulantes?
print(f"A idade média dos tripulantes era de {int(df['Age'].mean())} anos")

#Idade média dos homens e das mulheres?
homens = df[df['Sex'] == 'male']
mulheres = df[df['Sex'] == 'female']
print(f"A idade média entre os homens era de {int(homens['Age'].mean())} anos")
print(f"A idade média entre as mulheres era de {int(mulheres['Age'].mean())} anos")

#Idade média dos sobreviventes.
print(f"A idade média dos sobreviventes era de {int(sobreviventes['Age'].mean())} anos")

#Faça outras análises e compartilhe.
#Plotar um gráfico com o percentual de homens e mulheres.
df['Age'].plot()
#Pesquise os tipos de gráficos. Você pode, por exemplo, montar um DF com o percentual e plotar num gráfico de pizza.
#Plotar um gráfico por classe.
#Plota um gráfico de plot.box() nos preços e tentar idenficiar Outliers.
#Caso tenha identificado Outliers na atividade 13, alguma sugestão de resolução.
#Plotar um gráfico de sobreviventes