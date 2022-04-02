from sklearn import datasets
import pandas as pd
import numpy as np

iris = datasets.load_iris()
dados = pd.DataFrame(data= np.c_[iris['data'], iris['target']], columns= iris['feature_names'] + ['target'])

target2 = []



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
    


def arvore_modelo02(dados):
    target3 = -1
    if dados['petal length (cm)'] <= 2.45:
        print('setosa')
        target3 = 0.0
    else:
        if dados['petal width (cm)'] <= 1.75:
            print('versicolor')
            target3 = 1.0
        else:
            print('virginica')
            target3 = 2.0
    return target3

def acuracia(acerto,tamanho_amostra):
    accuracy = acerto/tamanho_amostra
    return accuracy

# Rodando modelo 01 com For explicito
print("="*30)
print("MODELO 01".center(30))
print("="*30)
for i in dados.index:
    arvore_modelo01(dados['sepal length (cm)'][i],dados['sepal width (cm)'][i],dados['petal length (cm)'][i],dados['petal width (cm)'][i])
print("="*30)
dados['target2'] = target2

# Rodando Modelo 02 usando função apply
print("="*30)
print("MODELO 02".center(30))
print("="*30)
dados['target3'] = dados.apply(arvore_modelo02,axis=1)


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
print(filtro.drop(columns=['target3']))

tamanho_rows = len(dados.index)
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
print(filtro2.drop(columns=['target2']))

ac = acuracia(acertos,tamanho_rows)
print(f"Accuracy: {ac}")
print("="*100)