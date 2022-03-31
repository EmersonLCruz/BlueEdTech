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

print("="*60)
print(" POPULAÇÃO POR ESTADOS".center(60))
print("="*60)
print(df[['Sigla','População']])


# Verificar Estado com maior população
index_maior_populacao = df['População'].idxmax()
print(f"O estado com maior população é {df.iloc[index_maior_populacao]['Estado']}, com {df.iloc[index_maior_populacao]['População']} de habitantes.")


# Qual a quantidade de Estados
print(f"A quantidades de Estados brasileiros é de {len(df.index)-1} + o Distrito Federal")
print("="*60)
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
print("NUMERO DE ESTADOS POR REGIÃO".center(60))
print("="*60)
print(f"Norte: {len(norte.index)}")
print(f"Nordeste: {len(nordeste.index)}")
print(f"Centro-Oeste: {len(centro_oeste.index)-1} + Distrito Federal")
print(f"Sudeste: {len(sudeste.index)}")
print(f"Sul: {len(sul.index)}")
print("="*60)
# Polulação total de cada região
print("POPULAÇÃO TOTAL POR REGIÃO".center(60))
print("="*60)
print(f"Norte: {norte['População'].sum()}")
print(f"Nordeste: {nordeste['População'].sum()}")
print(f"Centro-Oeste: {centro_oeste['População'].sum()}")
print(f"Sudeste: {sudeste['População'].sum()}")
print(f"Sul: {sul['População'].sum()}")

# Qual região com a maior população?
if norte['População'].sum() > nordeste['População'].sum() and norte['População'].sum() > centro_oeste['População'].sum() and norte['População'].sum() > sudeste['População'].sum() and norte['População'].sum() > sul['População'].sum():
    print(f"A Região com maior população é {norte['Região'].unique().item()} com {norte['População'].sum()} habitantes")
elif nordeste['População'].sum() > norte['População'].sum() and nordeste['População'].sum() > centro_oeste['População'].sum() and nordeste['População'].sum() > sudeste['População'].sum() and nordeste['População'].sum() > sul['População'].sum():
    print(f"A Região com maior população é {nordeste['Região'].unique().item()} com {nordeste['População'].sum()} habitantes")
elif centro_oeste['População'].sum() > norte['População'].sum() and centro_oeste['População'].sum() > nordeste['População'].sum() and centro_oeste['População'].sum() > sudeste['População'].sum() and centro_oeste['População'].sum() > sul['População'].sum():
    print(f"A Região com maior população é {centro_oeste['Região'].unique().item()} com {centro_oeste['População'].sum()} habitantes")
elif sudeste['População'].sum() > norte['População'].sum() and sudeste['População'].sum() > centro_oeste['População'].sum() and sudeste['População'].sum() > nordeste['População'].sum() and sudeste['População'].sum() > sul['População'].sum():
    print(f"A Região com maior população é {sudeste['Região'].unique().item()} com {sudeste['População'].sum()} habitantes")
else:
    print(f"A Região com maior população é {sul['Região'].unique().item()} com {sul['População'].sum()} habitantes")


# Qual a regiçao com a menor população?
if norte['População'].sum() < nordeste['População'].sum() and norte['População'].sum() < centro_oeste['População'].sum() and norte['População'].sum() < sudeste['População'].sum() and norte['População'].sum() < sul['População'].sum():
    print(f"A Região com menor população é {norte['Região'].unique().item()} com {norte['População'].sum()} habitantes")
elif nordeste['População'].sum() < norte['População'].sum() and nordeste['População'].sum() < centro_oeste['População'].sum() and nordeste['População'].sum() < sudeste['População'].sum() and nordeste['População'].sum() < sul['População'].sum():
    print(f"A Região com menor população é {nordeste['Região'].unique().item()} com {nordeste['População'].sum()} habitantes")
elif centro_oeste['População'].sum() < norte['População'].sum() and centro_oeste['População'].sum() < nordeste['População'].sum() and centro_oeste['População'].sum() < sudeste['População'].sum() and centro_oeste['População'].sum() < sul['População'].sum():
    print(f"A Região com menor população é {centro_oeste['Região'].unique().item()} com {centro_oeste['População'].sum()} habitantes")
elif sudeste['População'].sum() < norte['População'].sum() and sudeste['População'].sum() < centro_oeste['População'].sum() and sudeste['População'].sum() < nordeste['População'].sum() and sudeste['População'].sum() < sul['População'].sum():
    print(f"A Região com menor população é {sudeste['Região'].unique().item()} com {sudeste['População'].sum()} habitantes")
else:
    print(f"A Região com menor população é {sul['Região'].unique().item()} com {sul['População'].sum()} habitantes")
print("="*60)

# Qual a população média de cada região?
print("POPULAÇÃO MÉDIA POR REGIÃO".center(60))
print("="*60)
print(f"Norte: {norte['População'].sum() // len(norte.index)}")
print(f"Nordeste: {nordeste['População'].sum() // len(nordeste.index)}")
print(f"Centro-Oeste: {centro_oeste['População'].sum() // len(centro_oeste.index)}")
print(f"Sudeste: {sudeste['População'].sum() // len(sudeste.index)}")
print(f"Norte: {sul['População'].sum() // len(sul.index)}")
print("="*60)