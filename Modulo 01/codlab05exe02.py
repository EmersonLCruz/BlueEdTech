'''Faça uma pesquina na internet e busque os seguintes dados:
Nome dos estados brasileiros;
Sigla dos estados;
Região;
Capital;
Polulação.
Adicione estas informações em um Datafrane;
Exiba na tela apenas a sigla e a população;
Qual o estado com a maior população?
Qual a quantidade de estados?
Crie novos Dataframes a partir do conjunto principal. Crie um Dataframe para cada uma das regiões.
Quantidade de estados por região?
Polulação total de cada região?
Qual região com a maior população?
Qual a regiçao com a menor população?
Qual a população média de cada região?'''

import pandas as pd

arquivo = pd.read_excel('Modulo 01\datasets\populacao-e-pib-por-estados.xlsx')
df = pd.DataFrame(arquivo)

#print(df[['Sigla','População']])


# Verificar Estado com maior população
'''index_maior_populacao = df['População'].idxmax()
print(f"O estado com maior população é {df.iloc[index_maior_populacao]['Estado']}, com {df.iloc[index_maior_populacao]['População']} de habitantes.")
print(df.iloc[index_maior_populacao]['Estado'] ,  df.iloc[index_maior_populacao]['População'])'''

# Qual a quantidade de Estados
#print(len(df.index)-1)

# Criar novos DataFrames
norte = df['Região'] == 'Norte'
norte = df[norte]

nordeste = df['Região'] == 'Nordeste'
nordeste = df[nordeste]

centro_oeste = df["Região"] == 'Centro-Oeste'
centro_oeste = df[centro_oeste]

sudeste = df['Região'] == 'Sudeste'
sudeste = df[sudeste]

sul = df['Região'] == 'Sul'
sul = df[sul]

# Calcular números de Estados por região
#print(f"Norte: {len(norte.index)}")
#print(f"Nordeste: {len(nordeste.index)}")
'''print(f"Centro-Oeste: {len(centro_oeste.index)-1}")
print(f"Sudeste: {len(sudeste.index)}")
print(f"Sul: {len(sul.index)}")

# Polulação total de cada região
print(f"Norte: {norte['População'].sum()}")
print(f"Nordeste: {nordeste['População'].sum()}")
print(f"Centro-Oeste: {centro_oeste['População'].sum()}")
print(f"Sudeste: {sudeste['População'].sum()}")
print(f"Sul: {sul['População'].sum()}")'''

# Qual região com a maior população?
if sudeste['População'].sum() > nordeste['População'].sum():
    print(sudeste['Região'].unique(), ": ",sudeste['População'].sum())



# Qual a regiçao com a menor população?
# Qual a população média de cada região?
