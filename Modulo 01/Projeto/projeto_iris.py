
from sklearn import datasets
import pandas as pd
import numpy as np

iris = datasets.load_iris()
dados = pd.DataFrame(data= np.c_[iris['data'], iris['target']], columns= iris['feature_names'] + ['target'])




cont_setosa = 0
cont_versicolor =0
cont_virginica = 0
cont = 0
target2 = []


def arvore_modelo01(sl,sw,pl,pw):
    global cont_setosa
    global cont_versicolor
    global cont_virginica
    global target2
    if pl <= 2.45:
        print('setosa')
        cont_setosa += 1
        target2.append(0.0)
    else:
        if pw <= 1.75:
            if pl <= 4.95:
                if pw <= 1.65:
                    print('versicolor')
                    cont_versicolor += 1
                    target2.append(1.0)
                else:
                    print('virginica')
                    cont_virginica += 1
                    target2.append(2.0)
            else:
                if pw <= 1.55:
                    print('virginica')
                    cont_virginica += 1
                    target2.append(2.0)
                else:
                    print('versicolor')
                    cont_versicolor += 1
                    target2.append(1.0)
        else:
            if pl <= 4.85:
                if sw <= 3.1:
                    print('virginica')
                    cont_virginica += 1
                    target2.append(2.0)
                else:
                    print('versicolor')
                    cont_versicolor += 1
                    target2.append(1.0)
            else:
                print('virginica')
                cont_virginica += 1
                target2.append(2.0)
    


def arvore_modelo02(sl,sw,pl,pw):
    global cont_setosa
    global cont_versicolor
    global cont_virginica
    global target2
    if pl <= 2.45:
        print('setosa')
        cont_setosa += 1
        target2.append(0.0)
    else:
        if pw <= 1.75:
            print('versicolor')
            cont_versicolor += 1
            target2.append(1.0)
        else:
            print('virginica')
            cont_virginica += 1
            target2.append(2.0)



for i in dados.index:
    arvore_modelo01(dados['sepal length (cm)'][i],dados['sepal width (cm)'][i],dados['petal length (cm)'][i],dados['petal width (cm)'][i])

dados['target2'] = target2
#dados.to_excel('Blue\BlueEdTech\iris02.xlsx')

tamanho_rows = len(dados.index)



while cont < tamanho_rows:
    arvore_modelo02(dados['sepal length (cm)'][cont],dados['sepal width (cm)'][cont],dados['petal length (cm)'][cont],dados['petal width (cm)'][cont])
    cont += 1

dados['target2'] = target2
#dados.to_excel('Blue\BlueEdTech\iris03.xlsx')
quant_setosa,quant_versicolor,quant_virgeinica = 0,0,0

for i in dados.index:
    
    if dados['target'][i] == 0.0:
        quant_setosa += 1
        
    elif dados['target'][i] == 1.0:
        quant_versicolor += 1
    else:
        quant_virgeinica += 1

filtro = dados['target'] != dados['target2']
filtro = dados[filtro]
print(filtro)
print(f'Setosas {cont_setosa}')
print(f'Versicilor {cont_versicolor}')
print(f'Virginica {cont_virginica}')

'''def acuracia(setosa,versicolor,virginica):
    if setosa > quant_setosa:
        setosa = quant_setosa
    if versicolor > quant_versicolor:
        versicolor = quant_versicolor
    if virginica > quant_virgeinica:
        virginica = quant_virgeinica
    accuracy = (setosa+versicolor+virginica)/tamanho_rows
    return accuracy


ac = acuracia(cont_setosa,cont_versicolor,cont_virginica)
print(ac)'''







