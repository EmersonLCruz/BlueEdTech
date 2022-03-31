from sklearn import datasets
import pandas as pd
import numpy as np

iris = datasets.load_iris()
dados = pd.DataFrame(data= np.c_[iris['data'], iris['target']], columns= iris['feature_names'] + ['target'])

target2 = []
target3 = []


def arvore_modelo01(sl,sw,pl,pw):
    global target2
    if pl <= 2.45:
        print('setosa')
        target2.append(0.0)
    else:
        if pw <= 1.75:
            if pl <= 4.95:
                if pw <= 1.65:
                    print('versicolor')
                    target2.append(1.0)
                else:
                    print('virginica')
                    target2.append(2.0)
            else:
                if pw <= 1.55:
                    print('virginica')
                    target2.append(2.0)
                else:
                    print('versicolor')
                    target2.append(1.0)
        else:
            if pl <= 4.85:
                if sw <= 3.1:
                    print('virginica')
                    target2.append(2.0)
                else:
                    print('versicolor')
                    target2.append(1.0)
            else:
                print('virginica')
                target2.append(2.0)
    


def arvore_modelo02(sl,sw,pl,pw):
    global target3
    if pl <= 2.45:
        print('setosa')
        target3.append(0.0)
    else:
        if pw <= 1.75:
            print('versicolor')
            target3.append(1.0)
        else:
            print('virginica')
            target3.append(2.0)

def acuracia(acerto,tamanho_amostra):
    accuracy = acerto/tamanho_amostra
    return accuracy


print("="*30)
print("MODELO 01".center(30))
print("="*30)
for i in dados.index:
    arvore_modelo01(dados['sepal length (cm)'][i],dados['sepal width (cm)'][i],dados['petal length (cm)'][i],dados['petal width (cm)'][i])
print("="*30)
dados['target2'] = target2
#dados.to_excel('Blue\BlueEdTech\iris02.xlsx')
tamanho_rows = len(dados.index)
cont = 0
print("="*30)
print("MODELO 02".center(30))
print("="*30)
while cont < tamanho_rows:
    arvore_modelo02(dados['sepal length (cm)'][cont],dados['sepal width (cm)'][cont],dados['petal length (cm)'][cont],dados['petal width (cm)'][cont])
    cont += 1

dados['target3'] = target3
#dados.to_excel('Blue\BlueEdTech\iris03.xlsx')
print("="*100)
print("ANALISE MODELO 01".center(100))
print("="*100)
acertos = erros = 0
for i in dados.index:
    if dados['target'][i] == dados['target2'][i]:
        acertos += 1
    else:
        erros += 1
print(f"O modelo utilizado acertou: {acertos} iris em sua classificação")
print("Abaixo segue tabela de erros")
filtro = dados['target'] != dados['target2']
filtro = dados[filtro]
print(filtro)

ac = acuracia(acertos,tamanho_rows)
print(f"Accuracy: {ac}")
print("="*100)
print("ANALISE MODELO 02".center(100))
print("="*100)
acertos = erros = 0
for i in dados.index:
    if dados['target'][i] == dados['target3'][i]:
        acertos += 1
    else:
        erros += 1
print(f"O modelo utilizado acertou: {acertos} iris em sua classificação")
print("Abaixo segue tabela de erros")
filtro2 = dados['target'] != dados['target3']
filtro2 = dados[filtro2]
print(filtro2)

ac = acuracia(acertos,tamanho_rows)
print(f"Accuracy: {ac}")
print("="*100)