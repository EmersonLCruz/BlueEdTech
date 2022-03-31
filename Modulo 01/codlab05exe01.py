'''Faça a importação do módulo Pandas
Crie um Dataframe com as séries: Nome, Idade, prato favorito. Preencha com seus dados e da sua família. Fique a vontade para adicionar 
novas colunas.
Qual a idade média da sua família?
Qual a maior e a menor idade de sua família?'''

import pandas as pd

familia = { 'nome':['Ana','Bianca','Carlos','Daniel','Elaine'], 
            'idade':[15,20,22,10,27], 
            'prato_favorito':['Pizza','Churrasco','Sopa','Salada','Sushi']}

df = pd.DataFrame(familia)

print(f"A idade média da familia é {df['idade'].mean()}")
print(f"A maior idade é {df['idade'].max()}")
print(f"A menor idade é {df['idade'].min()}")